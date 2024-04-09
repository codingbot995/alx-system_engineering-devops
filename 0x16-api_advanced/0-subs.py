#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """Return doc type on the given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advance:v1.0.0 (by /u/bdov)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
