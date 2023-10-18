from bs4 import BeautifulSoup
import requests
import json
from flask import Flask, jsonify

busqueda = "Televisor" #Recuerda de quitarlo y poner un input
url = "https://www.amazon.com/s?k=" + busqueda
headers = {"FUser": "An","user-agent":"an"}
response = requests.get(url,headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')
#--------------------------------NOMBRES PRODUCTOS-----------------------------------------------------------

elemento_nombre = soup.find_all('h2', class_='a-size-mini')

nombre = []

for elemento in elemento_nombre:
    elementos = elemento.find('span', class_='a-text-normal')
    nombre.append(elemento.text.strip())



#------------------------------------LINK DE PRODUCTOS--------------------------------------------------------

elemento_href = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')

href = []

for elemento in elemento_href:

    elementos_productos = elemento.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    
    for i in elementos_productos:
        link_href = i.get('href')
        href.append("https://www.amazon.com" + link_href)

for i in href:
    print(i)

#-------------------------------------------------------------------------------------------------------------

