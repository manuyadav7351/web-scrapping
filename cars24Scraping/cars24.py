import requests
from time import sleep
from urllib import response
from urllib.request import urlopen, Request
from selenium import webdriver
from bs4 import BeautifulSoup

def dataScraping(strUrl):
    sleep(1)
    req = Request(
    url=strUrl, 
    headers={'User-Agent': 'Mozilla/5.0'}
    )
    html = urlopen(req)
    sleep(1)
    bs = BeautifulSoup(html, 'html.parser')
    Name = bs.find('h2', {'class':'_2geSF'})
    Model = bs.find('span', {'class':'_18vo2'})
    Price = bs.find('strong', {'class':'_2yYvS Wqfj6'})
    Monthly = bs.find('strong', {'class':'_2yYvS'})
    DownPayment  = bs.find('span',{'class':'qlqyA'})
    Image = bs.find('div',{'class':'_1eV4Q'})
    KM = bs.find('ul', {'class':'_3RaRw'})
    print(Name.text)
    print(Model.text)
    print(Price.text)
    print(Monthly.text)
    print(DownPayment.text)
    print(KM.text)
    print(Image.text)





def links(strUrl):
    sleep(1)
    req = Request(
    url=strUrl, 
    headers={'User-Agent': 'Mozilla/5.0'}
    )
    html = urlopen(req)
    sleep(1)
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.find_all('a', {'class':'_9Ue0B'}, 'href')
    for link in links:
        # print(link.get('href'))
        url = link.get('href')
        dataScraping(url)
    

driver = webdriver.Firefox()
url = "https://www.cars24.com"
driver.get(url)
sleep(5)
btn = driver.find_element_by_class_name('_175lW')
btn.click()
btn = driver.find_element_by_class_name('_1K8Qe')
btn.click()
btn = driver.find_element_by_xpath('//li[@data-title="New Delhi"]')
btn.click()
sleep(5)
strUrl = driver.current_url
links(strUrl)