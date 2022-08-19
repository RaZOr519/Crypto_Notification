# Import libraries
import json
import requests
from notify_run import Notify 
import time

notify = Notify(endpoint="https://notify.run/F3j3dAWumnS1SCYURuXu")

# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
notify.send('Bot Running Successfully')

#Change price here
print("Enter top value")
top = int(input())
print("Enter bottom value")
bottom = int(input())

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
		notify.send('Reached Top')
	elif strprice<=bottom:
		print("Sending bottom notification")
		notify.send('Reached Bottom')
	time.sleep(30)