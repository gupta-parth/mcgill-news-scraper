from bs4 import BeautifulSoup
import requests


URL = "https://www.mcgill.ca/newsroom/aggregator/categories/2"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

feed_items = soup.find_all('div', class_='feed-item')

for feed in feed_items:
    title_item = feed.find('h3', class_='feed-item-title')
    # Get the title of the news item
    news_title = title_item.find('a').text

    # Get the news item content and clean it a bit
    news_content = feed.find(
        'div', class_='feed-item-body').text.replace('\n', '')

    # Get the news date
    news_date = feed.find('span', class_='feed-item-date').text
