from flask import Flask
from flask import request
from flask import jsonify
from nlp.nlp import WitHelper
from utils.preferences import Preferences
app = Flask(__name__)

@app.route("/query")
def query():
	query = request.args.get('q')
	preferences = request.args.get('preferences')
	if preferences != None:
		Preferences().loadPreferences(preferences)
	print "Query came as : " + query
	helper = WitHelper()
	nlp = helper.query(query)
	return jsonify({"response" : { "success" : True }})

@app.route("/")
def ping():
	return jsonify({"response" : { "success" : True }})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
