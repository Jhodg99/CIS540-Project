# **Website Scraper using Topic keywords**
### _Keyword Extraction Function_

---
- Looks for files with .txt within local folders
- Fetches the topic_date information
- Reads in the fetched file and then extracts keywords from those files based on string within quotation marks for non-twitter topics
- Iterates through those keywords and passes those keyword to bing_search, google_search functions for weblink querying
---

### _Bing Search Function_
---
- Uses the Bing Search v7 API to fetch web links using the keywords extracted by the Keyword Extraction Function
- The API pulls 15 web links per search keyword
- Targets the english language for US & World regions
- Outputs the web links to a local file with [search_engine_topic_date_country] format
---

### _Google Search Function_
---
- Uses the Google Search library to fetch web links using the keywords extracted by the Keyword Extraction Function
- The API pulls 15 web links per search keyword
- Targets the english language for US & World regions
- Outputs the web links to a file with [search_engine_topic_date_country] format
---

