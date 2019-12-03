from funcs.stats import my_stats, chat_stats, stat
from funcs.RPN import rpn_calc as calc
from funcs.exchange import Exchange
from googletrans import Translator
from funcs.tts import tts
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

	if '!stats' in msg:		
		txt = chat_stats(chat, service)
		rp(txt)
	
	elif '!karma' in msg:
		if message.reply_to_message:
			txt = stat(service, message, chat)
		else:
			txt = my_stats(chat, service, mmbr.id)
		rp(txt)
				
	elif '!help' in msg:	
		if 'exch' in msg:
			url_txt = '<a href="https://www.exchangerate-api.com/docs/supported-currencies"> Поддерживаемые валюты</a>'
			txt = url_txt+'\n'+service['helpe']
		elif 'admin' in msg:
			txt = service['help_admin']
		elif 'config' in msg:
			txt = service['help_usr_set']
		else: 
			txt = service['help']
		rp(txt, disable_web_page_preview=True)

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
			if message.reply_to_message:
				text = (rep_usr_name+'__\n\n'+message.reply_to_message.text)
			else:
				text = msb.replace('!translate '+msgrp[1]+' ', '').replace('!trans '+msgrp[1]+' ', '').replace('!tl '+msgrp[1]+' ', '')
			txt = (translator.translate(text, dest=msgrp[1])).text
		rp(txt)

	elif '!tts ' in msg and chat.ttsm == 1:
		tts(message, chat, app)
			
	elif '!exch' in msg:
		exch = Exchange()
		if 'add' in msgs[1]:	txt = exch.exchange_add(msgs[2], str(mmbr.id))
		if 'del' in msgs[1]:	txt = exch.exchange_del(msgs[2], str(mmbr.id))
		else:					txt = exch.exchange_run(msgs[2], msgs[3], msgs[1], str(mmbr.id))
		rp(txt)

	elif '!calc' in msg:
		rp(msg.replace('!calc ', '') + ' = ' + calc(msg.replace('!calc ', '')))
	
	elif '!config' in msg:
		if 'cond' in msgs[1]:
			if 'on' == msgs[2]:
				chat.users[mmbr.id].cond = 1
				rp(service['user_rp_on'])
			if 'off' == msgs[2]:
				chat.users[mmbr.id].cond = 0
				rp(service['user_rp_off'])	
		elif 'shipper' in msg:
			if 'on' == msgs[2]:
				chat.users[mmbr.id].ship = 1
				rp(service['user_ship_on'])
			if 'off' == msgs[2]:
				chat.users[mmbr.id].ship = 0
				rp(service['usr_ship_off'])
	elif '!id' in msg:
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
