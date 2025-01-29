#  Convert CSV to JSON
# Install Required Libraries

# You only need pandas for handling CSV files.
#     pip install pandas

import pandas as pd

# Read the CSV file
csv_file = './original/data.csv'
df = pd.read_csv(csv_file)

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', indent=4)

# Save JSON to a file (optional)
with open('output-CSV-JSON.json', 'w') as json_file:
    json_file.write(json_data)

print(json_data)