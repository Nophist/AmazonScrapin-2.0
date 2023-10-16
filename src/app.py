from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/amazon', methods=["GET"])

def amazon():
    busqueda = "Televisor" #Recuerda de quitarlo y poner un input
    url = "https://www.amazon.com/s?k=".format(busqueda)
    headers = {"FUser": "An","user-agent":"an"}
    response = requests.get(url,headers=headers)

    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

    return jsonify({"res": "hola"})

if __name__=="__main__":
    app.run(debug=True,port=5000,host="0.0.0.0")