from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
import json

@app.route('/sendReports', methods=['GET', 'POST'])
def sendReports():
    # get typed character from frontend
    if request.json:
        id = int(request.json.get('id'))
        haku_id = int(request.json.get('haku_id'))


        with open("dataset4.json") as f: 
            bd = json.load(f) 
        i = 0
        palautetteva = {}
        loyty = False
        while not loyty:
            l = 0
            if bd[i]["id"] == id:
                loppuselvitykset = bd[i]["loppuselvitys"]
                while not loyty and l != len(loppuselvitykset):
                    if loppuselvitykset[l]["haku_id"] == haku_id:
                        loyty = True
                        palautettava = loppuselvitykset[l]
                        print(loyty)
                    else: 
                        l = l + 1
            i  = i + 1
        

        return jsonify(palautettava), 200

    else:
        return jsonify({"message": "No typed found"}), 200


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Raportti palvelun hieno serveri :)</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)