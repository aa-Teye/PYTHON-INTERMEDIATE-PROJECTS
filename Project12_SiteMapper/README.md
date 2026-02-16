# Project 12: Site Mapper and Link Validator

## What this tool does
I built this script to solve the problem of manual link checking. It acts as an automated crawler that walks through a website, finds every internal link, and checks if the page actually loads. It’s essentially a "smoke test" for a site's entire architecture.

## How it works
The script uses a concurrent worker strategy (Multi-threading). Instead of checking pages one-by-one, it opens multiple connections to speed up the process. 

For every link it finds, it records the HTTP status:
- **200**: The page is healthy and accessible.
- **404**: The link is broken and needs to be fixed.
- **500**: The server crashed trying to load that page.



## Tech used
- **Python 3**
- **Requests & BeautifulSoup**: For handling network calls and parsing the HTML.
- **ThreadPoolExecutor**: To handle the simultaneous "pinging" of URLs.
- **JSON/XML**: To save the results in formats that are actually useful for audits or SEO.

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Run the script: `python mapper.py`
3. Enter the URL you want to audit.

## Results
- **site_audit.json**: This is the raw data. It lists every URL and its status code.
- **sitemap.xml**: A standard map of the site that you can submit to Google.