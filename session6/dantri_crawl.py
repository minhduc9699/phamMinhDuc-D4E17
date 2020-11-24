import requests
from bs4 import BeautifulSoup

web = requests.get('https://dantri.com.vn/')

content = BeautifulSoup(web.text)

highlight_area = content.find('div', {'class': 'highlight-event'})

title_list = highlight_area.find_all('li')
print(title_list)