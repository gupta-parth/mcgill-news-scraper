from datetime import date
from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.mcgill.ca/newsroom/channels_item/19'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# Get all the news items on the page
items = soup.find_all(
    'div', class_='channel-item channel_news has-image clear-block')

for item in items:

    # Each news item has its separate content container
    item_content = item.find('div', class_='content-container')
    news_title = item_content.find('a').text
    # The link to the actual news article
    news_link = item_content.find('a')['href']
    news_link = 'https://www.mcgill.ca' + news_link
    date_container = item_content.find(
        'div', class_='multi-date date-container')
    day = date_container.find('span', class_='day').text
    month = date_container.find('span', class_='month').text
    year = date_container.find('span', class_='year').text
    # Construct the date
    publishing_date = str(day+' ' + month + ' ' + year)

    print(news_title)
    # Scraping the metadata by going to the actual news article page
    news_page = requests.get(news_link)
    news_soup = BeautifulSoup(news_page.content, 'html.parser')

    # Metadata tree
    metadata = news_soup.find('div', class_='mcgill-tags')

    # Categories tree
    categories_container = metadata.find('div', class_='categories')
    category_item_list = categories_container.find('ul', class_='links inline')
    all_categories = category_item_list.find_all('a')
    # Categories stored in an array
    categories = [cat.text for cat in all_categories]

    source_site_container = metadata.find(
        'div', class_='field source-site source-inline')
    source_site = source_site_container.find('a').text
    print(source_site)

    print()
    print()
