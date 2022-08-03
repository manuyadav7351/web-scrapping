from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image
from pytesseract import pytesseract
import os

driver = webdriver.Firefox()
url = 'https://www.amazon.com/errors/validateCaptcha'
driver.get(url)

while url == 'https://www.amazon.com/errors/validateCaptcha':    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # saving image to a folder inside downloads
    images = soup.find('img')
    imageUrl = images['src']
    urllib.request.urlretrieve(imageUrl, "/home/england/Downloads/a/captcha.jpg")
 
    # the image we would be using
    image_path = r"/home/england/Downloads/a/captcha.jpg"
  
    # Opening the image & storing it in an image object
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    inputElement = driver.find_element_by_id("captchacharacters")
    inputElement.send_keys(text)
    input = driver.find_element_by_tag_name('button').click()
    os.remove('/home/england/Downloads/a/captcha.jpg')




