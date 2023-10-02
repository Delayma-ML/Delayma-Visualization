import os 
import gdown
import subprocess

UNPROCESSED_URL:str = "https://drive.google.com/drive/u/0/folders/1yrEpkupqJtN-Pdg5D8cd3n893WbfsQgi"
PROCESSED_URL:str = "https://drive.google.com/drive/u/0/folders/173sLVBjS-9rqEjMZB-9PK3yKBZ0-w_as"

UNPROCESSED_PATH:str = "data/"
PROCESSED_PATH:str = "data/"

if __name__ == "__main__":
    gdown.download_folder(url=UNPROCESSED_URL, output=UNPROCESSED_PATH, quiet=False)
    gdown.download_folder(url=PROCESSED_URL, output=PROCESSED_PATH, quiet=False)
