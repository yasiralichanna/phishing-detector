# Phishing Domain Detector 

A Python tool to detect potential phishing domains by analyzing multiple security indicators in real-time.

![Phishing Detection](https://img.shields.io/badge/security-phishing%20detection-red) 
![Python](https://img.shields.io/badge/python-3.6%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features 

-  Checks against PhishTank and OpenPhish databases
-  Analyzes SSL certificate validity and details
-  Checks domain age (new domains are suspicious)
-  Detects suspicious URL patterns
-  Scores domains based on risk factors
-  Easy to install and use via CLI or Python API
-  Compatible with Python 3.6+

## Installation 📥

### Prerequisites
- Python 3.6+
- pip package manager

### Method 1: From GitHub (recommended)
```bash
pip install git+https://github.com/yourusername/phishing-detector.git
```
###**Method 2: Install from source**
```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
pip install -r requirements.txt
pip install -e .
```
**Usage Examples
Command Line Interface**
**Basic check:**
```bash
phishing-detector "https://example.com"
```
**With PhishTank integration**:
```bash
phishing-detector "https://example.com" --phishtank-key YOUR_API_KEY
```
**JSON output format:**
```bash
phishing-detector "https://example.com" --json
