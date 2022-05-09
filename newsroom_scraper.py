from bs4 import BeautifulSoup
import requests


URL = "https://www.mcgill.ca/newsroom/aggregator/categories/2"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

feed_items = soup.find_all('div', class_='feed-item')

for feed in feed_items:
    title_item = feed.find('h3', class_='feed-item-title')
    title = title_item.find('a').text       # Get the title of the news item
