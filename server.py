from flask import Flask
from flask import request
from nlp.nlp import WitHelper
app = Flask(__name__)

@app.route("/query")
def query():
	query = request.args.get('q')
	helper = WitHelper()
	nlp = helper.query(query)
	return "Logging request"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
