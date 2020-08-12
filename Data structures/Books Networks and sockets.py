from urllib.request import urlopen
from bs4 import BeautifulSoup # filter library

url = input('Enter - ')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html').read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

for i in range(count):
    link = tags[position].get('tags',None)
    print(tags[position].contents[0])
    html = urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html').read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    
