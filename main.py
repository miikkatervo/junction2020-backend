from flask import Flask, request, render_template, json
import collections

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/results', methods=['POST', 'GET'])
def filter():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True)