import csv
import requests

def predict_country_from_usernames(input_csv_path, output_csv_path):
    # URL of the Nationalize API
    api_url = "https://api.nationalize.io"
    
    # Read usernames from the input CSV
    with open(input_csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        usernames = list(reader)

    # Prepare results list with header
    results = [['username', 'country_id']]
    
    # Process each username
    for username in usernames[1:]:  # skip header
        # API request for each username
        response = requests.get(api_url, params={'name': username[0]})
        data = response.json()
        
        # Extract the most probable country code
        if data['country']:
            country_code = data['country'][0]['country_id'] if data['country'] else 'Unknown'
        else:
            country_code = 'Unknown'
        
        # Append the username and country code to results
        results.append([username[0], country_code])
    
    # Write the results to a new CSV file
    with open(output_csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)
    print(f'Results written to {output_csv_path}')


