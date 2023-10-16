from bs4 import BeautifulSoup
import requests

busqueda = "Televisor" #Recuerda de quitarlo y poner un input
url = "https://www.amazon.com/s?k=" + busqueda
headers = {"FUser": "An","user-agent":"an"}
response = requests.get(url,headers=headers)

if response.status_code==200:

    soup = BeautifulSoup(response.content, 'html.parser')

    elementos = soup.find_all('div', class_='sg-col-inner')

    for i in elementos:
        hrefs = i.find_all('a', class_='a-link-normal s-no-outline')
        print(hrefs)