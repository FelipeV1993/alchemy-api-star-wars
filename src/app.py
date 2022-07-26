from flask import Flask, jsonify, request

app = Flask(__name__)
# Todo mi codigo debe estar de aqui hacia abajo
app.config["DEBUG"] = True
app.config["ENV"] = "development"


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def root():
    print("Hola Mundo")
    return """<h1>Hola Mundo</h1><p>Este es mi parrafo</p>"""

@app.route('/api/contact', methods=['GET'])
def contact():
    return "Accediendo a la ruta contact"

@app.route('/api/about/<name>', methods=['POST', 'PUT']) # request
def about(name):

    if request.method == 'POST': # verificar si estamos llegando por el metodo POST

        msg = {
            "method": request.method,
            "status": "success",
            "code": 200,
            "name": name
        }

        return jsonify(msg)

    if request.method == 'PUT': # verificar si estamos llegando por el metodo PUT
        msg = {
            "method": request.method,
            "status": "success",
            "code": 200,
            "name": name
        }

        return jsonify(msg) # response


@app.route('/api/save-data', methods=['POST'])
def save_data():

    data = request.get_json()

    data = {
        "data": request.json.get('data'),
       # "persona": request.json.get('persona')
       "persona": data["persona"]
    }

    return jsonify(data)


# Todo mi codigo debe estar de aqui hacia arriba
if __name__ == '__main__':
    """ app.run(debug=True, port=3000, host="0.0.0.0") """
    app.run()