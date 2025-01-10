import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'valorant_stats.csv'
valorant_data = pd.read_csv(file_path)

# Calculate Aggression (First Kills + First Deaths)
valorant_data['Aggression'] = valorant_data['FK(First Kills)'] + valorant_data['FD(First Deaths)']

# Group by Mental State and calculate average aggression
mental_state_vs_aggression = valorant_data.groupby('Mental State')['Aggression'].mean()

# Sorting the data for a more dynamic presentation
mental_state_vs_aggression = mental_state_vs_aggression.sort_index()

# Create a bar chart with distinct color emphasis
plt.figure(figsize=(12, 6))
bars = plt.bar(
    mental_state_vs_aggression.index,
    mental_state_vs_aggression.values,
    color=['#FF5733' if val > mental_state_vs_aggression.mean() else '#3498DB'
           for val in mental_state_vs_aggression.values],
    edgecolor='black'
)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 0.1,
        f'{height:.1f}',
        ha='center',
        va='bottom',
        fontsize=10
    )

# Customize the chart
plt.title('Impact of Mental State on Aggression', fontsize=16, fontweight='bold')
plt.xlabel('Mental State Score', fontsize=12)
plt.ylabel('Average Aggression (First Kills + First Deaths)', fontsize=12)
plt.xticks(mental_state_vs_aggression.index, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the chart
plt.show()
