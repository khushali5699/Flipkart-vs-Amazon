from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_url = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=37592845-5d1a-47ad-9691-d1f8050e8c83'       
        
#opening up connection, grabing the page
uClient = uReq(my_url)
page_html = uClient.read()

#html parsing
page_soup = soup(page_html, "html.parser") 
uClient.close()

containers = page_soup.findAll("div",{"class":"_1UoZlX"})

file_name = "products.csv"

headers = "Product_Name, Rating, Ram, display, Camera, Battery, rate, EMI\n"
f = open(file_name,"w",encoding='utf-8')
f.write(headers)

#grabs each product
for container in containers:
    try:
        Product_Name = container.a.find("div",{"class":"_1-2Iqu row"}).div.div.text
        Rating = container.a.find("div",{"class":"hGSR34"}).text
        Ram = container.a.findAll("li",{"class":"tVe95H"})[0].text
        display = container.a.findAll("li",{"class":"tVe95H"})[1].text
        Camera = container.a.findAll("li",{"class":"tVe95H"})[2].text
        Battery = container.a.findAll("li",{"class":"tVe95H"})[3].text
    
    #processor = container.a.findAll("li",{"class":"tVe95H"})[4].text
    #Warrenty = container.a.findAll("li",{"class":"tVe95H"})[5].text
        rate = container.a.find("div",{"class":"_1vC4OE _2rQ-NK"}).text
        price = re.sub('[^0-9]',"",rate)
        EMI = container.a.find("div",{"class":"_2nE8_R"}).text
    
    #detail_1 = container.a.find("div",{"class":"_1-2Iqu row"}).div.li.text
    except:
        pass
        
    f.write(Product_Name.replace(",", "|") + "," + Rating + "," + Ram + "," + display + "," + Camera + "," + Battery + "," + price + "," + EMI + "\n")
    
f.close()


for i in range(2,6):
    my_url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=37592845-5d1a-47ad-9691-d1f8050e8c83&page=" + str(i)       
        
    #opening up connection, grabing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    #html parsing
    page_soup = soup(page_html, "html.parser")
    uClient.close()

    containers = page_soup.findAll("div",{"class":"_1UoZlX"})

    file_name = "products.csv"
    f = open(file_name,"a+",encoding='utf-8')

#grabs each product
    for container in containers:
        try:
            Product_Name = container.a.find("div",{"class":"_1-2Iqu row"}).div.div.text
            Rating = container.a.find("div",{"class":"hGSR34"}).text
            Ram = container.a.findAll("li",{"class":"tVe95H"})[0].text
            display = container.a.findAll("li",{"class":"tVe95H"})[1].text
            Camera = container.a.findAll("li",{"class":"tVe95H"})[2].text
            Battery = container.a.findAll("li",{"class":"tVe95H"})[3].text
        
        #processor = container.a.findAll("li",{"class":"tVe95H"})[4].text
        #Warrenty = container.a.findAll("li",{"class":"tVe95H"})[5].text
            rate = container.a.find("div",{"class":"_1vC4OE _2rQ-NK"}).text
            price = re.sub('[^0-9]',"",rate)
            EMI = container.a.find("div",{"class":"_2nE8_R"}).text
        
        #detail_1 = container.a.find("div",{"class":"_1-2Iqu row"}).div.li.text
        except:
            pass
        f.write(Product_Name.replace(",", "|") + "," + Rating + "," + Ram + "," + display + "," + Camera + "," + Battery + "," + price + "," + EMI + "\n")
        
    f.close()

