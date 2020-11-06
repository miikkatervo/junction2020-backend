from flask import Flask, request, render_template, json
import collections
import json 

app = Flask(__name__, template_folder='templates', static_folder='static')
filename = "dump.json"
with open(filename) as f: 
    data = json.load(f) 

"""@app.route('/')
def main():
    return render_template('index.html', data = data)"""
@app.route('/')
def main():
    return data


@app.route('/results', methods=['POST', 'GET'])
def filter():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True)