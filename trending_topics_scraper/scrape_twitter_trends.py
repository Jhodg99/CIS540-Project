from datetime import datetime, timedelta, date
from bs4 import BeautifulSoup
import requests
import time
import re
import os 
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 

# C:\Users\Jake\AppData\Local\Programs\Python\Python37\python.exe
def query_twitter_trend(topic):
    headers={'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    if topic == "USA":
        base_url = 'https://trends24.in/united-states/'
        driveName = "twitter_USA_" + str(date.today()) + ".txt"
        relativeFileName =  "twitter_USA_" + str(date.today()) + ".txt"
        fileName = "../twitter" + "/twitter" + "_USA_" + str(date.today()) + ".txt"
    else:
        base_url = 'https://trends24.in'
        driveName = "twitter_" + str(date.today()) + ".txt"
        relativeFileName =  "twitter_" + str(date.today()) + ".txt"
        fileName = "../twitter" + "/twitter" + "_" + str(date.today()) + ".txt"

    # getting the url
    r = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    news_lis = soup.find_all("div", {"class": "trend-card"})
    f = open(fileName, "w", encoding="utf-8")
    for div in news_lis:
        for li in div.find_all('li'):
            headline = li.find('a').text
            print("headline:", headline)
            tweets = li.find('span')
            if tweets != None:
                tweets = li.find('span').text
                f.write(str(headline) + " - " + str(tweets) + "\n")
            else: 
                f.write((str(headline) + "\n"))

        break

    f.close()

    # replace the value of this variable 
    # with the absolute path of the directory 
    path = "C:\\Users\\Jake\\Documents\\CIS540Project\\twitter"
    # iterating thought all the files/folder 
    # of the desired directory 
    file_metadata = {'title': driveName, "parents": [{"id": "1_-nIQobagdwVCv88ehtoWx8gKsedJ02C"}]}
    f = drive.CreateFile(file_metadata) 
    f.SetContentFile(os.path.join(path, relativeFileName)) 
    f.Upload() 

    return

if __name__ == '__main__':
    # Below code does the authentication 
    # part of the code 
    gauth = GoogleAuth() 

    # Creates local webserver and auto 
    # handles authentication. 
    gauth.LocalWebserverAuth()        
    drive = GoogleDrive(gauth) 

    # replace the value of this variable 
    # with the absolute path of the directory 

    topics = ["USA", "World"]

    for i in topics:
        path = "C:\\Users\\Jake\\Documents\\CIS540Project\\" + i
        
        try:
            query_twitter_trend(i) 

        # except is for handling the errors
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            print('request time out')
            input()
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print('too many redirect')
            input()
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            print('request unknown error')
            input()