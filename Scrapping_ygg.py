from yggtorrentscraper import YggTorrentScraperSelenium
from selenium import webdriver
import undetected_chromedriver as uc
from yggtorrentscraper import set_yggtorrent_tld
import os

set_yggtorrent_tld("wtf")
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
scraper = YggTorrentScraperSelenium(driver_path="chromedriver2.exe")


def get_files_in_directory(folder_path):
    files = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            files.append(file_name)
    return files


def download_torrents():
    if(scraper.login("***", "***")):

        parameters = {
            "name": "1080p",
            "category": "films_&_videos",
            "subcategory": "film",
            "options": {
                "langue": {"francais_(vff/truefrench)"},
                "qualite": {"hdrip_1080_[rip_hd_depuis_bluray]"},
            },
        }    

        file_path = "downloaded_urls.txt"
        with open(file_path, "r") as file:
            existing_urls = [line.strip() for line in file]

        torrents_url = scraper.search(parameters)
        for url in torrents_url:
            try:
                if url not in existing_urls:
                    with open(file_path, "a") as file:
                        file.write(url + "\n")
                    try:
                        scraper.download_from_torrent_url(url)
                    except:
                        print("Could not download torrent : ", url)
                else:
                    print("Torrent already downloaded : ", url)
            except:
                print("Could not download torrent : ", url)
        scraper.logout()

    else:
        print("Login failed")
        


if __name__ == "__main__":
    download_torrents()