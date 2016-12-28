from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/query")
def query():
	query = request.args.get('q')
	return query

if __name__ == "__main__":
    app.run()
