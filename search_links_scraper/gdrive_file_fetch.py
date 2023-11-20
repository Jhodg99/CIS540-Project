import gdown

# Based Folder URLS for scraped topics
entertainment_folder_url = "https://drive.google.com/drive/folders/1_NeZVtES6BnUVDZD0YpsgPylAoWb-A1Y"
health_folder_url = "https://drive.google.com/drive/folders/1XWcZ6Hji2d1kMI57SleuKRBBA-Ia71x4"
politics_folder_url = "https://drive.google.com/drive/folders/1ONnvQTuXi5MsS-gX6S4eqOzxDKtlLdhD"
sports_folder_url = "https://drive.google.com/drive/folders/1ZUXN6xwX-890rkPVqDNnlHQHLz6nL8So"
twitter_folder_url = "https://drive.google.com/drive/folders/1_-nIQobagdwVCv88ehtoWx8gKsedJ02C"
world_folder_url = "https://drive.google.com/drive/folders/1GnxGg8tmtADMZZSIv3HxI4ZhpUKucISX"


# Download files from based on folder ids
gdown.download_folder(entertainment_folder_url)
gdown.download_folder(health_folder_url)
gdown.download_folder(politics_folder_url)
gdown.download_folder(sports_folder_url)
gdown.download_folder(twitter_folder_url)
gdown.download_folder(world_folder_url)





