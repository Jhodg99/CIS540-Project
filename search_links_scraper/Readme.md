# **Website Scraper using Topic keywords**
### _Keyword Extraction Function_

---
- Looks for files with .txt
- Determine if those files have the words sports, entertainment, politics, world or health
- Reads in the fetched file and then extracts keywords from those files based on string within quotation marks
- Iterates through those keywords and passes those keyword to bing_search, google_search functions
---

### _Bing Search Function_
---
- Uses the Bing Search v7 API to fetch web links using the keywords extracted by the Keyword Extraction Function
- The API pulls 15 web links per search keyword
- Targets the english language from: US, World regions
- Outputs the web links to a file
---

### _Google Search Function_
---
- Uses the Google Search library to fetch web links using the keywords extracted by the Keyword Extraction Function
- The API pulls 15 web links per search keyword
- Targets the english language from: US, World regions
- Outputs the web links to a file
---

