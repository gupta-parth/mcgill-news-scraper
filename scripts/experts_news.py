from bs4 import BeautifulSoup
import requests
from csv import writer
import re

url = 'https://www.mcgill.ca/newsroom/channels_item/20?page=0'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
