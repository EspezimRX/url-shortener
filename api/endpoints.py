from flask import Flask, redirect, request, jsonify
import json


app = Flask(__name__)


added_urls = {

        'id' : 1,
        'original_url' : 'https://www.google.com',
        'shorten_url' : 'http://short.url/1'

    }



@app.route('/', methods=['GET'])
def home():
    return 'oi'


@app.route('/urls', methods=['GET'])
def urls_list():
    return jsonify(added_urls)


@app.route('/urls/<int:id>', methods=['GET'])
def url_redirect(id):
    text = json.loads('original_url')

    return requests.get(text).json()


@app.route('/users/<string:userid>/urls', methods=['POST'])
def new_url():
    data = request.get_json()
    urls.append(data)

    return jsonify(data), 201



if __name__ == '__main__':
    app.run(debug=True)