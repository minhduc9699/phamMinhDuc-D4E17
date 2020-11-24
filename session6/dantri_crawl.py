import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
dantri_database = client.get_database('dantri')
highlight_collection = dantri_database.get_collection('highlights')

web = requests.get('https://dantri.com.vn/')

content = BeautifulSoup(web.text)

highlight_area = content.find('div', {'class': 'highlight-event'})
title_list = highlight_area.find_all('li')

for title in title_list:
    title_a_tag = title.find('a')
    data = {
        'title': title_a_tag.text.strip(),
        'link': title_a_tag['href']
    }
    highlight_collection.insert_one(data)
    
