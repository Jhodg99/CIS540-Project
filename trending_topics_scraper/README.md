Scrape_Trends is a Python program which scrapes global news stories from a reputable news website. 
Scrape_Twitter_Trends is a Python program which scrapers trending hashtag and keywords off the popular social media site X (Twitter). This is done for both the USA and Worldwide trends.

Each day these two programs automatically run using a Windows Batch File. The BeautifulSoup library to send a get request to each of the two websites trending topic pages to get the trending stories/keywords/hashtags for the day. Upon gathering these stories, it stores them in a local text files to be further processed by the Google Auth Api.
Once these text files are gathered, using Google's Authentication API we can upload these files to a shared Project Google Drive to be processed later by other programs.

Files are stored by topic and date, for later analysis. 
For twitter, we include the region it is trending in (USA)
Topics include, politics, entertainment, world, health, and sports news

10/15/2023 -
Program was attempting to scrape other news websites (CNN, Fox, Twitter), but was rejected due to website Javascript.

10/21/2023 -
Program was updated to hit GlobalNews.Ca, grabbing entertainment, sports, and political news. Data stored only in text files

10/27/2023 - 
Program was updated to upload to Google Drive. Includes health and world news topics.

11/14/2023 -
A new file was added, scrape_twitter_trends.py does the same thing as described above, but scrapes a website which reports which hashtags and keywords are trending on the popular social media platform X (Twitter)

11/7/2023 - 
Readme updated
