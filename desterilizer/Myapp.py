import requests
import json

URL = "http://127.0.0.1:8000/percreate/"

data = {
    'first_name': 'Aashi',
    'last_name': 'Gupta',
    'age': 22
}

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)
