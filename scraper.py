from apify_client import ApifyClient
import json

def run_actor_with_cookies(username):
    # Initialize the ApifyClient with your API token
    client = ApifyClient("apify_api_Fve3I7NXgTy663nFemU5JSyeOsysUh4xv4rg")

    # Load Instagram cookies from a local JSON file
    with open('instagram_cookies.json', 'r') as file:
        cookies = json.load(file)

    # Prepare the Actor input, including Instagram cookies
    run_input = {
        "target_username": username,
        "insta_cookie": cookies
    }

    # Run the Actor and wait for it to finish
    run = client.actor("bhansalisoft/instagram-follower-scraper").call(run_input=run_input)

    # Fetch all Actor results from the run's dataset
    results = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        results.append(item)
    
    # Save results to a local JSON file
    with open(f'{username}_results.json', 'w') as f:
        json.dump(results, f, indent=4)

    print(f"Saved results to '{username}_results.json'")


