# Import necessary libraries
import random
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Define custom headers
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

username = 'xxx'  # Change this to your Instagram username
password = 'xxx'  # Change this to your Instagram password
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(4)
username_field = driver.find_element('name', 'username')
password_field = driver.find_element('name', 'password')

username_field.send_keys(username)
password_field.send_keys(password)
login_button = driver.find_element('xpath', "//button[@type='submit']")
login_button.click()
time.sleep(5)

username_mine='santiagocanepa'

#--------------------------------------------------------------------------------------------------------aca empieza followers
# Navigate to your profile
profile_url = f'https://www.instagram.com/{username_mine}/'
driver.get(profile_url)
time.sleep(5)

# Navigate to your followers list and load all followers
followers_link = driver.find_element('xpath', "//a[@href='/" + username_mine + "/followers/']")
followers_link.click()
time.sleep(5)
followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
#followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
scroll_height = 0


while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', followers_list)
    time.sleep(random.randint(1, 3))
    new_scroll_height = driver.execute_script('return arguments[0].scrollHeight;', followers_list)
    time.sleep(random.randint(1, 3))
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height

# Scrape your followers
followers = []
soup = BeautifulSoup(driver.page_source, 'html.parser')
for li in soup.find_all('div', class_='x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'):
    username = li.text
    followers.append(username)

# Save the data to a CSV file



# ------------------------------------------------------------------------ aca empieza following


driver.get("https://www.instagram.com/" + username_mine + "/following/")
time.sleep(5)


time.sleep(5)
following_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
#followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
scroll_height = 0


while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', following_list)
    time.sleep(1)
    new_scroll_height = driver.execute_script('return arguments[0].scrollHeight;', following_list)
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height

# Scrape your followers
sigues_pero_no_te_siguen = []
soup = BeautifulSoup(driver.page_source, 'html.parser')
for li in soup.find_all('div', class_='x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'):
    username = li.text
    if username not in followers:
        sigues_pero_no_te_siguen.append(username)

# Save the data to a CSV file
df = pd.DataFrame(sigues_pero_no_te_siguen, columns=['Name'])
df.to_csv('unfollowers.csv', index=False)

