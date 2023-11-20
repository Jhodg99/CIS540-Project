from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
   
# For using listdir() 
import os 
   
  
# Below code does the authentication 
# part of the code 
gauth = GoogleAuth() 
  
# Creates local webserver and auto 
# handles authentication. 
gauth.LocalWebserverAuth()        
drive = GoogleDrive(gauth) 
   
path = os.getcwd() #get current working directory path 
   
# iterating thought all the files/folder 
# of the desired directory 
for x in os.listdir(path): 

    if "bing" in x:

        f = drive.CreateFile({'title': 'Bing Search Results'}) 
        f.SetContentFile(os.path.join(path, x)) 
        f.Upload() 

        # Due to a known bug in pydrive if we  
        # don't empty the variable used to 
        # upload the files to Google Drive the 
        # file stays open in memory and causes a 
        # memory leak, therefore preventing its  
        # deletion 
        f = None
    
    elif "google" in x:

        f = drive.CreateFile({'title': 'Google Search Results'}) 
        f.SetContentFile(os.path.join(path, x)) 
        f.Upload() 

        # Due to a known bug in pydrive if we  
        # don't empty the variable used to 
        # upload the files to Google Drive the 
        # file stays open in memory and causes a 
        # memory leak, therefore preventing its  
        # deletion 
        f = None