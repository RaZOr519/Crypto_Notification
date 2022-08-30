# Import libraries
from telethon.tl.types import (PeerChannel)
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon import TelegramClient, events, sync
from telethon.errors import SessionPasswordNeededError
import json
#from pickle import GLOBAL
#from xxlimited import new
import requests
import telegram_send
import time
import configparser
import asyncio
import os

os.system('cls||clear')


username = input("Enter your username (@name): ")
api_id = input("Enter your api id: ")
api_hash = input("Enter your api hash: ")
user_input_channel = input("Enter your channel link: ")

with open("wc.jpg", "rb") as wc:
	telegram_send.send(images=[wc])
telegram_send.send(messages=["Send desired pair in following format"])

# defining key/request url
ogkey = "https://api.binance.com/api/v3/ticker/price?symbol="


#Change price here
top = 2000
bottom = 1750


print("upper limit is ", top, " down limit is ", bottom)

client = TelegramClient(username, api_id, api_hash)


@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
	newMessage = event.message.message

	if ('buy' in newMessage):
		global top
		print("------------------------------")
		print("top updated with the value ")
		newMessage = newMessage[3:8]
		print(newMessage)
		newMessage = int(newMessage)
		top = newMessage
		print("------------------------------")

		telegram_send.send(messages=["updated"])

		loop()

	elif ('sell' in newMessage):
		global bottom
		print("------------------------------")
		print("bottom updated with the value ")
		newMessage = newMessage[4:9]
		print(newMessage)
		newMessage = int(newMessage)
		bottom = newMessage
		print("------------------------------")

		telegram_send.send(messages=[" updated"])

		loop()
	elif ("Current" in newMessage):
	    currentprice()
	elif ("Config" in newMessage):
	    settings()
	elif ("Coin" in newMessage):
		global key
		telegram_send.send(messages=["Pair Updated"])
		key = ogkey+newMessage[4:12]
		print(key)
	elif ("ClearAll" in newMessage):
		top = 9999999
		bottom = -9999999
		telegram_send.send(
			messages=["All settings got clear! setup again to start the bot"])

	elif ("Exit" in newMessage):
		sys.exit()

	elif ("Ping" in newMessage):
		Ping()
	else:
		loop()


def loop():

  data = requests.get(key)
  data = data.json()
  strprice = json.dumps(f"{data['price']}")
  strprice = str(strprice)
  strprice = strprice[1:8]
  strprice = (float(strprice))
  notifyprice = str(strprice)

  if strprice>=top:
      with open("top.jpg", "rb") as tp:
        telegram_send.send(images=[tp])
        print("Sending top notification", top)
        telegram_send.send(messages=[notifyprice + " - ETH Reached the upper limit"])
  elif strprice<=bottom:
      with open("bottom.jpg", "rb") as bc:
        telegram_send.send(images=[bc])
        print("Sending bottom notification",bottom)
        telegram_send.send(messages=[notifyprice + " - ETH Reached the down limit"])
		
  time.sleep(10)
  os.system('cls||clear') 


def currentprice():

	data = requests.get(key)
	data = data.json()

	strprice = json.dumps(f"{data['price']}")
	strprice = str(strprice)
	strprice = strprice[1:8]
	strprice = (float(strprice))
	notifyprice = str(strprice)

	telegram_send.send(messages=[notifyprice + " is now price"])

	loop()


def settings():

    global top
    global bottom

    top = str(top)
    bottom = str(bottom)
    telegram_send.send(
    	messages=["top is set to " + top+" bottom is set to " + bottom])

    top = int(top)
    bottom = int(bottom)

    loop()


def Ping():
	with open("wc.jpg", "rb") as wc:
		telegram_send.send(images=[wc])
	loop()


with client:
	client.run_until_disconnected()
