from bs4 import BeautifulSoup
import requests
from csv import writer
import re

with open('../data/experts_list_data.csv', 'w', encoding='utf8', newline='') as f:
    out = writer(f)
    header = ['Name', 'Title', 'Department']
    out.writerow(header)

    for i in range(0, 43):
        url = "https://www.mcgill.ca/newsroom/people/field_mprofile_guide_subjects/Human%20Resources%20/%20Organizational%20Behaviour/field_mprofile_department/Faculty%20of%20Medicine?page=" + \
            str(i)
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        profiles = soup.find_all(
            'div', class_=re.compile('profiles-glossary-entry'))

        for profile in profiles:
            name = profile.find(
                'h2', class_='mcgill-profiles-display-name').text
            title_div = profile.find(
                'div', class_='views-field views-field-field-mprofile-title')
            try:
                title = title_div.find('span', class_='field-content').text
            except:
                title = ''
            department_div = profile.find(
                'div', class_='views-field views-field-field-mprofile-department')
            try:
                department = department_div.find(
                    'span', class_='field-content').text
            except:
                department = ''

            info = [name, title, department]
            out.writerow(info)
