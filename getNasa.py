import requests
import re
from bs4 import BeautifulSoup
import wget
import os

base_url = "https://apod.nasa.gov/apod/"
url = base_url + "archivepixFull.html"
dir = "img/"


def process_img_page(url):
    img_page = requests.get(url)
    img_soup = BeautifulSoup(img_page.text, 'html.parser')
    try:
        img_soup = img_soup.find('img')
        img_url = base_url + img_soup['src']
        destination = os.path.join(dir, strip_img_name(img_soup['src']))
        wget.download(img_url, out=destination)
        #download_img(img_url,strip_img_name(img_soup['src']))
        #download_img(img_url,img_soup['src'])
    except(TypeError, KeyError) as e:
        return
    
#def download_img(url, name):


def strip_img_name(src):
    name = src.replace('image/','')
    result = re.match(r"\d+/",name)
    name = name.replace(result.group(0), '')
    print(name)
    return name



page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
soup = soup.find_all('b')[1]
tags = soup.find_all('a')



for tag in tags:
    new_url = base_url + tag['href']
    process_img_page(new_url)
    
'''
process_img_page("https://apod.nasa.gov/apod/ap200909.html")
'''