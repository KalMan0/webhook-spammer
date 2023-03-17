import requests
import json
from time import sleep

webhook_url = 'enter url here'
message = "enter message here"
Ammount_of_msg = 5 #change the amount of messages you wish to send 

payload= {
    'content': message
}

data = json.dumps(payload)

def main ():
    for i in range(Ammount_of_msg):
        response = requests.post(webhook_url, data=data, headers={'Content-Type': 'application/json'})
        sleep(0.7)
        if response.status_code == 204:
            print(f'Message sent')
        else:
            print('Error:', response.status_code)

if __name__ == "__main__": 
    main ()
