from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

def InfoFinder(id):
        try:
            headline = id.find("a", {"data-chorus-optimize-field" : "hed"})
            print(headline.text)
        except:
            print("No Headline")

        try:
            artLink = id.find("a", {"data-chorus-optimize-field" : "hed"})
            if 'href' in artLink.attrs:
                print(artLink.attrs['href'])
        except:
            print("No article Link")
        try:
            author = id.find("span" , {'class' : 'c-byline__author-name'})
            print(author.text)
        except:
            print("No author")

        try :
            dateTime = id.find("time" , {'data-ui' : 'timestamp'})
            if 'datetime' in dateTime.attrs:
                print(dateTime.attrs['datetime'])
        except:
            print("No Date")
        print("*********************************************")

def FindId(bs):
    ids = bs.find_all('div', {'class':'c-entry-box--compact'})
    for id in ids:
        if 'data-chorus-optimize-id' in id.attrs:
            prime = id.attrs['data-chorus-optimize-id']
            InfoFinder(id)
    driver.find_element_by_class_name('c-pagination__more').click()


driver = webdriver.Firefox()
url = "https://www.theverge.com/"

#html = urlopen(url)
html = driver.get(url)
#bs = BeautifulSoup(html.read(), 'html.parser')
bs = BeautifulSoup(html, 'html.parser')
FindId(bs)
