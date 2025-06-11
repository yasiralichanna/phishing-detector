import ssl
import socket
from datetime import datetime
from urllib.parse import urlparse

def analyze_ssl(url):
    """Analyze SSL certificate for potential issues"""
    issues = []
    
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname
        
        if not hostname:
            return ["Invalid URL"]
            
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Check expiration
                expire_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                if (expire_date - datetime.now()).days < 15:
                    issues.append(f"SSL expires soon ({expire_date})")
                
                # Check issuer
                issuer = dict(x[0] for x in cert['issuer'])
                if 'Let\'s Encrypt' in issuer.get('organizationName', ''):
                    issues.append("Uses Let's Encrypt certificate (common for phishing)")
                
                # Check subject
                subject = dict(x[0] for x in cert['subject'])
                if subject.get('organizationName', '').strip() == '':
                    issues.append("No organization in certificate")
                    
    except ssl.SSLCertVerificationError:
        issues.append("SSL certificate verification failed")
    except Exception as e:
        issues.append(f"SSL error: {str(e)}")
    
    return issues