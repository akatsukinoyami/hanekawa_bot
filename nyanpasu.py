from config import api_id, api_hash, chaos_id, katsu_id, hebushek_id
from pyrogram import Client, MessageHandler, Filters
from time import sleep as sleep
from words import reacts
import random
import shelve
import re

app = Client("hebushek", api_id, api_hash)

class chat_db:
	def __init__(self, cond=1, lang='ru', mode='nyan', greet=None, nyan=0):
		self.cond	= cond
		self.lang	= lang
		self.mode	= mode
		self.greet	= greet
		self.nyan	= nyan

@app.on_message(~Filters.user(chaos_id))
def nyanpasu(Client, message):
	msb = str(message.text)
	msg = msb.lower()
	chat_id = str(message.chat.id)
	rp = message.reply
	rnd = random.choice
	FILENAME = "DB"

	with shelve.open(FILENAME) as db:
		print(chat_id)
		if chat_id not in db:
			db[chat_id] = chat_db()
		chat	= db[chat_id]
		lang	= chat.lang
		mode	= chat.mode
		greet	= chat.greet
		nyan	= chat.nyan
		
		for triggers, reaction in reacts[lang][mode].items():
			for trigger in triggers:
				if re.search(r'\b'+trigger, msg):
					rp(rnd(reaction))

	message.continue_propagation()

@app.on_message(Filters.user(katsu_id) | Filters.user(hebushek_id))
def rm(Client, message):
	msb = str(message.text)
	msg = msb.lower()
	chat_id	= message.chat.id
	n = int(msg.replace('//rmh ','').replace('..рмх', ''))

	if '..рмх' in msg or '//rmh' in msg:
		for message in app.iter_history(chat_id, 100):
			if message.from_user.id == hebushek_id:
				sleep(.1)
				a = message.message_id
				app.delete_messages(chat_id, a)
				n = n - 1
				if n == 0: break

app.run()