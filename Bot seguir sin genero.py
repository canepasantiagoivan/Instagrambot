import csv
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import pickle
#from name_predictor.model import feature_extractor,vectorizer
import random
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Define custom headers para evitar ser identificado por IG
headers = {
    "User-Agent": "Mozilla/4.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept-Language": "en-US,en;q=0.9",
}

chrome_options = Options()
for header, value in headers.items():
    chrome_options.add_argument(f"--header-{header}={value}")

# Initialize the webdriver with the custom headers
driver = webdriver.Chrome(executable_path="C:/Users/Sebastian/chromedriver_win32/chromedriver.exe", options=chrome_options)

 
# proxy server 
PROXY = "IpOfTheProxy:PORT" 
 
# Set ChromeOptions() 
chrome_options = webdriver.ChromeOptions() 
 
# Add the proxy as argument 
chrome_options.add_argument("--proxy-server=%s" % PROXY) 

driver_path = 'C:/Users/Sebastian/chromedriver_win32/chromedriver.exe'  # Change this to the path of your WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# Log into Instagram

username = 'usuario aqui'  # Change this to your Instagram username
password = 'pass aqui'  # Change this to your Instagram password
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(4)
username_field = driver.find_element('name', 'username')
password_field = driver.find_element('name', 'password')

username_field.send_keys(username)
password_field.send_keys(password)
login_button = driver.find_element('xpath', "//button[@type='submit']")
login_button.click()
time.sleep(random.randint(5, 7))


username = 'usuario aca a copiar'

time.sleep(random.randint(6, 8))

driver.get("https://www.instagram.com/" + username + "/followers/")
time.sleep(5)


time.sleep(5)
#following_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
followers_list = driver.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
scroll_height = 0





'''
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
'''



# Cargar el modelo desde el archivo, esto es solo si se piensa en seguir personas de un genero determinado de lo contrario es necesario comentar las secciones. 
# Asi como esta, solo seguiria nombre de usuarios que  que prediga como femeninos

#with open('./modelo.pkl', 'rb') as f:
    #modelo = pickle.load(f)

#def predict_gender(name):
#    features = feature_extractor(name.lower())
#    X = vectorizer.transform([features])
#    prediction = modelo.predict(X)
#    return "hombre" if prediction[0] == 1 else "mujer"
# nueva_prediccion = predict_gender('sofia')


# A continuacion el codigo creara un CSV con cada usuario al cual se siga o se le envie solicitud, el mismo codigo leera posteriormete el csv antes de seguir a cada usuario, con el objetivo de no repetir solicitudes
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

contador = 0
contador_total = 0
contador_tanda = 0
scrolls = 0
#from name_predictor.separetor import possible_name


while contador_total<600 :

    casillas_grandes = driver.find_elements(By.XPATH,"//div[contains(@class, 'x9f619') and contains(@class, 'xjbqb8w') and contains(@class, 'x78zum5') and contains(@class, 'x168nmei') and contains(@class, 'x13lgxp2') and contains(@class, 'x5pf9jr') and contains(@class, 'xo71vjh') and contains(@class, 'x1pi30zi') and contains(@class, 'x1swvt13') and contains(@class, 'xwib8y2') and contains(@class, 'x1y1aw1k') and contains(@class, 'x1uhb9sk') and contains(@class, 'x1plvlek') and contains(@class, 'xryxfnj') and contains(@class, 'x1c4vz4f') and contains(@class, 'x2lah0s') and contains(@class, 'xdt5ytf') and contains(@class, 'xqjyukv') and contains(@class, 'x1qjc9v5') and contains(@class, 'x1oa3qoh') and contains(@class, 'x1nhvcw1')]")


    for idx, casilla in enumerate(casillas_grandes):
        contador += 1 
        
        if contador > 10*(contador_tanda+1):
            contador_tanda += 1
            contador = 0
            break
            

        usuario = casilla.text.split('\n')[0]
        nombre_usuario = casilla.text.split('\n')[1]
        print(nombre_usuario.encode("cp1252", errors="replace").decode("cp1252"))

# Ejecutamos la prediccion antes de seguir, nuevamente COMENTAR ESTA LINEA SI NO SE QUIERE SEGMENTAR POR GENERO.
    #    if predict_gender(possible_name(nombre_usuario)) == "mujer":
            # print(possibl_name(nombre_usuario), "es mujer")
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


    scrolls += 1 
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', followers_list)
    time.sleep(random.randint(5, 8))
    new_scroll_height = driver.execute_script('return arguments[0].scrollHeight;', followers_list
    )
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height
    time.sleep(random.randint(5, 8))

    







    

driver.close()
