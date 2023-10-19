from bs4 import BeautifulSoup
import requests
import json
import csv



busqueda = "telefono" #Recuerda de quitarlo y poner un input
url = "https://www.amazon.com/s?k=" + busqueda # recuerda hacer que recorra varias paginas
headers = {"FUser": "An","user-agent":"an"}
response = requests.get(url,headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')

nombre_clase_producto = 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'
recorre_productos = soup.find_all('div', class_=nombre_clase_producto)



#------------------------------------LINK DE PRODUCTOS--------------------------------------------------------

"""href = []

for elemento in recorre_productos:

    elementos_href = elemento.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    
    for i in elementos_href:
        link_href = i.get('href')
        href.append("https://www.amazon.com" + link_href)

"""
#--------------------------------NOMBRES PRODUCTOS-----------------------------------------------------------

"""nombre = []

for elemento in recorre_productos:
    elementos_nombres = elemento.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    if elementos_nombres:
        nombre.append(elementos_nombres.text.strip())

"""
#-------------------------------------PRECIOS------------------------------------------------------------------------

precio = []

for elemento in recorre_productos:
    elementos_precio = elemento.find('span', class_='a-price-whole')
    elementos_precio_decimal = elemento.find('span', class_='a-price-fraction')
    if elementos_precio and elementos_precio_decimal:
        precio.append(elementos_precio.text.strip() + elementos_precio_decimal.text.strip())

for i in precio:
    print(i)
#------------------------------------exportar data a csv---------------------------------------------------------------

nombre_archivo = "productos.csv"

# Abre el archivo en modo de escritura
with open(nombre_archivo, mode='w', newline='', encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    # Escribe la primera fila con los encabezados
    escritor_csv.writerow(['Nombre', 'Precio', 'Enlace'])

    # Combina las listas y escribe los datos en el archivo CSV
    for n, p, h in zip(nombre, precio, href):
        escritor_csv.writerow([n, p, h])