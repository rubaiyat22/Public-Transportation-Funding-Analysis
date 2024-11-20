import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
data = pd.read_csv('/Users/rubaiyatrashid/Documents/GitHub/Public-Transportation-Funding-Analysis/data/cleaned/mta_turnstile_data_2022.csv')

data['Datetime'] = pd.to_datetime(data['Datetime'])
# Extract the hour from the DATETIME column
data['Hour'] = data['Datetime'].dt.hour

# Sum up entries and exits to get total ridership per hour
data['Total_Ridership'] = data['Entries'] + data['Exits']

# Group by hour and sum the total ridership
hourly_total_ridership = data.groupby('Hour')['Total_Ridership'].sum()

# Find the hour with the highest total ridership
peak_hour = hourly_total_ridership.idxmax()
peak_ridership = hourly_total_ridership.max()

# Plot total ridership by hour of day
plt.figure(figsize=(12, 6))
plt.plot(hourly_total_ridership.index, hourly_total_ridership.values, color='green')

# Adding titles and labels
plt.title('Total Ridership by Time of Day', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Total Ridership', fontsize=12)

# Mark the peak ridership hour
plt.axvline(x=peak_hour, color='red', linestyle='--', label=f'Peak Hour: {peak_hour}:00')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

# Print the peak ridership time and the total ridership during that hour
print(f"The peak ridership hour is {peak_hour}:00 with a total ridership of {peak_ridership} people.")
