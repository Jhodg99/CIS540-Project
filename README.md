# Repository for University of Michigan Dearborn CIS 540 
## Analysis of malicious link filtering by public search engines on trending topics and news
### All Relevant Code Relating to Project 2: Trending Topics Weaponization With Alternative Ideas

# Members:
Constantin Balan\
Alistair Clarke\
Jacob Hodgson\
Hannah Klooster\  
Bhanu Singh\

# Paper Abstract and Introduction
In this paper our goals are to understanding attackers' mentality by  analyzing e popular search engines on the internet for their ability to filter malicious websites which attempt to use trending topics and news stories to appear relevant when searched; compare abilities of (2) search engines to filter out suspicious and dangerous links to their users ; compare regional differences - (US as well as Global topics) ; compare categories of trending topics to each other, determining which ones are more prone to adversarial attack i.e. politics, or entertainment, or sports. In addition to this, we were able to complete our stretch goal a): compare multiple link analysis software tools to each other i.e., Virus Total, Hybrid Analysis. 

Trending topics derive online conversations & information flow, e.g., wars, pandemics, protests, elections, sport tournaments. Trending topics can also be misused by cybercriminals as weapons, by misusing trending terms for, registering to a domain, Blackhat SEO to maximize chance of visitors landing on a page and serve them with malware/compromise their environment. A website/server address can use a trending term that has links to malicious activity but classifier websites like VirusTotal / Hybrid Analysis verifies that the server is detected as malicious / suspicious because trending terms are as part of their keywords indexed by search engines.

# Tools

1. trending_topics_scraper is a Python Web Scraping tool for grabbing popular news stories and trending X.com hashtags to later be searched in different search engines and analyzed by popular free-to-use URL scanning tools
2. search_links_scraper is a Python Web Scraping tool which hits different search engines with popular new story titles and X.com hashtag keywords and stores the top-K return URLs to later be analyzed by the malware_scanning_apis tool
3. maleware_scanning_apis is a Python Script for querying free-to-use URL scanning APIs with relevant search engine URLs and later parses return data in readable and analyzable JSON format

All files contain proper how-to-use and readme files to fully understand the code in relation to our written paper.
