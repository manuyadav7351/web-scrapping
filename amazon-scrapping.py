from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import json


# opening and reading csv file

file = open('Amazon Scraping - Sheet1.csv')
csvreader = csv.reader(file)

#an empty list
finalResult = []
header = next(csvreader)
rows = []

# empty dictionary
dict = {}
driver = webdriver.Firefox()

for row in (csvreader):
    count = int(row[0])  
    asin = row[2]
    country = row[3]
    url = 'https://www.amazon.{}/dp/{}'.format(country,asin)
    url2 = url
    driver.get(url)   
    soup = BeautifulSoup(driver.page_source, 'html.parser')

# checking if URL's working

    if soup.find_all('a', {'href':'/ref=cs_404_logo/'}) or soup.find_all('a', {'href':'/ref=cs_404_logo'}) or soup.find_all('img', {'src':'https://images-eu.ssl-images-amazon.com/images/G/29/x-locale/common/kailey-kitty._CB485935139_.gif'}) or soup.find_all('img', {'src':"https://images-na.ssl-images-amazon.com/images/G/30/x-locale/common/kailey-kitty._CB485935146_.gif"}):
        url = url + " NOT AVAILABLE."
        producttitle = ""
        imageUrl = ""
        productPrice = ""
        productDetails = ""

# if there is cookies to accept

    else:
        try:
            driver.find_element_by_id('sp-cc-accept').click()

            # scrapping product title 
            producttit = soup.find('span', {'id':'productTitle'})
            producttitle = producttit.text.strip()


           # scrapping product image
            if soup.find_all('img', {'id':'landingImage'}):
                images = soup.find_all('img', {'id':'landingImage'})
                for image in images:
                    imageUrl = image['src']
                
            else:
                images = soup.find_all('img', {'class':'frontImage'})
                for image in images:
                    imageUrl = image['src']


            # scrapping product price
           

            if soup.find('span', {'class':'offer-price'}) or soup.find('span', {'class':'priceToPay'}):
                if soup.find('span', {'class':'priceToPay'}):
                    prices = soup.find('span', {'class':'priceToPay'})
                    productPrice = prices.text.strip()
        

                else:
                    prices = soup.find('span', {'class':'offer-price'})
                    productPrice = prices.text.strip()
                     

            elif soup.find('a-size-base a-color-price a-color-price'):
                 price  = soup.find('a-size-base a-color-price a-color-price')
                 productPrice = price.text.strip()
                 

            elif soup.find('span', {'class':'a-text-price'}):
                prices = soup.find('span', {'class':'a-text-price'})
                productPrice = prices.text.strip()
               

            elif soup.find('a', {'class':'a-size-mini a-link-normal'}):
                prices = soup.find('a', {'class':'a-size-mini a-link-normal'})
                productPrice = prices.text.strip()
                
            
            else:
                print("Price Not Available")
            
            # scrapping products details

            try:
                if soup.find('div', {'id':'detailBullets_feature_div'}):
                    details = soup.find('div', {'id':'detailBullets_feature_div'})
                    productDetails = details.text.replace(" ","")

                else:
                    details = soup.find('table', {'id':'productDetails_techSpec_section_1'})
                    productDetails = details.text.replace(" ","")
            
            except:
                continue

            url = url

# without cookies 


        except:
            # scrapping product title
            producttit = soup.find('span', {'id':'productTitle'})
            producttitle = producttit.text.strip()


            # scrapping product image
            if soup.find_all('img', {'id':'landingImage'}):
                images = soup.find_all('img', {'id':'landingImage'})
                for image in images:
                    imageUrl = image['src']
                # productimg = soup.find('img', {'id':'landingImage'})
            
                
            else:
                images = soup.find_all('img', {'class':'frontImage'})
                for image in images:
                    imageUrl = image['src']

            # scrapping product price           


            if soup.find('span', {'class':'offer-price'}) or soup.find('span', {'class':'priceToPay'}):
                if soup.find('span', {'class':'priceToPay'}):
                    prices = soup.find('span', {'class':'priceToPay'})
                    productPrice = prices.text.strip()                    

                else:
                    prices = soup.find('span', {'class':'offer-price'})
                    productPrice = prices.text.strip()                      

            elif soup.find('a', {'class':'a-size-mini a-link-normal'}):
                price  = soup.find('a', {'class':'a-size-mini a-link-normal'})
                productPrice = price.text.strip()                 

            elif soup.find('a-size-base a-color-price a-color-price'):
                price  = soup.find('a-size-base a-color-price a-color-price')
                productPrice = price.text.strip()                 

            elif soup.find('span', {'class':'a-text-price'}):
                prices = soup.find('span', {'class':'a-text-price'})
                productPrice = prices.text.strip()                

            elif soup.find('a', {'class':'a-size-mini a-link-normal'}):
                prices = soup.find('a', {'class':'a-size-mini a-link-normal'})
                productPrice = prices.text.strip()
                
            
            else:
                print("Price Not Available")

            # scrapping product details

            try:
                if soup.find('div', {'id':'detailBullets_feature_div'}):
                    details = soup.find('div', {'id':'detailBullets_feature_div'})
                    productDetails = details.text.replace(" ", "")

                else:
                    details = soup.find('table', {'id':'productDetails_techSpec_section_1'})
                    productDetails = details.text.replace(" ","")
            
            except:
                continue

            url = url
    
    dict[count] = {" URL " : url , " PRODUCT TITLE " : producttitle, " PRICE " : productPrice, " IMAGE URL " : imageUrl, " PRODUCT DETAILS ": productDetails}
    finalResult.append(dict)
    dict = {}
    # limit 100 times iterate
    if count == 100:
        # Dumping data into json file
        json_object = json.dumps(finalResult, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        driver.quit()
    else:
        continue

