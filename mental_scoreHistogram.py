import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'valorant_stats.csv'
data = pd.read_csv(file_path)

# Plot histogram for Mental State Scores
plt.figure(figsize=(10, 6))
data['Mental State'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel("Mental State Score")
plt.ylabel("Count")
plt.title("Distribution of Mental State Scores")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
