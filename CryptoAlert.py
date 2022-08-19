# Import libraries
import json
import requests
from pushbullet import PushBullet
import time

access_token = "o.WcF8xk6hjc2hLJvLPkgPdwB0ZsgLb6ET"
pb = PushBullet(access_token)


# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
push =pb.push_note("CryptoBot","Bot Started")
#Change price here
top = 2000
bottom = 1700

while True:  
	# requesting data from url
	data = requests.get(key)  
	data = data.json()

	strprice = json.dumps(f"{data['price']}")
	strprice = str(strprice)
	strprice = strprice[1:8]
	strprice = (float(strprice))
	print(strprice)

	if strprice>=top:
		print("Sending top notification")
		push =pb.push_note("CryptoBot","Reached Top")
	
	elif strprice<=bottom:
		print("Sending bottom notification")
		push =pb.push_note("CryptoBot","Reached Bottom")
	time.sleep(30)
