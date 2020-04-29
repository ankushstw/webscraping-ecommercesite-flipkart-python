
from urllib2 import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib2
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')

driver.get("https://www.flipkart.com")


content = []
Seller = []
Description = []
Highlights = []
Payment_Option = []
Warranty = []
Available_Offers = []
# Top_Reviews = []
General_specification = []
with open('output.csv','r') as csvf:
	urls = csv.reader(csvf)

	for line in urls:
		rows = line[4]
		content.append(rows)

	for i in (content):
		time.sleep(10)
		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		url = "https://www.flipkart.com{}".format(i)
		driver.get(url)
		
		results = soup.find_all("div" ,attrs={"class":"_3e7xtJ"})

		
		for result in results:
			try:
				Seller.append(result.find("div" , attrs={"class":"_3HGjxn"}).text.strip())
			except AttributeError:
				Seller.append('')

			try:
				Description.append(result.find("div" , attrs={"class":"_3la3Fn _1zZOAc"}).text.strip())
			except AttributeError:
				Description.append('')	

			try:
				Highlights.append(result.find("div",attrs={"class":"_3WHvuP"}).text.strip())
			except AttributeError:
				Highlights.append('')
			try:
				Payment_Option.append(result.find("div" ,attrs={"class":"_1-V7IJ"}).text.strip())
			except AttributeError:
				Payment_Option.append('')
			try:
				Warranty.append(result.find("div" ,attrs={"class":"_3h7IGd"}).text.strip())
			except AttributeError:
				Warranty.append('')
			try:
				Available_Offers.append(result.find("div" ,attrs={"class":"_3D89xM"}).text.strip())
			except AttributeError:
				Available_Offers.append('')
			# try:
			# 	Top_Reviews.append(result.find("div" ,attrs={"class":"qwjRop"}).text.strip())
			# except AttributeError:
			# 	Top_Reviews.append('')
			try:
				General_specification.append(result.find("div",attrs={"class":"_2RngUh"}).text.strip())
			except AttributeError:
				General_specification.append('')					
					
a = {"Seller Name":Seller,"Description":Description ,"Highlights":Highlights,"Payment_Option":Payment_Option,"Warranty":Warranty,"Available_Offers":Available_Offers,"General_specification":General_specification}
df = pd.DataFrame.from_dict(a,)
# print(df)
df.to_csv("o2.csv",index = False,encoding = 'utf-8')

df1 = pd.read_csv('output.csv')
df2 = pd.read_csv('outnew1.csv')

out =pd.concat([df1 ,df2] ,axis = 1)
out.to_csv('outputnew1.csv',index = False,encoding = 'utf-8')
out.to_json('outputnew1.json',orient = "records")