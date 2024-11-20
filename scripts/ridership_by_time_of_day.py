import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
data = pd.read_csv('/Users/rubaiyatrashid/Documents/GitHub/Public-Transportation-Funding-Analysis/data/cleaned/mta_turnstile_data_2022.csv')

# Ensure the 'DATETIME' column is in datetime format
data['Datetime'] = pd.to_datetime(data['Datetime'])

# Extract hour from the 'DATETIME' column
data['Hour'] = data['Datetime'].dt.hour

# Calculate average entries and exits per hour
hourly_ridership = data.groupby('Hour')[['Entries', 'Exits']].mean()

# Plot the average ridership by time of day
plt.figure(figsize=(12, 6))
plt.plot(hourly_ridership.index, hourly_ridership['Entries'], label='Average Entries', color='blue')
plt.plot(hourly_ridership.index, hourly_ridership['Exits'], label='Average Exits', color='red')

# Adding titles and labels
plt.title('Average Ridership by Time of Day (Entries & Exits)', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Average Count', fontsize=12)

# Display legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
