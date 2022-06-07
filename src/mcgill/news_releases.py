from bs4 import BeautifulSoup
import requests
from csv import writer
import re


with open('../data/news_releases_data.csv', 'w', encoding='utf8', newline='') as f:
    # CSV writer stuff init
    out = writer(f)
    header = ['Title', 'Date', 'Content', 'Categories', 'Source Site', 'Tags']
    out.writerow(header)

    for i in range(0, 218):
        url = 'https://www.mcgill.ca/newsroom/channels_item/19?page=' + str(i)
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        # Get all the news items on the page
        items = soup.find_all(
            'div', class_=re.compile('channel_news'))       # Have to use some regex because the class names aren't consistent

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

            # Scraping the metadata and actual content by going to the actual news article page
            news_page = requests.get(news_link)
            news_soup = BeautifulSoup(news_page.content, 'html.parser')

            print(i)
            print(news_title)

            # Scraping the content
            news_content_obj = news_soup.find(
                'div', class_='content channels channel-item channel_news')
            all_content = news_content_obj.get_text().replace('\n', ' ').strip()

            # Metadata tree
            metadata = news_soup.find('div', class_='mcgill-tags')
            # Categories scraping
            try:
                categories_container = metadata.find(
                    'div', class_='categories')
                category_item_list = categories_container.find(
                    'ul', class_='links inline')
                all_categories = category_item_list.find_all('a')
                # Storing the categories in an array
                categories = [cat.text for cat in all_categories]
            except:
                categories = []

            # Source site scraping
            source_site_container = metadata.find(
                'div', class_='field source-site source-inline')
            source_site = source_site_container.find('a').text

            # Tags scraping
            tags_container = metadata.find(
                'div', class_='field terms terms-inline')
            all_tags = tags_container.find_all('a')
            tags = [tag.text for tag in all_tags]

            # Write to the CSV file
            info = [news_title, publishing_date,
                    all_content, categories, source_site, tags]
            out.writerow(info)
