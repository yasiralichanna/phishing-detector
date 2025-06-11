from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="phishing-detector",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package to detect phishing domains using multiple indicators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/phishing-detector",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/phishing-detector/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
    ],
    package_dir={"": "."},
    packages=find_packages(where="."),
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
        "python-whois>=0.8.0",
        "beautifulsoup4>=4.9.3",
        "urllib3>=1.26.0",
        "python-dateutil>=2.8.1",
        "tldextract>=3.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "flake8>=3.9.0",
            "black>=21.0",
            "mypy>=0.900",
        ],
    },
    entry_points={
        "console_scripts": [
            "phishing-detector=detector.cli:main",
        ],
    },
)