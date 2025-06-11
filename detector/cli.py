import argparse
from .core import PhishingDetector

def main():
    parser = argparse.ArgumentParser(description="Phishing Domain Detector")
    parser.add_argument("url", help="URL to check for phishing")
    parser.add_argument(
        "--phishtank-key",
        help="PhishTank API key (optional)",
        default=None,
    )
    parser.add_argument(
        "--json",
        help="Output results in JSON format",
        action="store_true",
    )
    
    args = parser.parse_args()
    
    detector = PhishingDetector(phishtank_api_key=args.phishtank_key)
    result = detector.analyze(args.url)
    
    if args.json:
        import json
        print(json.dumps(result, indent=2, default=str))
    else:
        print(f"\nURL: {args.url}")
        print(f"Phishing: {'YES' if result['is_phishing'] else 'NO'}")
        print(f"Score: {result['score']}/100")
        if result['indicators']:
            print("Indicators:")
            for indicator in result['indicators']:
                print(f"- {indicator}")

if __name__ == "__main__":
    main()