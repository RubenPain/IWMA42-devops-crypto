import requests
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {'vs_currency': 'eur'}
    response = requests.get(url, params=params).json()
    return render_template("crypto.html", response=response)


if __name__ == "__main__":
    app.run(debug=False)