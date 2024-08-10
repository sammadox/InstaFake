from apify_client import ApifyClient
import json

def scrape_details_from_username(username):
    # Initialize the ApifyClient with your API token
    client = ApifyClient("apify_api_Fve3I7NXgTy663nFemU5JSyeOsysUh4xv4rg")

    # Prepare the Actor input
    run_input = {"usernames": [username]}

    # Run the Actor and wait for it to finish
    run = client.actor("dSCLg0C3YEZ83HzYX").call(run_input=run_input)

    # Initialize a list to store the data
    data_to_save = []

    # Fetch Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)  # Print the item
        data_to_save.append(item)  # Append the item to the list

    # Save the fetched data to a JSON file
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
