import requests
import time
import json
import random

APIKEY = "api_key"
DEVICE_DEV_ID = "device_id"

url = "https://apiv2.favoriot.com/v2/streams"

headers = {
    'apikey': APIKEY,
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "postman-token"
}

while True:
    for bil in range(40):
        root = {}
        root["device_developer_id"] = DEVICE_DEV_ID
        data = {}
        bil = random.randint(20, 50)
        data["Temperature"] = bil
        root["data"] = data
        body = json.dumps(root)
        print(body)
        response = requests.request("POST", url, headers=headers, data=body)
        print(response.text)
        print("")
        time.sleep(3)
