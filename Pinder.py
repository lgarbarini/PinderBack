from flask import Flask
import redis
import os
import requests

#So this shit runs on heruko
port = int(os.environ.get('PORT', 5000))

app = Flask('Pinder')


##########################
## Loading the Data Set ##

r = requests.get('http://www.peacecorps.gov/api/v1/openings/?page=1')
next_url = r.json()['next']

opprtunities_list = r.json()['results']

while next_url != None:
	r = requests.get(next_url)
	opportunities_list += r.json()['results']
	next_url = r.json()['next']

# print r.json()['next']
# for l in opprtunities_list:
# 	print l['title']

# print len(opprtunities_list)

##########################




@app.route("/")
def hello():
    return "Hello World!" +"\n"+ str(opportunities_list)

#GET the swipey page

@app.route("/Index")
def swipey_page():
    return "Hello World!"


#GET next opportunity

@app.route("/GetNextOp/<user_id>")
def get_next_opportunity(user_id):
    return "Hello World!"


#POST swipe left

@app.route("/SwipeLeft/<user_id>/<op_id>")
def post_swipe_left(user_id, op_id):
    return "Hello World!"

#POST swipe right

@app.route("/SwipeRight/<user_id>/<op_id>")
def post_swipe_right(user_id, op_id):
    return "Hello World!"

#GET match list

@app.route("/GetMatchList/<user_id>")
def get_match_list(user_id):
    return "Hello World!"


app.debug = True

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port)
