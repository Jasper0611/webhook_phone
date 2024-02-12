import requests
import json

webhook_url='https://webhook.site/13e092e1-fd2f-43c8-a252-1b5d53bd843a'
data= {'data':'Name',
       'age':'24'}
headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
        }
res= requests.post(webhook_url, data=json.dumps(data), headers=headers)
