# WallStreetBets Sentiment Analysis

This section of the project is dedicated to the analysis of data scraped from the WallStreetBets subreddit. It involves processing the collected data, performing sentiment analysis, and visualizing the results to understand the community's sentiment over time.

## Overview

The sentiment analysis is conducted on posts and comments fetched from the WallStreetBets subreddit. The goal is to gauge the overall sentiment within the community, identifying trends, and understanding how sentiment correlates with market events or specific topics discussed in the subreddit.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system and all necessary libraries are installed:

```
pip install -r requirements.txt
```

### Data Preparation

Before running the analysis, make sure you have the `wsb_posts.csv` file generated from the scraping part of the project. This file should be located in the appropriate directory accessible by the analysis scripts.

### Running the Analysis

To perform the sentiment analysis and generate visualizations, run the `data_processor.py` script:

### Data Preparation

Before running the analysis, make sure you have the `wsb_posts.csv` file generated from the scraping part of the project. This file should be located in the root directory.

### Running the Analysis

To perform the sentiment analysis and generate visualizations, run the `data_processor.py` script:


This script will load the data, clean it, perform sentiment analysis, and generate visualizations that highlight the sentiment trends over time.

## Analysis Details

- **Data Cleaning**: The script first cleans the data by removing unnecessary elements such as URLs, emojis, and special characters.
- **Sentiment Analysis**: Utilizes the VADER sentiment analysis tool to assess the sentiment of each post and comment.
- **Visualization**: Generates plots to visualize the sentiment trends over time, helping to identify periods of high positive or negative sentiment.

## Results

The results of the analysis, including any generated plots, will be saved in the designated output directory. These results provide insights into the community's sentiment, potentially correlating with market movements or significant events.

## Contributing

Contributions to the analysis are welcome. If you have suggestions for improving the analysis or adding new features, please feel free to contribute.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
