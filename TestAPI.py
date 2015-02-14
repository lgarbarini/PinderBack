import requests
import os

# os.system("python Pinder.py")

requests.get('http://localhost:5000/Index/benji')

r = requests.get('http://localhost:5000/GetNextOp/benji')


print r.json()['req_id']