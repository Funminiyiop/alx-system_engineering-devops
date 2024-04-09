#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid
    """
    
    
    # Get data
    response = requests.request(
        'GET',
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={
            'User-Agent': 'my browser'
        },
        allow_redirects=False
    )
    
    # Check if successful
    if response.status_code == 200:
        # Get json data
        try:
            return(response.json().get('data').get('subscribers'))
        except:
            pass

    # Return 0 by default
    return(0)
