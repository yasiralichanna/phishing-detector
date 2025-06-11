import requests

def check_openphish(url):
    """Check URL against OpenPhish community feed"""
    try:
        response = requests.get('https://openphish.com/feed.txt')
        if response.status_code == 200:
            return url in response.text
        return False
    except Exception:
        return False