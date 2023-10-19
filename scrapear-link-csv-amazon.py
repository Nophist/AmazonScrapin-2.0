import csv
from bs4 import BeautifulSoup
import requests



# Especifica la ruta del archivo CSV
ruta_csv = 'D:\Workspace\Webscraping-Amazon\Productos_amazon.csv'  # Reemplaza 'archivo.csv' con la ruta de tu archivo CSV

# Lista para almacenar las URLs
urls = []

# Abre el archivo CSV en modo lectura
with open(ruta_csv, 'r', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    # Itera a través de las filas del archivo CSV
    for fila in lector_csv:
        # Supongamos que la URL se encuentra en la primera columna (índice 0)
        url = fila[2]
        urls.append(url)

# Ahora, la lista 'urls' contiene todas las URLs desde el archivo CSV
# Puedes iterar sobre esta lista y procesar las URLs según tus necesidades
nombres = []
precio = []
descuento = []

with open("datos_productos.csv", mode="w", newline="", encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Nombre", "Precio", "Descuento", "URL"])


for url in urls:

    headers = {"FUser": "An", "user-agent": "an"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    #---------------------NOMBRES---------------------------------------------------
    elemento_nombre = soup.find('span', id='productTitle').text.strip()
    nombres.append(elemento_nombre)

    #----------------------PRECIO-DESCUENTOS----------------------------------
    elemento_precio = soup.find_all('div', id='corePriceDisplay_desktop_feature_div')

    for i in elemento_precio:
        precio_producto = i.find('span', class_='a-offscreen').text.strip()
        descuento_producto = i.find('span', class_='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage')
        #precio_producto_decimal = i.find('span', class_='a-price-fraction').text.strip()
        if precio_producto:
            precio.append(precio_producto)
        else:
            precio.append("No encontro precio")
        if descuento_producto:
            descuento.append(descuento_producto.text.strip())
        else:
            descuento.append("Sin descuento")

# Crear una lista de datos combinados
datos_combinados = list(zip(nombres, precio, descuento, urls))

# Escribir los datos en un nuevo archivo CSV
with open("datos_productos.csv", mode="w", newline="", encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Nombre", "Precio", "Descuento", "URL"])
    escritor_csv.writerows(datos_combinados)












