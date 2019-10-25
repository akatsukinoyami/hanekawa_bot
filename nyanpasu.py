from config import api_id, api_hash, chaos_id, katsu_id, hebushek_id
from pyrogram import Client, MessageHandler, Filters, ChatMember
from time import sleep as sleep
from words import reacts, ru_service, en_service
import random
import shelve
import re

app = Client("hebushek", api_id, api_hash)

class chat_db:
	def __init__(self, cond=1, lang='ru', mode='nyan', greet=None, nyac=0):
		self.cond	= cond
		self.lang	= lang
		self.mode	= mode
		self.greet	= greet
		self.nyac	= nyac
	def print_chat(self, cond=1, lang='ru', mode='nyan', greet=None, nyac=0):
		print(self.cond, self.lang, self.mode, self.greet, self.nyac)


@app.on_message(~Filters.user(chaos_id))
def nyanpasu(Client, message):
	msb = str(message.text)
	msg = msb.lower()
	chat_id = str(message.chat.id)
	msg_id = int(message.message_id)
	mmbr_id = message.from_user.id
	rp = message.reply
	rnd = random.choice
	for_nyac = ('ня+', 'ня+к', 'nya+', 'мя+у')
	FILENAME = 'DB'
	user = app.get_chat_member(chat_id, mmbr_id)
	adm_coms = ()

	with shelve.open(FILENAME) as db:
		if chat_id not in db:
			db[chat_id] = chat_db(cond=1, lang='ru', mode='nyan', greet=None, nyac=0)
		chat	= db[chat_id]
		cond	= chat.cond
		lang	= chat.lang
		mode	= chat.mode
		greet	= chat.greet
		nyac	= chat.nyac
		
		if lang == 'ru':
			service = ru_service
		elif lang == 'en':
			service = en_service
		if mmbr_id == katsu_id or user.status is 'administrator' or user.status is 'creator':
			if '//greet' in msg:
				greet_txt = msb.replace('//greet', '')
				chat.greet = greet_txt
				print(chat.greet)
				rp(service['rp_greet'])
			if '//cond' in msg:
				msgc = msg.replace('//cond ','')
				if 'on' in msgc:
					chat.cond = 1
					rp(service['rp_on'])
				if 'off' in msgc:
					chat.cond = 0
					rp(service['rp_off'])
			if '//lang' in msg:
				lang_txt = msg.replace('//lang ', '')
				langs = ('ru', 'en')
				if lang_txt in langs:
					chat.lang = lang_txt
					rp(service['ch_lang'])
				else:
					rp(service['er_lang'])
			if '//mode' in msg:
				mode_txt = msg.replace('//mode ', '')
				modes = ('nyan', 'lewd', 'brut', 'scar')
				if mode_txt in modes:
					chat.mode = mode_txt
					rp(service['ch_mode'])
				else:
					rp(service['er_mode'])
		elif '//greet' in msg or '//chat_on' in msg or '//chat_off' in msg or '//lang' in msg or '//mode' in msg:
			rp(service['perm_er'])

		if message.new_chat_members:
			rp(greet)
			print(chat.greet+' for '+message.from_user.first_name)
		if '//count' in msg:
			rp(chat.nyac)
		
		if '//help_h' in msg:
			rp(service['help'])

		for triggers, reaction in reacts[lang][mode].items():
			for trigger in triggers:
				if chat.cond == 1:
					if re.search(r'\b'+trigger, msg):
						rp(rnd(reaction))
				for nyac1 in for_nyac:
					if trigger == nyac1:
						chat.nyac += 1

		db[chat_id] = chat

	message.continue_propagation()

@app.on_message(Filters.user(katsu_id) | Filters.user(hebushek_id))
def rm(Client, message):
	msb = str(message.text)
	msg = msb.lower()
	chat_id	= message.chat.id

	if '..рмх' in msg or '//rmh' in msg:
		n = int(msg.replace('//rmh ','').replace('..рмх', ''))
		for message in app.iter_history(chat_id, 100):
			if message.from_user.id == hebushek_id:
				sleep(.1)
				a = message.message_id
				app.delete_messages(chat_id, a)
				n = n - 1
				if n == 0: break

app.run()