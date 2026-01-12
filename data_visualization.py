import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("titanic_cleaned.csv")
os.makedirs("visualizations", exist_ok=True)


# Line plot
df['Age'].sort_values().reset_index(drop=True).plot()
plt.savefig("visualizations/line_age.png")
plt.clf()

# Scatter plot
plt.scatter(df['Age'], df['Fare'])
plt.savefig("visualizations/scatter_age_fare.png")
plt.clf()

# Histogram
df['Pclass'].hist()
plt.savefig("visualizations/hist_pclass.png")
plt.clf()

# Bar chart
df.groupby('Sex')['Survived'].mean().plot(kind='bar')
plt.savefig("visualizations/bar_survival.png")
plt.clf()

# Box plot
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.savefig("visualizations/box_fare.png")
plt.clf()

# Violin plot
sns.violinplot(x='Sex', y='Age', data=df)
plt.savefig("visualizations/violin_age.png")
plt.clf()

# Heatmap
sns.heatmap(df.corr(), annot=True)
plt.savefig("visualizations/heatmap.png")
plt.clf()

# Pair plot
sns.pairplot(df.select_dtypes(include='number'))
plt.savefig("visualizations/pairplot.png")
