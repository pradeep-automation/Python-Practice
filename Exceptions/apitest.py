import json

import requests
my_dict = {"user":{"first_name":"Test","last_name":"",
"email":"Felicia.Roberts78@hotmail.com","password":"12345678","phone_number":"+91-8285408009","user_type":"User","currency_id":1}}
with open("test.json", "r") as f:
    data = f.read()

resp = requests.post("https://api-staging-builder.engineer.ai/users", json=json.loads(data))
print(resp.json())

