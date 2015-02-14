from flask import Flask
import redis
import os
import requests
import random
from flask import jsonify
from flask import request


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

	def __init__(self):
		self.left_list = []
		self.right_list = []


	def add_to_left(self, opportunity_id):
		self.left_list.append(opportunity_id)
	def add_to_right(self, opportunity_id):
		self.right_list.append(opportunity_id)

	# Returns true if the user has NOT already seen this opportunity
	def has_not_seen(self, opportunity_id):
		if opportunity_id in self.left_list:
			return False
		elif opportunity_id in self.right_list:
			return False
		else:
			return True

	#Returns a list of the ids of matched opportunities.
	def get_matches_list(self):
		return self.right_list

## A dictionary that maps user_id's to User objects

users_map = {}

def get_user(user_id):
	if user_id in list(users_map):
		return users_map[user_id]
	else:
		users_map[user_id] = User()
		return users_map[user_id]

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
	user = get_user(user_id)
	while (user.has_not_seen(opp)) == 0:
		opp = random.choice(opportunities_list)
	return jsonify(opp)


#POST swipe left

@app.route("/SwipeLeft/<user_id>/<op_id>")
def post_swipe_left(user_id, op_id):
	user = get_user(user_id)
	user.add_to_left(op_id)
	return jsonify('Success')

#POST swipe right

@app.route("/SwipeRight/<user_id>/<op_id>")
def post_swipe_right(user_id, op_id):
	user = get_user(user_id)
	user.add_to_right(op_id)
	return jsonify('Success')

#GET match list

@app.route("/GetMatchList/<user_id>")
def get_match_list(user_id):
	match_list = get_user(user_id).get_matches_list()
	# return str(opp_dict[users_map[user_id].get_matches_list()[0]])
	return_list = []
	for op_id in match_list:
		return_list.append(opp_dict[op_id])
	return_object = {'list': return_list}
	return jsonify(return_object)


#Code I stole off github to allow CORS

def add_cors_headers(response):
	response.headers['Access-Control-Allow-Origin'] = '*'
	return response
app.after_request(add_cors_headers) 

###


app.debug = True

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port)
