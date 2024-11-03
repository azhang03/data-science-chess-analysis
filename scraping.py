import requests
import pandas as pd
import time
import json
import re

API_TOKEN = ''

headers = {
    'Authorization': f'Bearer {API_TOKEN}'
}

response = requests.get('https://lichess.org/api/account', headers=headers)

# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Error fetching account data: {response.status_code}")

def get_team_members(team_id, full=False):
    """Fetch all users from a Lichess team."""
    url = f'https://lichess.org/api/team/{team_id}/users'
    params = {'full': str(full).lower()}
    response = requests.get(url)
    
    if response.status_code == 200:
        # Process the NDJSON response
        members = [json.loads(line) for line in response.iter_lines(decode_unicode=True)]
        return members
    else:
        print(f"Error fetching team members: {response.status_code}")
        return []

def get_user_games(username, max_games=100, retries=3):
    """Fetch game history for a specific Lichess user (PNG Format)."""
    url = f'https://lichess.org/api/games/user/{username}?max={max_games}&format=pgn'
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)  # Add timeout
            if response.status_code == 200:
                return response.text
            elif response.status_code == 429:
                print(f"Rate limit hit for user {username}. Retrying in {2 ** i} seconds...")
                time.sleep(2 ** i)  # Exponential backoff
            else:
                print(f"Error fetching games for user {username}: {response.status_code}")
                return ""
        except requests.exceptions.Timeout:
            print(f"Timeout occurred for user {username}. Retrying in {2 ** i} seconds...")
            time.sleep(2 ** i)
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error for user {username}: {e}")
            return ""
    return ""

def process_pgn_data(pgn_data):
    """Process PGN game data into structured format."""
    games = []
    # Blank line between games
    games_data = pgn_data.strip().split("\n\n")
    
    for game in games_data:
        game_info = {}

        # Re to check if it returns None
        def extract_field(regex, text, default="Unknown"):
            match = re.search(regex, text)
            return match.group(1) if match else default

        # Organize info, else = 'Unknown'
        game_info['event'] = extract_field(r'\[Event "(.*?)"\]', game)
        game_info['site'] = extract_field(r'\[Site "(.*?)"\]', game)
        game_info['date'] = extract_field(r'\[Date "(.*?)"\]', game)
        game_info['white'] = extract_field(r'\[White "(.*?)"\]', game)
        game_info['black'] = extract_field(r'\[Black "(.*?)"\]', game)
        game_info['result'] = extract_field(r'\[Result "(.*?)"\]', game)
        game_info['white_elo'] = extract_field(r'\[WhiteElo "(.*?)"\]', game)
        game_info['black_elo'] = extract_field(r'\[BlackElo "(.*?)"\]', game)
        game_info['time_control'] = extract_field(r'\[TimeControl "(.*?)"\]', game)
        game_info['eco'] = extract_field(r'\[ECO "(.*?)"\]', game)
        game_info['termination'] = extract_field(r'\[Termination "(.*?)"\]', game)

        # Extract all moves (assuming everything after the headers)
        moves = game.split("\n")[-1].strip()
        game_info['moves'] = moves

        games.append(game_info)
    
    return games

def save_to_csv(games, filename='lichess_user_games.csv'):
    """Save the collected game data to a CSV file."""
    df = pd.DataFrame(games)
    df.to_csv(filename, index=False)
    print(f"Saved {len(games)} games to {filename}")


def main():
    team_id = 'coders'  # Replace with the team id (I'm using coders for now)
    members = get_team_members(team_id)

    if members:
        all_games = []
        for member in members:
            username = member['id']  # 'id' = username
            print(f"Fetching games for user: {username}")
            pgn_data = get_user_games(username, max_games=10)  # Limit to 10 games per user for now
            if pgn_data:
                games = process_pgn_data(pgn_data)
                all_games.extend(games)
        save_to_csv(all_games, 'lichess_team_games.csv')
    else:
        print("No members found or error retrieving members.")

if __name__ == '__main__':
    main()






