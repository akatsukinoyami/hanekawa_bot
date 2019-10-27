from config import api_id, api_hash, chaos_id, katsu_id, nyanpasu_id, nyanpasu_un
from pyrogram import Client, MessageHandler, Filters, ChatMember
from service import ru_service, en_service
from time import sleep as sleep
from exchange import Exchange
from words import reacts
import random
import shelve
import re

with shelve.open('DB') as db:
	app = Client("hebushek", api_id, api_hash)
	
	class chat_db:
		def __init__(self, cond=1, lang='ru', mode='nyan', greet=None, 
		nyanc=0, lewdc = 0, angrc = 0, scarc = 0):
			self.cond	= cond
			self.lang	= lang
			self.mode	= mode
			self.greet	= greet
			self.nyanc	= nyanc
			self.lewdc	= lewdc
			self.angrc	= angrc
			self.scarc	= scarc
	
	def replaier(reacts, lang, mode, chat, message, msg):
		for triggers, reaction in reacts[lang][mode].items():
					for trigger in triggers:
						if re.search(r'\b'+trigger, msg):
							a = random.choice(reaction)
							a.reply(message)
							if a.attr == 'nyan':
								chat.nyanc += 1
							elif a.attr == 'lewd':
								chat.lewdc += 1
							elif a.attr == 'angr':
								chat.angrc += 1
							elif a.attr == 'scar':
								chat.scarc += 1

	@app.on_message(~Filters.user(chaos_id) & (Filters.group | Filters.private))
	def nyanpasu(Client, message):
		chat_id = str(message.chat.id)
		if chat_id not in db:
			db[chat_id] = chat_db(cond=1, lang='ru', mode='nyan', greet='Добро Пожаловать', 
			nyanc=0, lewdc = 0, angrc = 0, scarc = 0)

		chat	= db[chat_id]
		cond	= chat.cond
		lang	= chat.lang
		mode	= chat.mode
		greet	= chat.greet
		nyanc	= chat.nyanc
		lewdc	= chat.lewdc
		angrc	= chat.angrc
		scarc	= chat.scarc

		msb = str(message.text)
		msg = msb.lower()
		msgs = msg.split()
		msg_id = int(message.message_id)
		mmbr_id = str(message.from_user.id)
		rp = message.reply
		rnd = random.choice
		service = eval(lang+'_service')
		try:	user = app.get_chat_member(chat_id, mmbr_id)
		except:	user=None
		try:	reply_user_id = str(message.reply_to_message.from_user.id)
		except:	reply_user_id = None
				
		if message.new_chat_members: rp(greet)

		elif '//count' in msb:		
			rp(service['count']+'\n'+
			service['nyanc']+str(nyanc)+'\n'+	
			service['lewdc']+str(lewdc)+'\n'+
			service['angrc']+str(angrc)+'\n'+
			service['scarc']+str(scarc))
		
		elif '//help' in msg:	rp(service['help'])

		elif '//help_exch' in msg:
			url_txt = '<a href="https://www.exchangerate-api.com/docs/supported-currencies"> Поддерживаемые валюты</a>'
			rp(url_txt+'\n'+service['helpe'], disable_web_page_preview=True)
		
		elif '//exch' in msg:
			exch = Exchange()
			if 'add' in msgs[1]:	rp(exch.exchange_add(msgs[2], str(mmbr_id)))
			if 'del' in msgs[1]:	rp(exch.exchange_del(msgs[2], str(mmbr_id)))
			else:					rp(exch.exchange_run(msgs[2], msgs[3], msgs[1], str(mmbr_id)))
		
		elif '..рмх' in msg or '//rmh' in msg or '//rma' in msg:
			k = str(katsu_id)
			h = str(nyanpasu_id)
			if mmbr_id in k or mmbr_id in h:
				n = int(msg.replace('//rma ','').replace('//rmh ','').replace('..рмх', ''))
				for message in app.iter_history(chat_id, 100):
					if message.from_user.id == nyanpasu_id:
						sleep(.1)
						a = message.message_id
						app.delete_messages(chat_id, a)
						n = n - 1
						if n == 0: break
				
		elif message.chat.type == 'supergroup':
			if mmbr_id == str(katsu_id) or user.status is 'administrator' or user.status is 'creator':
				if '//greet' in msg:
					greet_txt = msb.replace('//greet', '')
					chat.greet = greet_txt
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
					modes = ('nyan', 'lewd', 'angr', 'scar')
					if mode_txt in modes:
						chat.mode = mode_txt
						rp(service['ch_mode'])
					else:
						rp(service['er_mode'])

		elif '//greet' in msg or '//chat_on' in msg or '//chat_off' in msg or '//lang' in msg or '//mode' in msg:
			rp(service['perm_er'])
		
		if chat.cond == 1:
			if (reply_user_id == str(nyanpasu_id) or reply_user_id == None):
				replaier(reacts, lang, mode, chat, message, msg)

		elif chat.cond == 0: 
			if (reply_user_id == str(nyanpasu_id) or nyanpasu_un in msg):
				replaier(reacts, lang, mode, chat, message, msg)

		db[chat_id] = chat
		db.sync()
		message.continue_propagation()
	
	app.run()