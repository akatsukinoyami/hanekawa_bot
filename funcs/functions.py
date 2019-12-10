from funcs.stats import my_stats, chat_stats, stat
from funcs.exchange import Exchange
from funcs.yout_dl import down_func
from funcs.tts import tts
from config import nyanpasu_id
from subprocess import check_output
from googletrans import Translator
from threading import Thread
import random
import re

translator = Translator()

def functions(app, message, chat, service):
	msg_id = int(message.message_id)
	mmbr = message.from_user
	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()
	rp = message.reply
	chat_id = message.chat.id
	msg_id = int(message.reply_to_message.message_id) if message.reply_to_message else int(message.message_id)
	translates = ('!translate', '!trans', '!tl')
	if mmbr.id != nyanpasu_id:
			
		if '!stats' in msgs[0]:		
			txt = chat_stats(chat, service)
			rp(txt)
		
		elif '!help' in msgs[0]:	
			txt = service['help']
			rp(txt, disable_web_page_preview=True)
		
		elif '!karma' in msgs[0]:
			if message.reply_to_message:
				txt = stat(service, message, chat)
			else:
				txt = my_stats(chat, service, mmbr.id)
			rp(txt)

		elif '!rand' in msgs[0]:
			try:
				rand = random.randint(int(msgs[1]), int(msgs[2]))
				txt = 'Результат рандома между '+str(msgs[1])+' и '+str(msgs[2])+': \n'+str(rand)
			except ValueError:
				txt = ('Неправильные значения.\n Попробуй так:\n!rand 5 10')
			rp(txt)

		elif msgs[0] in translates:
			langs = ['en', 'ru', 'fr', 'de', 'jp', 'ch']
			msgrp = msb.split()
			if msgrp[1] in langs:
				if message.reply_to_message:
					text = (rep_usr_name+'__\n\n'+message.reply_to_message.text)
				else:
					text = msb.replace('!translate '+msgrp[1]+' ', '').replace('!trans '+msgrp[1]+' ', '').replace('!tl '+msgrp[1]+' ', '')
				txt = (translator.translate(text, dest=msgrp[1])).text
			rp(txt, disable_web_page_preview=True)

		elif '!tts ' in msgs[0] and chat.ttsm == 1:
			tts(chat, app, msb, msg_id)
				
		elif '!exch' in msgs[0]:
			if 'help' in msgs[1]:
				url_txt = '<a href="https://www.exchangerate-api.com/docs/supported-currencies"> Поддерживаемые валюты</a>'
				txt = url_txt+'\n'+service['helpe']
			else:
				exch = Exchange()
				if 'add' in msgs[1]:	txt = exch.exchange_add(msgs[2], str(mmbr.id))
				elif 'del' in msgs[1]:	txt = exch.exchange_del(msgs[2], str(mmbr.id))
				else:					txt = exch.exchange_run(msgs[2], msgs[3], msgs[1], str(mmbr.id))
			rp(txt)
		
		elif '!ut' in msgs[0]:
			if 'help' in msgs[1]:
					url_txt = '<a href="https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md"> Поддерживаемые сайты</a>'
					txt = url_txt+'\n'+service['help_youtube']
					rp(txt, disable_web_page_preview=True)
			else:
				if	  'aud' in msgs[1]:	upload = '_audio'
				elif  'vid' in msgs[1]:	upload = '_video'
				elif 'link' in msgs[1]:	upload = 'typing'
				msbs = msb.split()
				res = ('144', '240', '360', '480', '720', '1080', '1440', '2160')
				if msgs[2] in res:
					ut_thr = Thread(target=down_func, 
					args=(msg_id, chat_id, msbs[3], app, upload, service, msbs[2]))
				else:
					ut_thr = Thread(target=down_func, 
					args=(msg_id, chat_id, msbs[2], app, upload, service))
				ut_thr.run()

		elif '!calc' in msgs[0]:
			file = "/home/katsu/Documents/katsu_bots/funcs/RPN"
			expression = bytes(msg.replace('!calc ', ''), 'UTF-8')
			t = check_output(file, input=expression)
			res = str(round(float(str(t).replace("b'",'').replace("\\n'", ' '))))
			txt = msg.replace('!calc ', '') + ' = ' + res
			rp(txt)

		elif '!user' in msgs[0]:
			if 'cond' in msgs[1]:
				if 'on' == msgs[2]:
					chat.users[mmbr.id].cond = 1
					rp(service['user_rp_on'])
				if 'off' == msgs[2]:
					chat.users[mmbr.id].cond = 0
					rp(service['user_rp_off'])	
			elif 'shipper' in msgs[1]:
				if 'on' == msgs[2]:
					chat.users[mmbr.id].ship = 1
					rp(service['user_ship_on'])
				if 'off' == msgs[2]:
					chat.users[mmbr.id].ship = 0
					rp(service['usr_ship_off'])
			elif 'help' in msgs[1]:
				rp(service['help_usr_set'])
					
		elif '!id' in msgs[0]:
			try:
				if 'stick' in msg:
					txt = ('Sticker set: '+message.reply_to_message.sticker.set_name 
					+' '+ message.reply_to_message.sticker.emoji+'\n'+
					'Stiker ID: '+message.reply_to_message.sticker.file_id)
				if 'msg' in msg:
					txt = ('Chat ID: '+str(chat_id)+
					'\nUser ID: '+str(message.reply_to_message.from_user.id)+
					'\nMessage ID: '+str(message.reply_to_message.message_id))
				if 'voice' in msg:
					txt = ('Voice ID: '+message.reply_to_message.voice.file_id)
			except AttributeError:	txt = 'Ошибка нахождения ID'
			app.send_message(chat_id, txt, 
			reply_to_message_id=msg_id, disable_notification=True)	
					
		elif '!admins' in msg:
			admins = ''
			for member in app.iter_chat_members(message.chat.id, filter='administrators'):
				mu = member.user
				if mu.username:		muu = ' - ' + mu.username
				else:				muu = ' - ' + mu.first_name
				if member.title:	mt  = ' - ' + member.title
				else:				mt  = ' '
				if member.status == 'creator':
					admins = (str(member.status + muu +  mt + """
""") + admins)
				else: 
					admins += str(member.status + muu +  mt + """
""")
			rp(admins)
