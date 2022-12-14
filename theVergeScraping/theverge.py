from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

#  Extracting all the information like artcile heading , links , author, date based on articles id 

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

# Extracting all the possibe articles on the web page and calling another function (InfoFinder)

def FindId(soup, ID):
    ids = soup.find_all('div', {'class':'duet--content-cards--content-card'})
    for id in ids:
        ID = ID + 1
        InfoFinder(id, ID)

# Calling Url and Function (FindId)

VergeData = []
ID = 0
url = "https://www.theverge.com/"
driver = webdriver.Firefox()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
FindId(soup, ID)

# writing data to a csv file with a name based on current date

Today = str(date.today())
df = pd.DataFrame(VergeData, columns=['ID', 'Headline', 'Link', 'Author', 'DateTime'])
df.to_csv(Today+'.csv')


