from utils import read_and_display_json,extract_avg_likes
from scraper import scrape_details_from_username
import os

def is_fake_account(followers, following, posts, account_age_days, likes_per_post=None):
    """
    Determine if an Instagram account might be fake based on more nuanced metrics including account age,
    and provide the reason. Adaptations have been made to accommodate characteristics of large, legitimate accounts.
    
    Args:
    followers (int): Number of people following the account.
    following (int): Number of people the account is following.
    posts (int): Number of posts the account has made.
    account_age_days (int): Age of the account in days.
    likes_per_post (float, optional): Average number of likes per post, if known.
    
    Returns:
    tuple: (bool, str) where the bool indicates if the account is likely fake, and str is the reason.
    """
    # Context thresholds for large accounts and new accounts
    large_account_threshold = 10000  # Threshold for considering an account 'large'
    engagement_threshold_for_large_accounts = 0.005  # 0.5% engagement for large accounts
    new_account_threshold_days = 30  # Account is considered new if it's younger than 30 days

    # Suspicious if the following count is significantly higher than the followers count
    if following > 3 * followers:
        return (True, "Following count is significantly higher than followers count.")
    
    # Check for an unusually high followers to following ratio, exempting large accounts
    if followers > 50 * following and followers < large_account_threshold:
        return (True, "Followers to following ratio is unusually high.")

    # Adjust the threshold for very new accounts
    if account_age_days < new_account_threshold_days:
        if followers > 1000:
            return (True, "High number of followers for a very new account.")
        if posts > 30:
            return (True, "Unusually high number of posts for a very new account.")
    
    # Suspicious if there are very few posts but a high number of followers, adjust for large accounts
    if posts < 5 and followers > 500 and followers < large_account_threshold:
        return (True, "Very few posts but a high number of followers.")
    
    # Suspicious if there are no posts but the account has followers, adjust for large accounts
    if posts == 0 and followers > 50 and followers < large_account_threshold:
        return (True, "No posts but some followers are present.")
    
    # Consider engagement as a potential red flag, adjust threshold for large accounts
    if likes_per_post is not None and posts > 20:
        current_engagement_threshold = engagement_threshold_for_large_accounts if followers >= large_account_threshold else 0.01
        if likes_per_post < followers * current_engagement_threshold:
            return (True, f"Engagement rate is below {current_engagement_threshold * 100}% despite a reasonable number of posts.")
    
    return (False, "Account appears to be genuine.")





# Example usage
scrape_details_from_username('yyyell.l.e')
data=read_and_display_json('output.json')
avg_likes=extract_avg_likes('output.json')
print(is_fake_account(data[0],data[1],1000,29,avg_likes))  # Likely to be True, as following is much greater than followers and very few posts
# Check if the file exists and then delete it
if os.path.exists('output.json'):
    #os.remove('output.json')
    print(f"The file 'output.json' has been deleted successfully.")
else:
    print("The file does not exist.")

print(data)