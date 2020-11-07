# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/sendReports', methods=['GET', 'POST'])
def sendReports():
    # get typed character from frontend
    if request.json:
        id = request.json.get('id')
        

        return jsonify(result), 200

    else:
        return jsonify({"message": "No typed found"}), 200


@app.route('/sendTypedReports', methods=['GET', 'POST'])
def sendReports():
    # get typed character from frontend
    if request.json:
        typed = request.json.get('typed')
        typedLowercase = "\'{}%%\'".format(typed.lower())
        typedUppercase = "\'{}%%\'".format(typed.upper())

        result = "joo"
        

        return jsonify(result), 200

    else:
        return jsonify({"message": "No typed found"}), 200

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Raportti palvelun hieno serveri :)</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)