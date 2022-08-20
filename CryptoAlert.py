# Import libraries
import json
import requests
import telegram_send
import time
import configparser
import asyncio

from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (PeerChannel)

username = '@rzr519'
api_id = 19929208
api_hash = '3124280550900b74945637dfc47f7730'
user_input_channel = 'https://t.me/cryptonotificationbot'

telegram_send.send(messages=["Bot Started!"])


# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

#Change price here
top = 2000
bottom = 1650


client = TelegramClient(username, api_id, api_hash)


@client.on(events.NewMessage(chats=user_input_channel))

async def newMessageListener(event):
	#print("waiting 5 sec")
	#time.sleep(5)
	newMessage = event.message.message

	#print(newMessage)
	if('b' in newMessage):
		print("top updated")
		newMessage = newMessage[1:8]
		print(newMessage)
		loop()

	elif('s' in newMessage):
		print("bottom updated")
		loop()
	else:
		loop()

#if("top" in newMessage):
#		print(newMessage)
#		loop()


def loop():
	#while True:  
		
		# requesting data from url
		data = requests.get(key)  
		data = data.json()

		strprice = json.dumps(f"{data['price']}")
		strprice = str(strprice)
		strprice = strprice[1:8]
		strprice = (float(strprice))
		#print(strprice)
		notifyprice = str(strprice)

		if strprice>=top:
			print("Sending top notification")
			telegram_send.send(messages=[notifyprice + " - ETH Reached the top"])
	
		elif strprice<=bottom:
			print("Sending bottom notification")
			telegram_send.send(messages=[notifyprice + " - ETH Reached the bottom"])
		
		 #oya parana error ekak den run kroth methnin arkata gihilla eke loop wenwa
		time.sleep(10)

with client:
	client.run_until_disconnected()



