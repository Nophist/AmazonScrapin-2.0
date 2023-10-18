from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/amazon', methods=["GET"])

def amazon():
    busqueda = "Televisor" #Recuerda de quitarlo y poner un input
    url = "https://www.amazon.com/s?k=" + busqueda
    headers = {"FUser": "An","user-agent":"an"}
    response = requests.get(url,headers=headers)

    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')
        #//div[@class="s-main-slot s-result-list s-search-results sg-row"]//a[@class="a-link-normal s-no-outline"]
        #elementos_a = soup.find_all('h2', class_='h3 product-title')
        href= []
        urls = soup.find_all('div', class_='a-link-normal s-no-outline')
        results = []
        for a_tag in urls:
            href = a_tag.get('href')
            text = a_tag.get_text()
            results.append({"text": text, "href": href})

        # Devuelve los resultados como respuesta JSON
        return jsonify({"results": results})

    return jsonify({"Respuesta": "Fallida "})

   

if __name__=="__main__":
    app.run(debug=True,port=5000,host="0.0.0.0")