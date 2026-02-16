Project 11: Multi-Threaded Web Archiving and Audit Suite
Overview

This project is a high-concurrency web crawler designed for site mirroring and automated security auditing. Unlike standard sequential downloaders, this suite utilizes parallel processing to extract assets and map internal directory structures while simultaneously conducting a performance and security header analysis.

Technical Stack
Python 3

Requests: Utilized for session-based HTTP communication and custom header injection.

BeautifulSoup4: Implemented for DOM tree traversal and precise link/asset extraction.

Concurrent.futures: Facilitates multi-threaded execution to optimize I/O throughput.

Standard Library (OS, JSON, Time): Used for automated file system management and data persistence.

Core Functionality
Parallel Asset Extraction: Employs a ThreadPoolExecutor to handle multiple asset downloads concurrently, significantly reducing total execution time.

Identity Masking: Implements custom User-Agent headers to emulate standard browser behavior and bypass basic anti-scraping mechanisms.

Automated Audit Reports: Generates a structured JSON manifest upon completion, detailing execution duration, total disk usage, and a map of discovered internal resources.

Directory Sanitization: Automatically handles domain-based directory creation and manages a structured storage hierarchy for HTML, media, and technical logs.

Storage Auditing: Performs a post-cloning calculation of the local repository size to provide a clear footprint of the archived data.

Installation and Execution
Ensure all dependencies are met by running:
pip install requests beautifulsoup4

Execute the primary controller:
python cloner.py

Provide the target URL when prompted. The system will initialize the directory structure and begin the concurrent extraction process.