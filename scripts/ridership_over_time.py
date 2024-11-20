import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('/Users/rubaiyatrashid/Documents/GitHub/Public-Transportation-Funding-Analysis/data/cleaned/mta_turnstile_data_2022.csv')

# Print the column names and first few rows to inspect
print(data.columns)
print(data.head())

# Assuming the columns are like: 'C/A', 'Unit', 'SCP', 'Line Name', 'Division', 'Date', 'Time', 'Entries', 'Exits'

# Ensure the 'DATETIME' column is in datetime format (in case it's not already)
data['Datetime'] = pd.to_datetime(data['Datetime'])

# Set 'DATETIME' as the index
data.set_index('Datetime', inplace=True)

# Aggregate total entries and exits by day (you can change this to month or hour depending on the granularity you want)
daily_ridership = data.resample('D')[['Entries', 'Exits']].sum()

# Plot total ridership over time
plt.figure(figsize=(12, 6))
plt.plot(daily_ridership.index, daily_ridership['Entries'], label='Total Entries', color='blue')
plt.plot(daily_ridership.index, daily_ridership['Exits'], label='Total Exits', color='red')

# Adding titles and labels
plt.title('Total Ridership Over Time (Entries & Exits)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Count', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()