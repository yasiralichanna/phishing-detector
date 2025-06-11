import tldextract
from datetime import datetime, timedelta
from .phishtank import check_phishtank
from .openphish import check_openphish
from .ssl_analyzer import analyze_ssl
from .whois_utils import get_domain_age
from .patterns import check_suspicious_patterns

class PhishingDetector:
    def __init__(self, phishtank_api_key=None):
        self.phishtank_api_key = phishtank_api_key
    
    def analyze(self, url):
        """Analyze a URL for phishing indicators"""
        result = {
            'url': url,
            'is_phishing': False,
            'indicators': [],
            'score': 0
        }
        
        # Extract domain components
        extracted = tldextract.extract(url)
        domain = f"{extracted.domain}.{extracted.suffix}"
        
        # Check against phishing databases
        if self.phishtank_api_key:
            if check_phishtank(url, self.phishtank_api_key):
                result['is_phishing'] = True
                result['score'] += 80
                result['indicators'].append('Listed in PhishTank')
        
        if check_openphish(url):
            result['is_phishing'] = True
            result['score'] += 80
            result['indicators'].append('Listed in OpenPhish')
        
        # Check domain age
        age = get_domain_age(domain)
        if age and age < timedelta(days=30):
            result['score'] += 30
            result['indicators'].append(f'New domain ({age.days} days old)')
        
        # Check SSL certificate
        ssl_issues = analyze_ssl(url)
        if ssl_issues:
            result['score'] += len(ssl_issues) * 10
            result['indicators'].extend(ssl_issues)
        
        # Check suspicious patterns
        patterns = check_suspicious_patterns(url)
        if patterns:
            result['score'] += len(patterns) * 15
            result['indicators'].extend(patterns)
        
        # Determine final phishing status if not already confirmed
        if not result['is_phishing'] and result['score'] >= 65:
            result['is_phishing'] = True
        
        return result