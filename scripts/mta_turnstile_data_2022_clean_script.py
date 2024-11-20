import pandas as pd

# Load the dataset
file_path = 'data/raw/mta_turnstile_data_2022.csv'  # Update the path as needed
df = pd.read_csv(file_path)

# Print the first few rows to understand the structure
print(df.head())

# Clean column names by stripping any extra spaces
df.columns = df.columns.str.strip()

# Check for missing values in each column
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# OR: Fill missing values with a default (e.g., 0 for numeric columns)
df['Entries'] = df['Entries'].fillna(0)
df['Exits'] = df['Exits'].fillna(0)

# Convert 'Date' and 'Time' to string (if they are not already in string format)
df['Date'] = df['Date'].astype(str)
df['Time'] = df['Time'].astype(str)

# Combine 'Date' and 'Time' into a single datetime column
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%Y-%m-%d %H:%M:%S')

# Optionally, drop the original 'Date' and 'Time' columns
df = df.drop(columns=['Date', 'Time'])

# Convert 'Entries' and 'Exits' columns to numeric values, coercing errors to NaN
df['Entries'] = pd.to_numeric(df['Entries'], errors='coerce')
df['Exits'] = pd.to_numeric(df['Exits'], errors='coerce')

# Remove rows with negative entries or exits
df = df[(df['Entries'] >= 0) & (df['Exits'] >= 0)]

# Check data types
print(df.dtypes)

# Save the cleaned dataset
df.to_csv('data/cleaned/mta_turnstile_data_2022.csv', index=False)
