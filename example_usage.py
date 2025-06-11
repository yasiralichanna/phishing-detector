from detector.core import PhishingDetector

# Initialize with your PhishTank API key (optional)
detector = PhishingDetector(phishtank_api_key='your_api_key_here')

# Example URLs to check
urls = [
    'https://www.paypal.com',
    'https://paypal-verify-account.com',
    'https://secure-login-facebook.xyz',
    'https://github.com'
]

for url in urls:
    result = detector.analyze(url)
    print(f"\nURL: {url}")
    print(f"Phishing: {'YES' if result['is_phishing'] else 'NO'}")
    print(f"Score: {result['score']}/100")
    if result['indicators']:
        print("Indicators:")
        for indicator in result['indicators']:
            print(f"- {indicator}")