# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by MudabbirulSaad@Github, < https://github.com/MudabbirulSaad >.
#
# This file is part of < https://github.com/MudabbirulSaad/ScrapLoad > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MudabbirulSaad/ScrapLoad/blob/master/LICENSE >
#
# All rights reserved.

import math
import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

def mkdir(path):
    if not os.path.exists(path):
            os.makedirs(path)
    else:
        pass

def extract_url(list_urls, file_type):
    content_links = []
    for url in list_urls:
        resp = requests.get(url)
        soup = bs(resp.text,'lxml')
        og = soup.find("meta",  property="og:url")
        base = urlparse(url)
        for link in soup.find_all('a'):
            current_link = link.get('href')
            if current_link.endswith(file_type):
                if og:
                    content_links.append(og["content"] + current_link)
                else:
                    content_links.append(base.scheme+"://"+base.netloc + current_link)

                
    return download(content_links)

def download(content_links):
    for link in content_links:
        f_extns = link.split(".")
        f_names = f_extns[-2].split("/")
        f_extn = f_extns[-1]
        f_name = f_names[-1]
        web_name = f_extns[0].replace("https://", "").replace("http://", "")
        web_ext = f_extns[1]
        website = f"{web_name}.{web_ext}".replace(f_name, "")
        try:
            print(f"[+] Website: {website}\n[+] Downloading: {link}\n")
            response = requests.get(link)
            mkdir(website)
            f_path = f"{website}/{f_name}.{f_extn}"
            open(f"{f_path}", "wb").write(response.content)
            f_size = filesize(f_path)
            print(f"[+] Filename: {f_name}\n[+] Type: {f_extn}\n[+] Size: {f_size}\n")
        except requests.exceptions.HTTPError as e:
            return print(f"Error downloading {f_name}.{f_extn}", e)
        

def filesize(path):
    size = os.path.getsize(path)
    return convert_size(size)


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def main():
    input_urls = input("Enter the list of URLs (separated by space) (canbe single URL): ")
    extn = input("Enter the extension name of the file (empty for all avaiable extensions): ")
    list_urls = []
    urls = input_urls.split()
    for url in urls:
        list_urls.append(url)
    extract_url(list_urls, extn)


if __name__ == '__main__':
    main()