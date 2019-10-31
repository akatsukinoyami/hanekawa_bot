from config import api_id, api_hash, chaos_id, katsu_id, nyanpasu_id, nyanpasu_un
from pyrogram import Client, MessageHandler, Filters, ChatMember
from service import ru_service, en_service
from googletrans import Translator
from time import sleep as sleep
from exchange import Exchange
from mood import mood_func
from words import reacts
from gtts import gTTS
import random
import shelve
import time
import re

with shelve.open('DB') as db:
	app = Client("hebushek", api_id, api_hash)
	translator = Translator()
	
	class chat_db:
		def __init__(self, cond=0, nsfw=0, lang='ru', mood='nyan', ttsm = 0, greet=None, 
		nyanc=[], lewdc = [], angrc = [], scarc = []):
			self.cond	= cond
			self.nsfw	= nsfw
			self.lang	= lang
			self.mood	= mood
			self.ttsm	= ttsm
			self.greet	= greet
			self.nyanc	= nyanc
			self.lewdc	= lewdc
			self.angrc	= angrc
			self.scarc	= scarc
	
	def replaier(reacts, lang, mood, chat, message, msg):
		for triggers, reaction in reacts[lang][mood].items():
					for trigger in triggers:
						if re.search(r'\b'+trigger, msg):
							a = random.choice(reaction)
							a.reply(message)
							now = round(time.time())
							if a.attr == 'nyan':
								chat.nyanc.append(now)
							elif a.attr == 'lewd':
								chat.lewdc.append(now)
							elif a.attr == 'angr':
								chat.angrc.append(now)
							elif a.attr == 'scar':
								chat.scarc.append(now)

	@app.on_message(~Filters.user(chaos_id) & (Filters.group | Filters.private))
	def nyanpasu(Client, message):
		chat_id = str(message.chat.id)
		if chat_id not in db:
			db[chat_id] = chat_db(cond=0, nsfw=0, lang='ru', mood='nyan', ttsm = 0, greet='Добро Пожаловать', 
			nyanc=[], lewdc = [], angrc = [], scarc = [])

		chat	= db[chat_id]
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
		service = eval(chat.lang+'_service')
		try:	user = app.get_chat_member(chat_id, mmbr_id)
		except:	user=None
		try:	reply_user_id = str(message.reply_to_message.from_user.id)
		except:	reply_user_id = None
		try:
			rpl_id = message.reply_to_message.message_id
			reply_user_id = str(message.reply_to_message.from_user.id)
			rp_msg = message.reply_to_message.text
			rep_fst_nm = str(message.reply_to_message.from_user.first_name)
			if 'Хаос' in rep_fst_nm :
				reply_first_name = rep_fst_nm.replace('Хаоса', 'Х@оса')
			else:
				reply_first_name = rep_fst_nm
			usr_name = '@' + str(message.reply_to_message.from_user.username)
		except BaseException:
			rpl_id = None
			rp_msg = None
			usr_name = None
			reply_user_id = None
		
		chat.mood = mood_func(chat)
		
		if message.new_chat_members: rp(chat.greet)

		elif '//' in msg:
			if '//stats' in msb:
				if		int(chat.cond) == 1:	cc = '✅'
				elif	int(chat.cond) == 0: 	cc = '❌'
				if		int(chat.ttsm) == 1: 	ct = '✅'
				elif	int(chat.ttsm) == 0: 	ct = '❌'
				if 		int(chat.nsfw) == 1: 	cn = '✅'
				elif	int(chat.nsfw) == 0: 	cn = '❌'
				if 		str(chat.lang) == 'ru': cl = '🇷🇺'
				elif 	str(chat.lang) == 'en':	cl = '🇺🇸'

				rp(service['count']+'\n'+
				service['cond']+cc+'\n'+
				service['ttsm']+ct+'\n'+
				service['nsfw']+cn+'\n'+
				service['lang']+cl+'\n'+
				service['mood']+str(chat.mood)+'\n'+
				service['nyanc']+str(len(nyanc))+'\n'+	
				service['lewdc']+str(len(lewdc))+'\n'+
				service['angrc']+str(len(angrc))+'\n'+
				service['scarc']+str(len(scarc)))
			
			elif '//debug' in msg:
				murk = str(chat.nyanc)+'\n'+str(chat.lewdc)+'\n'+str(chat.angrc)+'\n'+str(chat.scarc)
				rp(murk)
			
			elif '//rand' in msg:
				rand = random.randint(int(msgs[1]), int(msgs[2]))
				rp('Результат рандома между '+str(msgs[1])+' и '+str(msgs[2])+': \n'+str(rand))

			elif '//translate' in msg or '//trans' in msg or '//tl' in msg:
				langs = ['en', 'ru', 'fr', 'de', 'jp', 'ch']
				msgrp = msb.split()
				if msgrp[1] in langs:
					if rp_msg:
						txt = (usr_name+'__\n\n'+rp_msg)
					else:
						txt = msb.replace('//translate '+msgrp[1]+' ', '').replace('//trans '+msgrp[1]+' ', '').replace('//tl '+msgrp[1]+' ', '')
					trans_to = translator.translate(txt, dest=msgrp[1])
					rp(trans_to.text)

			elif '//tts ' in msg and chat.ttsm == 1:
				langs = ['en', 'ru', 'fr', 'de', 'jp', 'ch']
				if str(msgs[1]) in langs:	
					lang = str(msgs[1])
					txt = msb.replace('//tts '+str(msgs[1]), '')
				else: 
					lang = chat.lang
					txt = msb.replace('//tts ', '')			
				try:
					tts = gTTS(text=txt, lang=lang)
					tts.save('nya.mp3')
					app.send_voice(chat_id, 'nya.mp3', reply_to_message_id=msg_id)
				except ValueError:
					rp('Ошибка распознавания текста.')
		
			elif '//help' in msg:	
				if 'exch' in msg:
					url_txt = '<a href="https://www.exchangerate-api.com/docs/supported-currencies"> Поддерживаемые валюты</a>'
					txt = url_txt+'\n'+service['helpe']
				elif 'admin' in msg:
					txt = service['help_admin']
				else: 
					txt = service['help']
				rp(txt, disable_web_page_preview=True)	
				
			elif '//exch' in msg:
				exch = Exchange()
				if 'add' in msgs[1]:	rp(exch.exchange_add(msgs[2], str(mmbr_id)))
				if 'del' in msgs[1]:	rp(exch.exchange_del(msgs[2], str(mmbr_id)))
				else:					rp(exch.exchange_run(msgs[2], msgs[3], msgs[1], str(mmbr_id)))
		
			elif '..рмх' in msg or '//rmh' in msg or '//rma' in msg:
				k = str(katsu_id)
				n = str(nyanpasu_id)
				if mmbr_id in k or mmbr_id in n:
					n = int(msg.replace('//rma ','').replace('//rmh ','').replace('..рмх', ''))
					for message in app.iter_history(chat_id, 100):
						if message.from_user.id == nyanpasu_id:
							sleep(.1)
							a = message.message_id
							app.delete_messages(chat_id, a)
							n = n - 1
							if n == 0: break
				
			elif message.chat.type == 'supergroup':
				if (mmbr_id == str(katsu_id) or mmbr_id == str(nyanpasu_id) or
				user.status is 'administrator' or user.status is 'creator'):
					if '//greet' in msg:
						greet_txt = msb.replace(msgs[0]+' ', '')
						chat.greet = greet_txt
						rp(service['rp_greet'])
					elif '//cond' in msg:
						if 'on' == msgs[1]:
							chat.cond = 1
							rp(service['rp_on'])
						if 'off' == msgs[1]:
							chat.cond = 0
							rp(service['rp_off'])
					elif '//nsfw' in msg:
						if 'on' in msgs[1]:
							chat.nsfw = 1
							rp(service['nsfw_on'])
						if 'off' in msgs[1]:
							chat.nsfw = 0
							rp(service['nsfw_off'])
					elif '//lang' in msg:
						langs = ('ru', 'en')
						if msgs[1] in langs:
							chat.lang = msgs[1]
							rp(service['ch_lang'])
						else:
							rp(service['er_lang'])
					elif '//ttsm' in msg:
						if 'on' in msgs[1]:
							chat.ttsm = 1
							rp(service['tts_on'])
						if 'off' in msgs[1]:
							chat.ttsm = 0
							rp(service['tts_off'])
					elif '//mood' in msg:
						moods = ('nyan', 'lewd', 'angr', 'scar')
						if msgs[1] in moods:
							chat.mood = msgs[1]
							rp(service['ch_mood'])
						else:
							rp(service['er_mood'])
					elif '//set_zero' in msg:
						chat.nyanc = []
						chat.lewdc = []
						chat.angrc = []
						chat.scarc = []
						rp('Счетчики обнулены.')

				elif ('//greet' in msg 
				or '//chat_on' in msg 
				or '//chat_off' in msg 
				or '//lang' in msg 
				or '//mood' in msg 
				or '//set_zero' in msg):
					rp(service['perm_er'])
		
		elif chat.cond == 1:
			if (reply_user_id == str(nyanpasu_id) or reply_user_id == None):
				replaier(reacts, chat.lang, chat.mood, chat, message, msg)

		elif chat.cond == 0: 
			if (reply_user_id == str(nyanpasu_id) or nyanpasu_un in msg or '&' in msg):
				replaier(reacts, chat.lang, chat.mood, chat, message, msg)

		db[chat_id] = chat
		db.sync()
		message.continue_propagation()
	
	app.run()