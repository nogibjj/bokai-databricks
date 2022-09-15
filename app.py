from flask import Flask
from dblib.querydb import querydb

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Databricks SQL query interface"


@app.route("/demo")
def demo():
    result = querydb()
    return {"result": result}


@app.route("/<sql_query>")
def query(sql_query):
    result = querydb(sql_query)
    return {"result": result}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
