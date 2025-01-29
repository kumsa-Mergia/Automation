# Convert Excel to JSON
# Step 1: Install Required Libraries

# You need to install pandas and openpyxl (for reading Excel files).
# pip install pandas openpyxl

import pandas as pd

# Read the Excel file
excel_file = 'your_file.xlsx'
df = pd.read_excel(excel_file)

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', indent=4)

# Save JSON to a file (optional)
with open('output-Excel-JSON.json', 'w') as json_file:
    json_file.write(json_data)

print(json_data)
