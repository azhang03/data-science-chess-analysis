# Chess Performance Analysis using Data Science

A comprehensive data science project analyzing chess games to uncover patterns in player performance, mistake rates, and outcome predictions using advanced machine learning techniques.

### A higher-level presentation of this project can be found on [USC's Statistics Seminar Youtube](https://www.youtube.com/watch?v=7AM4lGa9hoQ)

## Project Overview

This project uses the Lichess API to collect and analyze chess game data from multiple teams, focusing on Stockfish-analyzed games to extract performance metrics and identify patterns across different player skill levels.

## Key Findings

- **White Advantage**: Statistical analysis confirms a significant advantage for white pieces.
- **Mistake Patterns**: Lower-rated players make significantly more mistakes and blunders than higher-rated players.
- **Game Outcome Prediction**: Neural networks and logistic regression models successfully predict game outcomes based on player ratings and mistake frequencies.
- **Performance Clustering**: PCA and K-means clustering reveals distinct player performance clusters based on mistake patterns.

## Files and Contents

### Data Collection
- **Super Duper Lichess Scraper 5000.ipynb**: Code for collecting Stockfish-analyzed games from Lichess players across multiple teams. Extracts game data including player ratings, moves, and annotations for mistakes, inaccuracies, and blunders.

### Data Analysis
- **analyses.ipynb**: Contains statistical analysis including:
  - Win rate calculations for white and black pieces
  - Statistical tests (Z-tests) comparing mistake patterns across ELO ranges
  - Analysis of inaccuracies, mistakes, and blunders by player rating
  - Hypothesis testing to verify significant differences between rating groups

### Machine Learning Models
- **Neural.ipynb**: Contains complex model implementations including:
  - Neural network models for game outcome prediction
  - TF-IDF vectorization of chess moves for pattern recognition
  - Transformer-based models analyzing game sequence patterns
  - PCA visualization and clustering of game characteristics
  - Comparison of model performance metrics
  
### Statistical Modeling
- Contains logistic regression models examining the relationship between:
  - Player ratings and game outcomes
  - Mistake frequencies and win probabilities
  - The effect of blunders vs. smaller mistakes on game outcomes
  - Likelihood ratio tests validating model significance

## Technologies Used
- Python (Pandas, NumPy, SciPy)
- TensorFlow/Keras for neural networks
- Scikit-learn for machine learning algorithms
- Statistical testing (Z-tests, hypothesis testing)
- PCA and K-means for dimensionality reduction and clustering
- Lichess API for data collection

## How to Reproduce
1. Generate a Lichess API key
2. Run the scraper notebook to collect game data
3. Run analysis notebooks to perform statistical tests and train models
4. Game data is processed to extract inaccuracies, mistakes, and blunders using Stockfish analysis

## Conclusions
- White has a statistically significant advantage over black
- Lower-rated players make significantly more mistakes than higher-rated players
- The relationship between player rating and mistake frequency follows a clear pattern
- Game outcomes can be predicted with reasonable accuracy using both neural networks and traditional statistical models
- Machine learning models can identify meaningful patterns in chess games that correlate with player skill levels

## Expandables for those interested...
- Expand dataset with games from more diverse player pools
- Incorporate more advanced chess metrics such as piece development and positional advantage
- Develop real-time prediction models for ongoing games
- Analyze specific openings and their success rates at different ELO ranges
