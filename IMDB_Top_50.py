import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#insert the website url that will be scraped
req = requests.get("https://www.imdb.com/list/ls055386972/")

soup = BeautifulSoup(req.content, "html.parser")
# print(soup.prettify())

movie = [] #list to store name of the movie
release = [] #list to store release date
director = [] #list to store directors
stars = [] #list to store star cast

#find the data and append data in respective list
x1 = soup.find_all("h3", attrs={'class': 'lister-item-header'})
for row in x1:
    a = row.text
    b = a.split("\n")
    movie.append(b[2])
    release.append(b[3])
release[13] = '(2008)'
# print(len(release))
x2 = soup.find_all("p", attrs={'class': 'text-muted text-small'})
for row in x2:
    y = row.text
    y = y.replace("\n","")
    y = y.replace("\t","")
    y = y.replace("    ","")
    z = re.findall('(^D.+|$)', y)
    z1 = z[0].split("|")
    if z1[0] == '':
        continue
    else:
        director.append(z1[0])
    stars.append(z1[1])
# print(stars)

#output the data form of a csv file

output_data = {'Movie Name':movie, 'Intial Release Date':release, 'Director':director, 'Star cast':stars}
Data = pd.DataFrame(output_data)
Data.to_csv('IMDB_Top_50.csv')

