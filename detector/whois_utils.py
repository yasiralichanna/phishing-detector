import whois
from datetime import datetime

def get_domain_age(domain):
    """Get the age of a domain in days"""
    try:
        domain_info = whois.whois(domain)
        
        if isinstance(domain_info.creation_date, list):
            creation_date = domain_info.creation_date[0]
        else:
            creation_date = domain_info.creation_date
            
        if not creation_date:
            return None
            
        return datetime.now() - creation_date
    except Exception:
        return None