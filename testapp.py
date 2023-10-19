from bs4 import BeautifulSoup
import requests
import csv

def extraer_datos_amazon(busqueda):
    url = "https://www.amazon.com/s?k=" + busqueda
    headers = {"FUser": "An", "user-agent": "an"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    nombre_clase_producto = 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'
    recorre_productos = soup.find_all('div', class_=nombre_clase_producto)

    href = []
    nombre = []
    precio = []

    for elemento in recorre_productos:
        # ------------------------LINKS HREF--------------------------------------------------------------------------
        elementos_href = elemento.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        for i in elementos_href:
            link_href = i.get('href')
            href.append("https://www.amazon.com" + link_href)

        # ----------------------NOMBRES--------------------------------------------------------------------------------
        elementos_nombres = elemento.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        if elementos_nombres:
            nombre.append(elementos_nombres.text.strip())
        else:
            precio.append("Nombre no disponible")

        #----------------------------------PRECIOS----------------------------------------------------------------------
        elementos_precio = elemento.find('span', class_='a-price-whole')
        elementos_precio_decimal = elemento.find('span', class_='a-price-fraction')
        if elementos_precio and elementos_precio_decimal:
            precio.append(elementos_precio.text.strip() + elementos_precio_decimal.text.strip())
        else:
            precio.append("Precio no disponible")

    #------------------------------Datos de precio, nombre y href---------------------------------------
    datos = {
        "Nombre": nombre,
        "Precio": precio,
        "Enlace": href
    }
    return datos


busqueda = "telefono"
datos_amazon = extraer_datos_amazon(busqueda)


with open("Productos_amazon.csv", mode="w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Nombre", "Precio", "Enlace"])
    for n, p, h in zip(datos_amazon["Nombre"], datos_amazon["Precio"], datos_amazon["Enlace"]):
        escritor_csv.writerow([n, p, h])