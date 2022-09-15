from flask import Flask
from dblib.querydb import querydb

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Databricks SQL query interface"


@app.route('/demo')
def demo():
    result = querydb()
    return {"result": result}


@app.route('/<query>')
def query(query):
    result = querydb(query)
    return {"result": result}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)