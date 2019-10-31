from config import api_id, api_hash, chaos_id, katsu_id, nyanpasu_id, nyanpasu_un
from pyrogram import Client, MessageHandler, Filters, ChatMember
from googletrans import Translator
from time import sleep as sleep
import random
import shelve
import time

from words.service import lang_service
from funcs.chat_db import ChatDB as chat_db
from funcs.chat_db import User
from funcs.exchange import Exchange
from funcs.replaier import replaier
from funcs.mood import mood_func
from funcs.stats import stats
from funcs.tts import tts

with shelve.open('DB') as db:
	app = Client("hebushek", api_id, api_hash)
	translator = Translator()

	@app.on_message(~Filters.user(chaos_id) & (Filters.group | Filters.private))
	def nyanpasu(Client, message):
		k = str(katsu_id)
		n = str(nyanpasu_id)
		chat_id = str(message.chat.id)
		msg_id = int(message.message_id)
		mmbr_id = str(message.from_user.id)

		if chat_id not in db:
			db[chat_id] = chat_db()
		
		chat	= db[chat_id]

		if mmbr_id not in chat.users:
			chat.users[mmbr_id] = User()
		
		user	= chat.users[mmbr_id]
		nyanc	= chat.nyanc
		lewdc	= chat.lewdc
		angrc	= chat.angrc
		scarc	= chat.scarc

		msb = str(message.text)
		msg = msb.lower()
		msgs = msg.split()

		rp = message.reply
		rnd = random.choice

		service = lang_service(chat)

		try:	user = app.get_chat_member(chat_id, mmbr_id)
		except:	user=None
		try:	reply_user_id = str(message.reply_to_message.from_user.id)
		except:	reply_user_id = None
		try:
			rpl_id = message.reply_to_message.message_id
			rp_msg = message.reply_to_message.text
			rep_fst_nm = str(message.reply_to_message.from_user.first_name)
			if 'Хаос' in rep_fst_nm :	reply_first_name = rep_fst_nm.replace('Хаоса', 'Х@оса')
			else:						reply_first_name = rep_fst_nm
			usr_name = '@' + str(message.reply_to_message.from_user.username)
		except BaseException:
			rpl_id = None
			rp_msg = None
			usr_name = None
		
		chat.mood = mood_func(chat)

		if message.new_chat_members and chat.greetc == 1: rp(chat.greet)

		elif reply_user_id:
			rep(message, chat, reply_user_id, service)

		elif '!' in msg:
			if '!stats' in msb:		
				txt = stats(chat, service, n)
				rp(txt)
			
			elif '!mystat' in msg:
				txt = 'Твоя репутация:\n'+str(chat.users[mmbr_id].karma)
				rp(txt)
			
			elif '!help' in msg:	
				if 'exch' in msg:
					url_txt = '<a href="https://www.exchangerate-api.com/docs/supported-currencies"> Поддерживаемые валюты</a>'
					txt = url_txt+'\n'+service['helpe']
				elif 'admin' in msg:
					txt = service['help_admin']
				else: 
					txt = service['help']
				rp(txt, disable_web_page_preview=True)
#			elif '!debug' in msg:
			elif '!rand' in msg:
				try:
					rand = random.randint(int(msgs[1]), int(msgs[2]))
					txt = 'Результат рандома между '+str(msgs[1])+' и '+str(msgs[2])+': \n'+str(rand)
				except ValueError:
					txt = ('Неправильные значения.\n Попробуй так:\n!rand 5 10')
				rp(txt)

			elif '!translate' in msg or '!trans' in msg or '!tl' in msg:
				langs = ['en', 'ru', 'fr', 'de', 'jp', 'ch']
				msgrp = msb.split()
				if msgrp[1] in langs:
					if rp_msg:
						text = (usr_name+'__\n\n'+rp_msg)
					else:
						text = msb.replace('!translate '+msgrp[1]+' ', '').replace('!trans '+msgrp[1]+' ', '').replace('!tl '+msgrp[1]+' ', '')
					txt = (translator.translate(text, dest=msgrp[1])).text
					rp(txt)

			elif '!tts ' in msg and chat.ttsm == 1:
				tts(message, chat, app)
			
			elif '!exch' in msg:
				exch = Exchange()
				if 'add' in msgs[1]:	txt = exch.exchange_add(msgs[2], str(mmbr_id))
				if 'del' in msgs[1]:	txt = exch.exchange_del(msgs[2], str(mmbr_id))
				else:					txt = exch.exchange_run(msgs[2], msgs[3], msgs[1], str(mmbr_id))
				rp(txt)
		
			elif message.chat.type == 'supergroup':
				if (mmbr_id == k or mmbr_id == n or
				user.status is 'administrator' or user.status is 'creator'):
					if '!greet' in msg:
						if msgs[1] == 'on':
							chat.greetc = 1
							txt = service['greet_on']
						elif msgs[1] == 'off':
							chat.greetc = 0
							txt = service['greet_off']
						else:
							greet_txt = msb.replace(msgs[0]+' ', '')
							chat.greet = greet_txt
							txt = service['rp_greet']					
					elif '!cond' in msg:
						if 'on' == msgs[1]:
							chat.cond = 1
							txt = service['rp_on']
						if 'off' == msgs[1]:
							chat.cond = 0
							txt = service['rp_off']
					elif '!nsfw' in msg:
						if 'on' in msgs[1]:
							chat.nsfw = 1
							txt = service['nsfw_on']
						if 'off' in msgs[1]:
							chat.nsfw = 0
							txt = service['nsfw_off']
					elif '!ttsm' in msg:
						if 'on' in msgs[1]:
							chat.ttsm = 1
							txt = service['tts_on']
						if 'off' in msgs[1]:
							chat.ttsm = 0
							txt = service['tts_off']
					elif '!lang' in msg:
						langs = ('ru', 'en')
						if msgs[1] in langs:
							chat.lang = msgs[1]
							txt = service['ch_lang']
						else:
							txt = service['er_lang']
					elif '!mood' in msg:
						moods = ('nyan', 'lewd', 'angr', 'scar')
						if msgs[1] in moods:
							chat.mood = msgs[1]
							txt = service['ch_mood']
						else:
							txt = service['er_mood']
					elif '!set_zero' in msg:
						chat.nyanc = []
						chat.lewdc = []
						chat.angrc = []
						chat.scarc = []
						txt = service['zero']
				elif ('!greet' in msg 
				or '!cond' in msg 
				or '!nsfw' in msg
				or '!ttsm' in msg  
				or '!lang' in msg 
				or '!mood' in msg 
				or '!set_zero' in msg):
					txt = service['perm_er']
				rp(txt)
		
		elif ('!rma ' in msg or '!rmh ' in msg or '!рмх' in msg or '!рма' in msg) and (
			mmbr_id == k or mmbr_id == n):
					n = int(msg.replace('!rma ','').replace('!rmh ','').replace('!рмх', '').replace('!рма', ''))
					for message in app.iter_history(chat_id, 100):
						if message.from_user.id == nyanpasu_id:
							sleep(.1)
							app.delete_messages(chat_id, message.message_id)
							n = n - 1
							if n == 0: break
		
		elif chat.cond == 1:
			if (reply_user_id == n or reply_user_id == None):
				replaier(chat.lang, chat.mood, chat, message, msg)

		elif chat.cond == 0:
			if (reply_user_id == n or nyanpasu_un in msg or '&' in msg):
				replaier(chat.lang, chat.mood, chat, message, msg)

		db[chat_id] = chat
		db.sync()
	
	app.run()