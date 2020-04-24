import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import csv

options = Options()
# options.add_argument("window-size=1400,600")
# from fake_useragent import UserAgent

# ua = UserAgent()
# a = ua.random
# user_agent = ua.random
# print(user_agent)
# options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome('/home/abhay/webscraping/chromedriver')

driver.get('https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=08bbb6d0-adb2-45de-b9fe-04c740bb2a53')

import time

time.sleep(10)

Products = []
Prices = []
review = []
ratings = []
specification=[]
Original_price = []
# EMI = []
percentage = []
Img = []
page=2
while True:
	time.sleep(10)
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	results = soup.find_all("a",href=True, attrs={"class": "_31qSD5"})
	# images = soup.find_all("img",attrs={"class":"_30XEf0"})
	# print(images)
	
	# for image in images:
	# 	img = image['src']
	# 	print(img)
		
	for result in results:
		Products.append(result.find("div", attrs={"class": "_3wU53n"}).text.strip())
		Prices.append(result.find("div", attrs={"class":"_1vC4OE _2rQ-NK"}).text.strip())
		
		try:
			ratings.append(result.find("span",attrs={"class":"_2_KrJI"}).text.strip())
		except AttributeError:
			ratings.append('')
		try:
			review.append(result.find("span",attrs={"class":"_38sUEc"}).text.strip())
		except AttributeError:
			review.append('')
		try:
			Original_price.append(result.find("div",attrs={"class":"_3auQ3N _2GcJzG"}).text.strip())
		except AttributeError:
			Original_price.append('')
		try:
			percentage.append(result.find("div" ,attrs={"class":"VGWI6T"}).text.strip())
		except AttributeError:
			percentage.append('')
		specification.append(result.find("ul",attrs={"class":"vFw0gD"}).text.strip())
		test = result.find("div" ,attrs={"class":"_3BTv9X"}).img['src']
		Img.append(test)
	
	if len(driver.find_elements_by_css_selector("a.next")) >= 0:
		url = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=08bbb6d0-adb2-45de-b9fe-04c740bb2a53&page={}".format(page)
		driver.get(url)
		page += 1
		#It will traverse for only 5 pages as you are after if want more page just comment the below if block
		try:
			if int(page)>23:
				break
		except AttributeError:
			break		
	else:

		break
a = {'image':Img,'Product': Products,'rating':ratings ,'Price': Prices,'Reviews':review,'specification':specification,'Original_prices':Original_price,'percentage':percentage}
df = pd.DataFrame.from_dict(a, )
# print(df)
df.to_csv("/home/abhay/webscraping/output.csv",index=True,encoding='utf-8')
df1 = pd.read_csv('/home/abhay/webscraping/output.csv')
df1.to_json('/home/abhay/webscraping/data.json' ,orient="records")