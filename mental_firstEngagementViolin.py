import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'valorant_stats.csv'
data = pd.read_csv(file_path)

# Calculate the first engagement success ratio
data['First Engagement Success'] = data['FK(First Kills)'] / (data['FK(First Kills)'] + data['FD(First Deaths)'])

# Create a violin plot for First Engagement Success vs. Mental State
plt.figure(figsize=(12, 6))
sns.violinplot(x=data['Mental State'], y=data['First Engagement Success'], palette="muted")
plt.xlabel("Mental State Score")
plt.ylabel("First Engagement Success Ratio")
plt.title("First Engagement Success vs. Mental State")
plt.tight_layout()
plt.show()
