from datetime import datetime, timedelta, date
from bs4 import BeautifulSoup
import requests
import time
import mysql.connector
import re
import os 
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 

# C:\Users\Jake\AppData\Local\Programs\Python\Python37\python.exe
def query_google_trend():
    headers={'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    trendType = "entertainment"
    base_url = 'https://globalnews.ca/' + trendType + "/"
    # getting the url
    r = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    news_lis = soup.find_all("li", {"class": "c-posts__item c-posts__loadmore"})
    fileName = trendType + "/" + trendType + "_" + str(date.today()) + ".txt"
    driveName = trendType + "_" + str(date.today()) + ".txt"
    f = open(fileName, "w")
    for li in news_lis:
        headline = li.find("span", {"class": "c-posts__headlineText"})
        print("headline:", headline.string)
        f.write((str(headline.text) + "\n"))

    f.close()

    # replace the value of this variable 
    # with the absolute path of the directory 
    path = r"C:\Users\Jake\Documents\CIS540Project\entertainment"

    # iterating thought all the files/folder 
    # of the desired directory 
    for x in os.listdir(path): 
        file_metadata = {'title': driveName, "parents": [{"id": "1_NeZVtES6BnUVDZD0YpsgPylAoWb-A1Y"}]}
        f = drive.CreateFile(file_metadata) 
        f.SetContentFile(os.path.join(path, x)) 
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
    path = r"C:\Users\Jake\Documents\CIS540Project\entertainment"
    
    try:
        query_google_trend() 
  
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
