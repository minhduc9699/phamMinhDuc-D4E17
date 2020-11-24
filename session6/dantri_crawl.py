import requests
from bs4 import BeautifulSoup

web = requests.get('https://dantri.com.vn/')

content = BeautifulSoup(web.text)

highlight_area = content.find('div', {'class': 'highlight-event'})
title_list = highlight_area.find_all('li')

for title in title_list:
    title_a_tag = title.find('a')
    print(title_a_tag.text.strip())
    print(title_a_tag['href'])