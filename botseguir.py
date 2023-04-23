# Import necessary libraries
import random
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Definir headers para no ser bloqueado por IG
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept-Language": "en-US,en;q=0.9",
}

# Add headers to Chrome options
chrome_options = Options()
for header, value in headers.items():
    chrome_options.add_argument(f"--header-{header}={value}")

# Initialize the webdriver with the custom headers
driver = webdriver.Chrome(executable_path="path/to/chromedriver", options=chrome_options)

 
# Define the proxy server 
PROXY = "IpOfTheProxy:PORT" 
 
# Set ChromeOptions() 
chrome_options = webdriver.ChromeOptions() 
 
# Add the proxy as argument 
chrome_options.add_argument("--proxy-server=%s" % PROXY) 

# Your code to interact with the page goes here

# Don't forget to close the driver


# Set up a WebDriver
driver_path = 'path/to/chromedriver.exe'  # Change this to the path of your WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# Log into Instagram

username = 'usuariopropio'  # Usario
password = 'xxxx'  # contraseña
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(4)
username_field = driver.find_element('name', 'username')
password_field = driver.find_element('name', 'password')

username_field.send_keys(username)
password_field.send_keys(password)
login_button = driver.find_element('xpath', "//button[@type='submit']")
login_button.click()
time.sleep(5)

username='usuarioacopiarlista'
# usuario a copiar seguidos
profile_url = f'https://www.instagram.com/{username}/'
driver.get(profile_url)
time.sleep(5)

# Navigate to your followers list and load all followers 

followers_link = driver.find_element('xpath', "//a[@href='/" + username + "/followers/']")
followers_link.click()
time.sleep(5)
followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
#followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]') 
scroll_height = 0


while True:
    
    buttons = driver.find_elements('xpath',"//div[contains(@class, 'x9f619') and contains(@class, 'xjbqb8w') and contains(@class, 'x78zum5') and contains(@class, 'x168nmei') and contains(@class, 'x13lgxp2') and contains(@class, 'x5pf9jr') and contains(@class, 'xo71vjh') and contains(@class, 'x16n37ib') and contains(@class, 'x1uhb9sk') and contains(@class, 'x1plvlek') and contains(@class, 'xryxfnj') and contains(@class, 'xs83m0k') and contains(@class, 'x1c4vz4f') and contains(@class, 'x1q0g3np') and contains(@class, 'xqjyukv') and contains(@class, 'x1qjc9v5') and contains(@class, 'x1oa3qoh') and contains(@class, 'x1nhvcw1')]//button//div[contains(text(), 'Seguir')]")

    for button in buttons:
        #print(button)
        button.click()
        time.sleep(random.randint(60, 70))
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', followers_list)
    time.sleep(1)
    new_scroll_height = driver.execute_script('return arguments[0].scrollHeight;', followers_list)
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height




