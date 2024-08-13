#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

def number_of_subscribers(subreddit):
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set the headers with a custom User-Agent
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0 (by /u/yourusername)"}
    
    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0

        return 0
