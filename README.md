# Movies Dataset EDA (Exploratory Data Analysis)

## Overview

This program performs exploratory data analysis (EDA) on a movies dataset (`movies.csv`). It includes data loading, initial inspection, handling missing values, detecting and removing duplicates, and generating various visualizations to understand the data better.

## Author

Written by Muhammad Yousaf  
Email: yousafsahiwal3@gmail.com

## Features

1. **Data Loading**: Load the dataset from a CSV file.
2. **Initial Inspection**: Display the first few rows, dataset information, summary statistics, and check for missing values.
3. **Data Cleaning**: Handle missing values by filling them with the median of respective columns, and remove duplicate rows.
4. **Exploratory Data Analysis**:
   - **Distribution of Numerical Features**: Histograms for numerical features.
   - **Correlation Heatmap**: Heatmap showing the correlation between numerical features.
   - **Distribution of Categorical Features**: Count plots for categorical features.
   - **Grouping and Aggregation**: Group data by categorical features and calculate the mean of numerical features.
5. **Save Cleaned Dataset**: Save the cleaned dataset to a new CSV file.

## Installation

To run this program, you need to have the following libraries installed:

- pandas
- numpy
- matplotlib
- seaborn

You can install them using pip:

```bash
pip install pandas numpy matplotlib seaborn
