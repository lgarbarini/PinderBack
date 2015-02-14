from flask import Flask

app = Flask('Pinder')


##########################
## Loading the Data Set ##




##########################




@app.route("/")
def hello():
    return "Hello World!"

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
    app.run()