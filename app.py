from flask import Flask, jsonify
from getCollectionList import getCollection
from query import getResults
from createCollection import createCollection


app = Flask(__name__)

@app.before_request
def before():
    print("This runs before anything!")

@app.route('/collections/')
def getNames():
    return jsonify(getCollection())

@app.route('/query/<string:query>/<string:collection_name>')
def getQuery(query, collection_name):
    result = getResults(query, collection_name)
    return jsonify(result)

@app.route('/create/<string:path>/<string:collection_name>')
def makeCollection(path, collection_name):
    result = createCollection(path, collection_name)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)