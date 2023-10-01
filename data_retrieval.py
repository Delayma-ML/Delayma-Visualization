import os 
import gdown
import subprocess

GB_4_DATASET_URL:str = "https://drive.google.com/file/d/1XXa8bB2lerztO_2CLztryHCiFa-TuOqc/view?usp=sharing"
GB_4_DATASET_PATH:str = "data/4gb_dataset/unprocessed/"

GB_2_DATASET_URL:str = "https://drive.google.com/file/d/11nuxSqWbBCUFaq1HjufTFLjXQUT2oJED/view?usp=sharing"
GB_2_DATASET_PATH:str = "data/2gb_dataset/unprocessed/"

def get_files(url:str, path:str) -> None:
    """Download the files from google drive, if they are not already downloaded
    
    Parameters
    ----------
    url: str
        url of the dataset
    path: str
        Where to store the files
    """

    # check if the files are already downloaded
    if os.path.exists(path):
        print("Files already downloaded")
        return
    
    # download the files
    print("Downloading files")
    gdown.cached_download(url, path, quiet=False, fuzzy=True)
    
    # unzip the files
    print("Unzipping files")
    subprocess.Popen(["unzip", path + "dl", "-d", path]).wait()
    os.remove(path + "dl")
    print("Done")


if __name__ == "__main__":
    get_files(GB_4_DATASET_URL, GB_4_DATASET_PATH)
    get_files(GB_2_DATASET_URL, GB_2_DATASET_PATH)