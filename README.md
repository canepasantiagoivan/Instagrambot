## **Bot de Instagram con Python**
<a href="https://imgbb.com/"><img src="https://i.ibb.co/ZHXrBZ6/Ilustraci-n-De-Banner-De-Icono-De-Redes-Sociales-Rosa-En-Estilo-Dibujado-A-Mano-PNG-Im-genes-Predise.png" alt="Ilustraci-n-De-Banner-De-Icono-De-Redes-Sociales-Rosa-En-Estilo-Dibujado-A-Mano-PNG-Im-genes-Predise" border="0"></a>
<p align="center">
  <img src="https://pin.it/7Lbg90t" alt="Logo del Proyecto" width="200">
</p>
Bienvenidos a este repositorio, donde encontrarás scripts para automatizar algunas tareas en Instagram utilizando Python y Selenium.

## 📋 **Contenido del repositorio**
crear_lista_unfollowers.py: Este script se encarga de scrollear y comparar listas de seguidores, creando una lista llamada unfollowers.csv que contiene a aquellos usuarios que han dejado de seguirnos.

**deja_de_seguir.py** : Este script deja de seguir a los usuarios que se encuentren en la lista unfollowers.csv y agrega a estos usuarios a la lista add.csv.

**bot_seguir.py** : Este script segmenta a los usuarios por género y envía solicitudes de seguimiento a todos los usuarios de una lista de seguidores de otro usuario, de una lista de seguidos, o bien de una lista de likes para garantizar la actividad. Cada usuario al que se le envía una solicitud es copiado en add.csv para evitar enviar dos solicitudes al mismo usuario.

**bot_seguir_sin_genero.py** : Este script es una actualización del script anterior que elimina el modelo de segmentación por género para no cargarlo si no se va a utilizar.

## 📚 **Pre-requisitos**
Para poder utilizar estos scripts, es necesario tener instalados los siguientes paquetes en Python:

 **selenium
pandas
beautifulsoup4
pickle
random
csv
datetime**
Además, necesitarás el WebDriver de Chrome, que puedes descargar desde aquí.

💻 Cómo utilizar los scripts
Clona este repositorio en tu local.
bash
Copy code
git clone https://github.com/username/instagram-bot
Actualiza las variables username y password con tu nombre de usuario y contraseña de Instagram en cada script.
python
Copy code
username = 'introducir usuario'  # Cambia esto por tu nombre de usuario de Instagram
password = 'introducir pass'  # Cambia esto por tu contraseña de Instagram
Actualiza la variable driver_path con la ruta al WebDriver de Chrome.
python
Copy code
driver_path = 'path/to/chromedriver.exe'  # Cambia esto por la ruta al WebDriver de Chrome
Ejecuta los scripts en el orden en que desees utilizando Python.
bash
Copy code
python crear_lista_unfollowers.py
python deja_de_seguir.py
python bot_seguir.py
python bot_seguir_sin_genero.py
## ❗ **Nota importante**
Ten en cuenta que utilizar estos scripts de manera abusiva puede resultar en que Instagram bloquee tu cuenta. Se recomienda utilizarlos de manera responsable. Este código se proporciona con fines educativos y no se alienta ni apoya el spam o el abuso en Instagram.

## 🎯 **Contribuir**
Si tienes alguna mejora o corrección, no dudes en hacer un pull request. Asegúrate de probar el código antes de enviarlo.

## 📜 Licencia
**Este proyecto se encuentra bajo la licencia MIT.**
