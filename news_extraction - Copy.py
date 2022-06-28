from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd 

website="https://www.indiatoday.in/"
path="chromedriver"

#headless mode-without opening chromepage
options=Options()
options.headless=True

service=Service(executable_path=path)

#for headless mode we have to add options also below
driver=webdriver.Chrome(service=service,options=options)
driver.get(website)

#find elemets when many same elements are there
#otherwise use find_element()
containers=driver.find_elements(by="xpath",value='//div[@class="block block-itg-widget even"]/ul[@class="itg-listing"]/li')

#//h2
#//div[@class="block block-itg-widget even"]//ul[@class="itg-listing"]/li
subtitles=[]
links=[]
#for having inside title and subtext
for container in containers:
   subtitle=container.find_element(by="xpath",value='./a').text
   link=container.find_element(by="xpath",value='./a').get_attribute("href")
   subtitles.append(subtitle)
   links.append(link)

   #print(subtitle)

#//div[@class="block block-itg-widget even"]/ul[@class="itg-listing"]/li/a

#for href //div[@class="block block-itg-widget even"]/ul[@class="itg-listing"]/li/a

my_dict={'subtitle':subtitles,'link':links}
df_headlines=pd.DataFrame(my_dict)
df_headlines.to_csv('headline-headless.csv')
#print(df_headlines.head())

driver.quit()

#for scheduling use crontab