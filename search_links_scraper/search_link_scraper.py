import os
import re
import sys
import glob
from googlesearch import search

class KeyExtractor():

    def __init__(self):

        self.curr_path = os.getcwd() #get current working directory path 
        
    
    def keyword_extraction(self):

        txt_files = glob.glob(os.path.join(self.curr_path, "*.txt")) #find .txt files

        for file in txt_files: #iterate through files

            if 'sports' in file or 'entertainment' in file or 'politics' in file or 'health' in file or 'world' in file: #check file_name

                with open(file, "r") as txt_file: #open file and read file

                    contents =  txt_file.read() #get file contents

                    matched_words = re.findall("‘(.*?)’", contents) #extract words/keywords within quotation marks

                    for keywords in matched_words:
                        
                        self.google_search(keywords, 'en') #pass extracted keywords to google_search function targetting english sites
                        self.google_search(keywords, 'fr') #pass extracted keywords to google_search function targetting french sites
                        self.google_search(keywords, 'spa') #pass extracted keywords to google_search function targetting spanish sites


    def google_search(self, query, lang):

        for link in search(query, tld="co.in", lang=lang, num=10, stop=10, pause=2): #google_search function finds links of top 10
            
            sys.stdout.write(link + '\n')

if __name__ == "__main__":

    find_key = KeyExtractor() #create object for class
    find_key.keyword_extraction() #call keyword extraction function to fetch web links based on fed-in extracted keywords