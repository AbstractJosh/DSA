import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'valorant_stats.csv'
data = pd.read_csv(file_path)

# Convert Date to datetime for accurate time series plotting
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Sort data by Date to maintain order for time series
data = data.sort_values(by='Date')

# Plot scatter plot with regression line
plt.figure(figsize=(12, 6))
sns.regplot(x=data['Date'].map(pd.Timestamp.toordinal),  # Convert datetime to ordinal for regression
            y=data['ACS(Average Combat Score)'],
            scatter=True, line_kws={"color": "red"}, scatter_kws={"alpha": 0.6})
plt.xticks(data['Date'].map(pd.Timestamp.toordinal), data['Date'].dt.strftime('%d-%m-%Y'), rotation=45)
plt.xlabel("Time (Date)")
plt.ylabel("Average Combat Score (ACS)")
plt.title("Performance Improvement Over Time: ACS vs. Time")
plt.tight_layout()
plt.show()