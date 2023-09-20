# Python Cloud Project - Job Data Fetcher

## Overview
Fetch job data from [The Muse API](https://www.themuse.com/developers/api/v2) and save it to an AWS S3 bucket.

## Steps
1. **Setup**: Create an AWS EC2 instance and set up your Python environment via VSCode SSH.
2. **Fetch Data**: Use Python's `requests` library to fetch job data.
3. **Data Parsing**: Extract relevant fields using Python and convert to a DataFrame with `pandas`.
4. **Data Manipulation**: Clean and restructure the data.
5. **Save to S3**: Use either `boto3` or AWS CLI to save the data to an S3 bucket.

## Data Fields
- Company Name
- Job Name
- Job Type
- Location (Country & City)
- Publication Date

## Requirements
- Shell script for environment setup
- `.gitignore`
- Python run script
- Optional: `toml` for config parameters
- Secrets file

## Diagram
![Project Diagram](https://user-images.githubusercontent.com/108837052/192905682-28b6f3b9-0dee-4782-8902-a0a1e4efcf4c.png)
