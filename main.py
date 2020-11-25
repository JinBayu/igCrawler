from selenium import webdriver
from selenium.webdriver.common.by import By
import platform
import os
import time
import json
from config import config
from config import account
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

URL="https://www.instagram.com/"

result=[]
path = os.getcwd()+"/assets/chromedriver/"+platform.system()+"/chromedriver"
driver = webdriver.Chrome(path,options=options)
driver.get(URL)
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys(account.username)
driver.find_element(By.NAME,"password").send_keys(account.password)
driver.find_element(By.CLASS_NAME,"L3NKy").click()
time.sleep(5)
driver.get(URL+config.SUB_URL)
posts=driver.find_elements(By.CLASS_NAME,"v1Nh3")
for post in posts:
    result.append({"href" : post.find_element(By.TAG_NAME,"a").get_attribute("href")})
with open("output.json", "w") as json_file:
    json.dump(result, json_file)
driver.close()