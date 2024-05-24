#Movies Dataset EDA (Exploratory Data Analysis) By Muhammad yousaf

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('movies.csv')

print("First few rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include='all'))

print("\nMissing Values:")
print(df.isnull().sum())

df.fillna(df.median(numeric_only=True), inplace=True)

print("\nDuplicate Rows:")
print(df.duplicated().sum())


df.drop_duplicates(inplace=True)

numerical_features = df.select_dtypes(include=[np.number]).columns
df[numerical_features].hist(bins=15, figsize=(10, 5), layout=(1, len(numerical_features)))
plt.suptitle('Distribution of Numerical Features')
plt.show()
plt.figure(figsize=(10, 6))
correlation_matrix = df[numerical_features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
categorical_features = df.select_dtypes(include=[object]).columns
for feature in categorical_features:
    plt.figure(figsize=(10, 5))
    sns.countplot(y=df[feature], order=df[feature].value_counts().index)
    plt.title(f'Distribution of {feature}')
    plt.show()




print("\nGrouping by a categorical feature and calculating mean of numerical features:")
for cat_feature in categorical_features:
    if df[cat_feature].nunique() < 100: 
        print(df.groupby(cat_feature)[numerical_features].mean())

df.to_csv('cleaned_movies_data.csv', index=False)
print("\nEDA Complete. Cleaned dataset saved as 'cleaned_movies_data.csv'.")
