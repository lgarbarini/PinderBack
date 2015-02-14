import requests
import os

# os.system("python Pinder.py")

r = requests.get('http://localhost:5000/Index/benji')
print r.content
r = requests.get('http://localhost:5000/GetNextOp/benji')

# print r.content

print "Right swipe " + r.json()['req_id']

op_id = r.json()['req_id']

requests.get('http://localhost:5000/SwipeRight/benji/' + op_id)


r = requests.get('http://localhost:5000/GetNextOp/benji')

# print r.content

print "Right swipe " + r.json()['req_id']

op_id = r.json()['req_id']

requests.get('http://localhost:5000/SwipeRight/benji/' + op_id)


r = requests.get('http://localhost:5000/GetNextOp/benji')

# print r.content

print "Left swipe " + r.json()['req_id']

op_id = r.json()['req_id']

requests.get('http://localhost:5000/SwipeLeft/benji/' + op_id)



r = requests.get('http://localhost:5000/GetMatchList/benji')

mylist = r.json()['list']

for opp in mylist:
	print opp['title']