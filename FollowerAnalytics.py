import json
import csv

# Load JSON data from a local file
with open('young_.mi_.ba_resultsq.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract names of followers if they exist
names = [entry.get('name', '') for entry in data if entry.get('name', '')]

# Write names to a CSV file, one name per line
with open('followers_names.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name'])
    for name in names:
        csvwriter.writerow([name])

print("CSV file 'followers_names.csv' has been created successfully.")
