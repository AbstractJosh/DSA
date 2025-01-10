import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'valorant_stats.csv'
data = pd.read_csv(file_path)

# Calculate Total Fights (First Kills + First Deaths)
data['Total Fights'] = data['FK(First Kills)'] + data['FD(First Deaths)']

# Normalize Total Fights
data['Normalized Fights'] = data['Total Fights'] / data['Total Fights'].max()

# Calculate Aggression metric
data['Aggression'] = data['Normalized Fights'] * data['Mental State']

# Create a scatter plot with regression line for Aggression Metric vs. ACS
plt.figure(figsize=(12, 6))
sns.regplot(x=data['Aggression'], y=data['ACS(Average Combat Score)'], scatter=True, line_kws={"color": "red"}, scatter_kws={"alpha": 0.6})
plt.xlabel("Aggression Metric")
plt.ylabel("Average Combat Score (ACS)")
plt.title("ACS vs. Aggression Metric")
plt.tight_layout()
plt.show()
