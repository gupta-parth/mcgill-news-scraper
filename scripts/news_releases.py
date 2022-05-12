from datetime import date
from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.mcgill.ca/newsroom/channels_item/19'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
items = soup.find_all(
    'div', class_='channel-item channel_news has-image clear-block')
for item in items:
    item_content = item.find('div', class_='content-container')
    news_title = item_content.find('a').text
    news_link = item_content.find('a')['href']
    date_container = item_content.find(
        'div', class_='multi-date date-container')
    day = date_container.find('span', class_='day').text
    month = date_container.find('span', class_='month').text
    year = date_container.find('span', class_='year').text
    publishing_date = str(day+' ' + month + ' ' + year)
