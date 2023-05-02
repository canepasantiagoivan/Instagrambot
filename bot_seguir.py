import csv
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import pickle
from name_predictor.model import feature_extractor,vectorizer
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
    "User-Agent": "Mozilla/4.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
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

username = 'xxx1'  # Change this to your Instagram username
password = 'xxx1'  # Change this to your Instagram password
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(4)
username_field = driver.find_element('name', 'username')
password_field = driver.find_element('name', 'password')

username_field.send_keys(username)
password_field.send_keys(password)
login_button = driver.find_element('xpath', "//button[@type='submit']")
login_button.click()
time.sleep(random.randint(5, 7))

#username='so.manenti'
username = 'axelalmaraz77'
# Navigate to your profile
profile_url =f'https://www.instagram.com/{username}/'
driver.get(profile_url)
time.sleep(random.randint(6, 8))
driver.find_element(By.XPATH, '//a[contains(@href, "followers")]').click()

time.sleep(random.randint(4, 6))
followers_list = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
#followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
scroll_height = 0




'''while True:
    
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

'''



# Cargar el modelo desde el archivo
with open('./modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Hacer inferencias con el modelo
def predict_gender(name):
    features = feature_extractor(name.lower())
    X = vectorizer.transform([features])
    prediction = modelo.predict(X)
    return "hombre" if prediction[0] == 1 else "mujer"
# nueva_prediccion = predict_gender('sofia')

def guardar_usuario_csv(usuario):
    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('usuarios.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([usuario, fecha_actual])

def crear_archivo_csv_si_no_existe():
    if not os.path.exists('usuarios.csv'):
        with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Usuario', 'Fecha'])

crear_archivo_csv_si_no_existe()

def usuario_ya_guardado(usuario):
    with open('usuarios.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == usuario:
                return True
    return False    

contador_total = 0
contador_tanda = 0
scrolls = 0


while True:

    scrolls += 1 
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', followers_list)
    time.sleep(random.randint(5, 8))
    new_scroll_height = driver.execute_script('return arguments[0].scrollHeight;', followers_list)
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height
    time.sleep(random.randint(5, 8))

    





casillas_grandes = driver.find_elements(By.XPATH,"//div[contains(@class, 'x9f619') and contains(@class, 'xjbqb8w') and contains(@class, 'x78zum5') and contains(@class, 'x168nmei') and contains(@class, 'x13lgxp2') and contains(@class, 'x5pf9jr') and contains(@class, 'xo71vjh') and contains(@class, 'x1pi30zi') and contains(@class, 'x1swvt13') and contains(@class, 'xwib8y2') and contains(@class, 'x1y1aw1k') and contains(@class, 'x1uhb9sk') and contains(@class, 'x1plvlek') and contains(@class, 'xryxfnj') and contains(@class, 'x1c4vz4f') and contains(@class, 'x2lah0s') and contains(@class, 'xdt5ytf') and contains(@class, 'xqjyukv') and contains(@class, 'x1qjc9v5') and contains(@class, 'x1oa3qoh') and contains(@class, 'x1nhvcw1')]")

for casilla in casillas_grandes:
    if contador_total > 50:
        break

    usuario = casilla.text.split('\n')[0]
    nombre_usuario = casilla.text.split('\n')[1]
    print(nombre_usuario)

    if predict_gender(nombre_usuario) == "mujer":
        print(nombre_usuario, "es mujer")
        try:
            
            #boton_siguiendo = casilla.find_element(By.XPATH, ".//div[contains(@class, 'x9f619') and contains(@class, 'x1q0g3np') and contains (@class, 'xqjyukv') and contains (@class, 'x1nhvcw1') and contains (@class, 'x1oa3qoh')]//button//div[contains(text(), 'Seguir')]")
            boton_siguiendo = casilla.find_elements(By.XPATH, ".//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(., 'Seguir')]")
            print("len(boton_siguiendo)",len(boton_siguiendo) )
            
            # Si el botón "Seguir" está presente, haga clic en él y espere 20 segundos
            if len(boton_siguiendo) > 0 and not usuario_ya_guardado(usuario):
                
                boton_siguiendo[0].click()
                
                time.sleep(random.randint(60, 70))
                contador_total +=1
                guardar_usuario_csv(usuario)

        except NoSuchElementException:
            print("no se encontro el boton")
            # Si el botón "Seguir" no está presente, significa que ya estás siguiendo al usuario
            pass
                      
        time.sleep(random.randint(1, 2))


    

driver.close()


            




