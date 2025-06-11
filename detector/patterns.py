import re

def check_suspicious_patterns(url):
    """Check for suspicious patterns in the URL"""
    suspicious = []
    
    # Common phishing patterns
    patterns = [
        (r'login[-.]?[a-z0-9]*[-.]?[a-z0-9]*\.', 'Contains "login" in subdomain'),
        (r'secure[-.]?[a-z0-9]*[-.]?[a-z0-9]*\.', 'Contains "secure" in subdomain'),
        (r'account[-.]?[a-z0-9]*[-.]?[a-z0-9]*\.', 'Contains "account" in subdomain'),
        (r'verify[-.]?[a-z0-9]*[-.]?[a-z0-9]*\.', 'Contains "verify" in subdomain'),
        (r'web[-.]?[a-z0-9]*[-.]?[a-z0-9]*\.', 'Contains "web" in subdomain'),
        (r'\.(tk|ml|ga|cf|gq)$', 'Uses free domain extension'),
        (r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', 'Contains IP address directly'),
        (r'@', 'Contains @ symbol (possible credential embedding)'),
        (r'-(.+)-', 'Contains hyphens around text (common in phishing)')
    ]
    
    for pattern, message in patterns:
        if re.search(pattern, url, re.IGNORECASE):
            suspicious.append(message)
    
    return suspicious