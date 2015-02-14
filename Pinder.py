from flask import Flask
import redis
import os
import requests
import random
from flask import jsonify


#So this shit runs on heruko
port = int(os.environ.get('PORT', 5000))

app = Flask('Pinder')


##########################
## Loading the Data Set ##

r = requests.get('http://www.peacecorps.gov/api/v1/openings/?page=1')
next_url = r.json()['next']

opportunities_list = r.json()['results']

while next_url != None:
	r = requests.get(next_url)
	opportunities_list += r.json()['results']
	next_url = r.json()['next']

# print r.json()['next']
# for l in opprtunities_list:
# 	print l['title']

# print len(opprtunities_list)


opp_dict = {}
for opp in opportunities_list:
	opp_dict[opp['req_id']] = opp

##########################




class User:

	def __construct__():
		left_list = []
		right_list = []


	def add_to_left(self, opportunity_id):
		left_list.append(opportunity_id)
	def add_to_right(self, opportunity_id):
		right_list.append(opportunity_id)

	# Returns true if the user has NOT already seen this opportunity
	def is_new(self, opportunity_id):
		#return if 
		print ""

	#Returns a list of the ids of matched opportunities.
	def get_matches_list():
		print "I do moar stuffs"

## A dictionary that maps user_id's to User objects

users_map = {}

##

@app.route("/")
def hello():
	return "Hello World!"

#GET the swipey page

@app.route("/Index/<user_id>")
def swipey_page(user_id):
	users_map[user_id] = User()
	return "Hello World!"


#GET next opportunity

@app.route("/GetNextOp/<user_id>")
def get_next_opportunity(user_id):
	# Replace later based off of user preference data....
	opp = random.choice(opportunities_list)
	return jsonify(opp)


#POST swipe left

@app.route("/SwipeLeft/<user_id>/<op_id>")
def post_swipe_left(user_id, op_id):
	user = users_map[user_id]
	user.add_to_left(op_id)

#POST swipe right

@app.route("/SwipeRight/<user_id>/<op_id>")
def post_swipe_right(user_id, op_id):
	user = users_map[user_id]
	user.add_to_right(op_id)

#GET match list

@app.route("/GetMatchList/<user_id>")
def get_match_list(user_id):
	match_list = users_map[user_id].get_match_list()
	return_list = list()
	for op_id in match_list:
		return_list.append(opp_dict[op_id])
	return jsonify(return_list)


app.debug = True

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port)
