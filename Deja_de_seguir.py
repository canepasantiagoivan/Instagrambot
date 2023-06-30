# Import necessary libraries
import random
import datetime
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

username = 'cuenta_aqui'  # Change this to your Instagram username
password = 'cuenta_aqui'  # Change this to your Instagram password
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(4)
username_field = driver.find_element('name', 'username')
password_field = driver.find_element('name', 'password')

username_field.send_keys(username)
password_field.send_keys(password)
login_button = driver.find_element('xpath', "//button[@type='submit']")
login_button.click()
time.sleep(5)

username='melinarrrrdo'
# Navigate to your profile
profile_url = f'https://www.instagram.com/{username}/following'
driver.get(profile_url)
time.sleep(5)

# Navigate to your followers list and load all followers

time.sleep(5)
followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
#followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
scroll_height = 0

# Lee el archivo CSV
data = pd.read_csv('unfollowers.csv')

# Convierte la columna en una lista
no_me_siguen = data['Name'].tolist()

# while True:

#     casillas_grandes = driver.find_elements(By.XPATH,"//div[contains(@class, 'x9f619') and contains(@class, 'xjbqb8w') and contains(@class, 'x78zum5') and contains(@class, 'x168nmei') and contains(@class, 'x13lgxp2') and contains(@class, 'x5pf9jr') and contains(@class, 'xo71vjh') and contains(@class, 'x1pi30zi') and contains(@class, 'x1swvt13') and contains(@class, 'xwib8y2') and contains(@class, 'x1y1aw1k') and contains(@class, 'x1uhb9sk') and contains(@class, 'x1plvlek') and contains(@class, 'xryxfnj') and contains(@class, 'x1c4vz4f') and contains(@class, 'x2lah0s') and contains(@class, 'xdt5ytf') and contains(@class, 'xqjyukv') and contains(@class, 'x1qjc9v5') and contains(@class, 'x1oa3qoh') and contains(@class, 'x1nhvcw1')]")

#     for casilla in casillas_grandes:
#         usuario = casilla.text.split('\n')[0]
#         print(usuario)

#         if usuario in no_me_siguen:
#             print("entra aqui")
#             boton_siguiendo = casilla.find_elements(By.XPATH, ".//div[contains(@class, 'x9f619') and contains (@class, 'x1q0g3np') and contains (@class, 'xqjyukv') and contains (@class, 'x1nhvcw1') and contains (@class, 'x1oa3qoh')]")
#             boton_siguiendo[2].click()
#             time.sleep(5)
#             boton_dejar_de_seguir = driver.find_element(By.XPATH, "//button[contains(@class, '_a9-- _a9-_')]")
#             boton_dejar_de_seguir.click()
#             time.sleep(1)
#             no_me_siguen.remove(usuario)
            
#             time.sleep(random.randint(1, 2))
                
no_me_siguen = data['Name'].tolist()
no_me_siguen_dates = data['Date'].tolist()

# Función para calcular la diferencia de días
def days_passed(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return (datetime.datetime.now() - date_obj).days

while True:

    casillas_grandes = driver.find_elements(By.XPATH,"//div[contains(@class, 'x9f619') and contains(@class, 'xjbqb8w') and contains(@class, 'x78zum5') and contains(@class, 'x168nmei') and contains(@class, 'x13lgxp2') and contains(@class, 'x5pf9jr') and contains(@class, 'xo71vjh') and contains(@class, 'x1pi30zi') and contains(@class, 'x1swvt13') and contains(@class, 'xwib8y2') and contains(@class, 'x1y1aw1k') and contains(@class, 'x1uhb9sk') and contains(@class, 'x1plvlek') and contains(@class, 'xryxfnj') and contains(@class, 'x1c4vz4f') and contains(@class, 'x2lah0s') and contains(@class, 'xdt5ytf') and contains(@class, 'xqjyukv') and contains(@class, 'x1qjc9v5') and contains(@class, 'x1oa3qoh') and contains(@class, 'x1nhvcw1')]")

    for casilla in casillas_grandes:
        usuario = casilla.text.split('\n')[0]
        print(usuario)

        if usuario in no_me_siguen:
            # Encuentra la fecha en la que comenzaste a seguir al usuario
            index = no_me_siguen.index(usuario)
            follow_date = no_me_siguen_dates[index]

            # Verifica si han pasado más de 3 días
            if days_passed(follow_date) > 3:
                print("entra aqui")
                boton_siguiendo = casilla.find_elements(By.XPATH, ".//div[contains(@class, 'x9f619') and contains (@class, 'x1q0g3np') and contains (@class, 'xqjyukv') and contains (@class, 'x1nhvcw1') and contains (@class, 'x1oa3qoh')]")
                boton_siguiendo[2].click()
                time.sleep(5)
                boton_dejar_de_seguir = driver.find_element(By.XPATH, "//button[contains(@class, '_a9-- _a9-_')]")
                boton_dejar_de_seguir.click()
                time.sleep(1)
                no_me_siguen.remove(usuario)
                no_me_siguen_dates.pop(index)

            time.sleep(random.randint(1, 2))

        
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', followers_list)
    time.sleep(1)
    new_scroll_height = driver.execute_script('return arguments[0].scrollHeight;', followers_list)
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height




