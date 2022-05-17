from bs4 import BeautifulSoup
import requests
from csv import writer
import re

url = "https://www.mcgill.ca/newsroom/people/field_mprofile_guide_subjects/Human%20Resources%20/%20Organizational%20Behaviour/field_mprofile_department/Faculty%20of%20Medicine?page=0"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

profiles = soup.find_all('div', class_=re.compile('profiles-glossary-entry'))

for profile in profiles:
    name = profile.find()
