#Reading an XML

# import required modules
import bs4 as bs
import requests
URL = 'https://www.geeksforgeeks.org/python-list/'

url_link = requests.get(URL)

file = bs.BeautifulSoup(url_link.text, "lxml")

find_table = file.find('table', class_='numpy-table')
rows = find_table.find_all('tr')

for i in rows:
    table_data = i.find_all('td')
    data = [j.text for j in table_data]
    print(data)




#reading an XML File
'''
from bs4 import BeautifulSoup

file = open("test1.xml", "r")
contents = file.read()

soup = BeautifulSoup(contents, 'xml')
titles = soup.find_all('title')

for data in titles:
    print(data.get_text())
'''