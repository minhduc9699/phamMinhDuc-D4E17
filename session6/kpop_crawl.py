import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

web = requests.get('https://dbkpop.com/db/all-k-pop-idols')

web_content = BeautifulSoup(web.text)
table = web_content.find('table', {'id': 'table_1'})

idols = table.find_all('tr')

label_map = {
    0: 'profile',
    1: 'stage_name',
    2: 'full_name',
    3: 'korean_name',
    4: 'k.stage_name',
    9: 'height',
    10: 'weight'
}

for idol in idols:
    idol_info = idol.find_all('td')
    person_data = {}
    for i in range(len(idol_info)):
        if i in label_map:
            a_tag = idol_info[i].find('a')
            if a_tag: # check if idol have profile page
                profile_page = requests.get(a_tag['href'])
                profile_page_content = BeautifulSoup(profile_page.text)
                thumbnail_div = profile_page_content.find('div', {'class': 'post-thumbnail'})
                img_tag = thumbnail_div.find('img')
                person_data['thumbnail'] = img_tag['src']
            key = label_map[i]
            person_data[key] = idol_info[i].text
    print(person_data)
