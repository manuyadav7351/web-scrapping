from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import date
import pandas as pd

def InfoFinder(id, ID):
        Id = ID
        try:
            headline = id.find("a", {"class" : "group-hover:shadow-underline-franklin"}) or id.find("div", {"class" : "inline pr-4 font-medium"})
            Headline = headline.text
        except:
            Headline = "No Headline"

        try:
            artLink = id.find("a", {"class" : "group-hover:shadow-underline-franklin"}) or id.find("svg", {"class" : "ml-8 transition fill-gray-63 hover:fill-white"})
            if 'href' in artLink.attrs:
                Link = artLink.attrs['href']
            elif 'xmlns' in artLink.attrs:
                Link = artLink.attrs['xmlns']
        except:
            Link = "No article Link"
        try:
            author = id.find("a" , {'class' : 'text-franklin hover:shadow-underline-inherit mr-8'}) or id.find("a", {"class" : "pr-4 font-bold hover:shadow-underline-inherit"})
            Author = author.text
        except:
            Author = "No author"

        try :
            try:
                spans = id.select('span[class="flex flex-wrap pt-4 font-polysans text-11 tracking-15 leading-140 text-gray-bd uppercase"] > span')
                DateTime = spans[1].text
            except:
                spans = id.select('div[class="flex flex-row flex-wrap items-center mb-[3px] font-polysans text-12 tracking-15 leading-140 text-gray-ef uppercase"] > span')
                DateTime = spans[0].text           
        except:
            DateTime = "No Date"
        
        data = [Id, Headline, Link, Author, DateTime]
        VergeData.append(data)

def FindId(soup, ID):
    ids = soup.find_all('div', {'class':'duet--content-cards--content-card'})
    for id in ids:
        ID = ID + 1
        # if 'data-chorus-optimize-id' in id.attrs:
        #     prime = id.attrs['data-chorus-optimize-id']
        InfoFinder(id, ID)

#driver.find_element_by_class_name('c-pagination__more').click()
VergeData = []
ID = 0
url = "https://www.theverge.com/"
driver = webdriver.Firefox()
#html = urlopen(url)
driver.get(url)
html = driver.page_source
#bs = BeautifulSoup(html.read(), 'html.parser')
soup = BeautifulSoup(html, 'html.parser')
FindId(soup, ID)

# Creating a csv file

Today = str(date.today())

df = pd.DataFrame(VergeData, columns=['ID', 'Headline', 'Link', 'Author', 'DateTime'])
df.to_csv(Today+'.csv')

# f = open(Today+".csv", "wb")
# csv_writer = csv.writer(f)
# for i in VergeData:
#     csv_writer.writerow(i.encode())
# f.close()

# with open(Today+".csv", 'wb') as file:
#     writer = csv.writer(file)
#     for row in VergeData:
#         writer.writerow(row)
#     file.close()
