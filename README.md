# API-Integration-and-Data-Vizualization
# Air Pollution Data Visualization

This project fetches air pollution data from the OpenWeatherMap API and visualizes the distribution of air pollution components in India using a pie chart. The chart displays the various pollutants in the air, highlighting the ones with the highest concentration.

## Features

- Fetches air pollution data from the OpenWeatherMap API.
- Displays a pie chart with the distribution of pollutants.
- Pollutants with a concentration lower than 1% are excluded from the chart.
- The chart is dynamically generated based on the latest data from the API.

## Prerequisites

Before running the code, ensure that you have the following installed:

- Python 3.x
- `requests` library
- `matplotlib` library

## Output
- The output of the script is a pie chart showing the relative distribution of air pollutants. The chart includes a legend that displays the pollutants with their corresponding concentrations in µg/m³.

### Installing the required libraries:

You can install the required libraries using `pip`:
```bash
pip install requests matplotlib

