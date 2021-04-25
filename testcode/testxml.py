#Reading an XML
# import required modules
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Reading XML out of HTML from website
#'''
URL = 'https://www.geeksforgeeks.org/python-list/'
url_link = requests.get(URL)
soup = BeautifulSoup(url_link.text, "lxml")
for my_tabels in soup.find_all('table', class_='numpy-table'):
    for heads in my_tabels.find_all('tr'):
        table_data = heads.find_all('td')
        data = [j.text for j in table_data]
        print(data)
#'''
#reading an XML File
'''
df = pd.DataFrame(columns=['Title','Year', 'Price'])
file = open("test1.xml", "r")
contents = file.read()
soup = BeautifulSoup(contents, 'xml')
for books in soup.find_all('book'):
    for titles in books.find_all('title'):
        book_name = titles.text
    for all_years in books.find_all('year'):
        year_created = all_years.text
    for price in books.find_all('price'):
        b_price = price.text
    df = df.append({'Title' : book_name, 'Year' : year_created, 'Price' : b_price}, ignore_index=True)
print(df)
'''
