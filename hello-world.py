from flask import Flask
import datetime
import json

app = Flask(__name__)

@app.route('/')
def root():
    todays_date = datetime.datetime.now()
    date_in_ISO_format = todays_date.isoformat()
    data = {
        "objetivo": 'Desafio Técnico da SSYS',
        "feito por": "Pedro Henrique Silva Rodrigues",
        "data": f"{date_in_ISO_format}"
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(port=8080)
