Scrape_Trends is a Python program which scrapes global news stories from a reputable news website. 

Each day it uses the BeautifulSoup library to send a get request to each of the websites topic pages to get the trending stories for the day. Upon gathering these stories, it stores them in a local text files to be further processed
Once these text files are gathered, using Google's Authentication API we can upload these files to a shared Project Google Drive to be processed later by other programs.

Files are stored by topic and date, for later analysis
Topics include, politics, entertainment, world, health, and sports news
Program is run through a Windows Batch Job daily.

10/15/2023 -
Program was attempting to scrape other news websites (CNN, Fox, Twitter), but was rejected due to website Javascript.

10/21/2023 -
Program was updated to hit GlobalNews.Ca, grabbing entertainment, sports, and political news. Data stored only in text files

10/27/2023 - 
Program was updated to upload to Google Drive. Includes health and world news topics.

11/7/2023 - 
Readme updated