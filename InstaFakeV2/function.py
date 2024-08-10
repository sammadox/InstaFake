def is_fake_account(followers, following, posts, likes_per_post=None):
    """
    Determine if an Instagram account might be fake based on more nuanced metrics.
    
    Args:
    followers (int): Number of people following the account.
    following (int): Number of people the account is following.
    posts (int): Number of posts the account has made.
    likes_per_post (float, optional): Average number of likes per post, if known.
    
    Returns:
    bool: True if the account is likely fake, False otherwise.
    """
    # Suspicious if the following count is significantly higher than the followers count
    if following > 3 * followers:
        return True
    
    # Check for an unusually high followers to following ratio
    if followers > 50 * following:
        return True
    
    # Suspicious if there are very few posts but a high number of followers
    if posts < 5 and followers > 500:
        return True
    
    # Suspicious if there are no posts but the account has followers
    if posts == 0 and followers > 50:
        return True

    # Consider low engagement as a potential red flag
    if likes_per_post is not None and posts > 20:
        if likes_per_post < followers * 0.01:  # Less than 1% engagement per post
            return True
    
    return False
