import os
import re
import sys
import time
import glob
import requests
import subprocess
import asyncio
from datetime import datetime
from decouple import config
from duckduckgo_search import DDGS
from googlesearch import search

# Run Google Drive File Fetch to get topics, before executing other code blocks
#subprocess.run(['python', 'gdrive_file_fetch.py'], check=True)

class KeyExtractor():

    def __init__(self):

        self.curr_path = os.getcwd() #get current working directory path 
        self.curr_datetime = datetime.now() #get current date and time
        self.timestamp = self.curr_datetime.strftime("%Y_%m_%d") #format datetimestamp
        self.subscription_key = config('subscription_key', default='') #read bing key from .env file
        self.bing_search_url = "https://api.bing.microsoft.com/v7.0/search" #specify bing search api endpoint

        self.google_search_count = 0
        self.bing_search_count = 0
        
    def file_dir_chk(self):
        # List folder names within current directory
        with os.scandir(self.curr_path) as entries:
            folders = [entry.name for entry in entries if entry.is_dir()]

        #iterate through folder array and prepend directory name
        prefix = self.curr_path + "\\"
        folder_dirs = [prefix + elem for elem in folders]

        return folder_dirs #return array with folder paths
    
    async def keyword_extraction(self):

        folders = self.file_dir_chk() #fetch folder directories for scraped topics

        for path in folders:

            topic = path.split('\\')[-1]

            txt_files = glob.glob(os.path.join(path, "*.txt")) #find .txt files

            for file in txt_files: #iterate through files

                if 'twitter' in file: #check file_name

                    with open(file, "r", encoding="utf8") as txt_file: #open file and read file

                        contents =  txt_file.read() #get file contents

                        await self.bing_search(contents, 'en-US', 5, topic)
                        await self.bing_search(contents, 'en-GB', 5, topic)
                        await self.bing_search(contents, 'en-KR', 5, topic)
                        await self.bing_search(contents, 'en-CN', 5, topic)
                        await self.bing_search(contents, 'en-RU', 5, topic)

                        await self.google_search(contents, 'en', 'countryUS', 5, topic)
                        await self.google_search(contents, 'en', 'countryUK', 5, topic)
                        await self.google_search(contents, 'en', 'countryIL', 5, topic)
                        await self.google_search(contents, 'en', 'countryCN', 5, topic)
                        await self.google_search(contents, 'en', 'countryRU', 5, topic)   

                else:

                    with open(file, "r") as txt_file: #open file and read file

                        contents =  txt_file.read() #get file contents

                        matched_words = re.findall("‘(.*?)’", contents) #extract words/keywords within quotation marks

                        for keywords in matched_words:
                                
                            await self.bing_search(keywords, 'en-US', 5, topic)
                            await self.bing_search(keywords, 'en-GB', 5, topic)
                            await self.bing_search(keywords, 'en-KR', 5, topic)
                            await self.bing_search(keywords, 'en-CN', 5, topic)
                            await self.bing_search(keywords, 'en-RU', 5, topic)

                            await self.google_search(keywords, 'en', 'countryUS', 5, topic)
                            await self.google_search(keywords, 'en', 'countryUK', 5, topic)
                            await self.google_search(keywords, 'en', 'countryIL', 5, topic)
                            await self.google_search(keywords, 'en', 'countryCN', 5, topic)
                            await self.google_search(keywords, 'en', 'countryRU', 5, topic)                          

    async def bing_search(self, query, region, num, topic):

        if self.bing_search_count > 15:
            await asyncio.sleep(900)

        file_name = "bing_"+topic+"_search_results_"+self.timestamp+"_"+region+".txt" #out file name

        headers = {"Ocp-Apim-Subscription-Key": self.subscription_key}
        params = {"q": query, "safesearch": "Off","textDecorations": True, "textFormat": "HTML", "count": num, "mkt":region}

        response = requests.get(self.bing_search_url, headers=headers, params=params)
        
        if response.status_code == 429:

            time.sleep(10) #delay for 10 secs to wait for the rate limit window to reset

            response = requests.get(self.bing_search_url, headers=headers, params=params)

        elif response.status_code == 200: #if http get request was successful

            search_results = response.json() #fetch json response object

            with open(file_name, "a") as file:

                if 'webPages' in search_results:

                    for result in search_results["webPages"]["value"]:
                        url = result["url"]

                        file.write(f"{url}\n") #write to file
                        print(f"Saving Bing Search: {url} to the file")

                        self.search_count+=1

        else:
            print(f"HTTP get response was {response.status_code}")
    

    async def google_search(self, query, lang, country, num, topic):

        if self.google_search_count > 15:
            await asyncio.sleep(900)

        file_name = "google_"+topic+"_search_results_"+self.timestamp+"_"+country+".txt" #out file name

        with open(file_name, "a") as file:

            for link in search(query, tld="co.in", lang=lang, country=country, stop=num, pause=5): #google_search function finds links of top 10

                try:
                    response = requests.head(link, allow_redirects=True)

                    if response.status_code == 429:

                        time.sleep(15) #delay for 10 secs to wait for the rate limit window to reset

                        response = requests.head(link, allow_redirects=True)

                    elif response.status_code == 200 and response.url.startswith("http"):

                        file.write(f"{link}\n") #write to file
                        print(f"Saving Google Search: {link} to the file.") #output progress

                        self.search_count+=1

                except requests.RequestException as e:
                    print(f"Failed to fetch URL: {link}, Error: {e}")


if __name__ == "__main__":

    find_key = KeyExtractor() #create object for class

    try:
        asyncio.run(find_key.keyword_extraction())
    except KeyboardInterrupt:
        sys.exit() #exit