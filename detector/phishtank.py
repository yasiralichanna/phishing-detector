import requests
from urllib.parse import urlparse

def check_phishtank(url, api_key):
    """Check URL against PhishTank database"""
    try:
        parsed = urlparse(url)
        if not parsed.scheme:
            url = 'http://' + url
            
        params = {
            'format': 'json',
            'url': url,
            'app_key': api_key
        }
        
        response = requests.post(
            'https://checkurl.phishtank.com/checkurl/',
            data=params
        )
        data = response.json()
        
        return data.get('results', {}).get('in_database', False)
    except Exception:
        return False