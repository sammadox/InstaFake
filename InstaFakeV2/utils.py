import json
from datetime import datetime

def read_and_display_json(file_path):
    # Try to open the file and read the data
    res=[]
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            res.append(data[0]['followersCount'])
            res.append(data[0]['followsCount'])
            res.append(data[0]['postsCount'])
            return(res)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")


def extract_avg_likes(file_path):
    # Try to open the file and read the data
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            likes_counts = [post['likesCount'] for post in data[0]['latestPosts']]
            # Calculate the average likes count
            average_likes = sum(likes_counts) / len(likes_counts) if likes_counts else 0
            return(average_likes)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_account_date(file_path):
    # Try to open the file and read the data
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            #Retrieve all posts date
            posts_date = [post['timestamp'] for post in data[0]['latestPosts']]
            return(posts_date)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_recent_account(file_path):
    # Try to open the file and read the data
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            #Retrieve all posts date
            is_recent = data[0]['joinedRecently']
            return(is_recent)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

def oldest_post(timestamps):


print(is_recent_account('output.json'))
# Usage example (you need to replace 'path_to_your_file.json' with the actual file path)
