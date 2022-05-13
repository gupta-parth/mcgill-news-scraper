from bs4 import BeautifulSoup
import requests
from csv import writer


with open('data/campus_news_data.csv', 'w', encoding='utf8', newline='') as f:
    # CSV writer init
    out = writer(f)
    header = ['Title', 'Summary', 'Date']
    out.writerow(header)

    # There are currently 8 pages in the newsroom
    for i in range(0, 9):
        url = "https://www.mcgill.ca/newsroom/aggregator/categories/2?page=" + \
            str(i)
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        feed_items = soup.find_all('div', class_='feed-item')

        for feed in feed_items:
            title_item = feed.find('h3', class_='feed-item-title')
            # Get the title of the news item
            news_title = title_item.find('a').text

            # Get the news item content and clean it a bit
            news_summary = feed.find(
                'div', class_='feed-item-body').text.replace('\n', '').strip()

            # Get the news date
            news_date = feed.find('span', class_='feed-item-date').text

            info = [news_title, news_summary, news_date]
            out.writerow(info)
