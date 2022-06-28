from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd 
from datetime import datetime
import os
import sys

#application_path=os.path.dirname(sys.executable)

now=datetime.now()
month=now.strftime("%d-%m-%Y")
print(month)
curr=datetime.now()

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
#file_name=f'headline-{curr}.csv'

#final_path=os.path.join(application_path,file_name)
df_headlines.to_csv(f'headline_{month}.csv')
#print(df_headlines.head())

driver.quit()

#for scheduling use crontab