from config import api_id, api_hash, katsu_id, chaos_id, dev_api_pst, usrnm_pst, psswd_pst
from pyrogram import Client, MessageHandler, Filters
from paste_bin import PasteBinApi as pastebin
from googletrans import Translator
from time import sleep as sleep
from exchange import exchange
import youtube_dl
import random

app = Client("katsu", api_id, api_hash)
translator = Translator()
pst_api = pastebin(dev_api_pst)
usr_key = pst_api.user_key(username=usrnm_pst, password=psswd_pst)

@app.on_message(Filters.user("me"))
def buff(Client, message):
	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()
	msbs = msb.split()
	msg_id = message.message_id
	ch_id = message.chat.id
	edit = app.edit_message_text
	translate = translator.translate
	langs = ['en', 'ru', 'ua', 'jp', 'ch']
	try:
		rpl_id = message.reply_to_message.message_id
		reply_user_id = str(message.reply_to_message.from_user.id)
		rp_msg = message.reply_to_message.text
		rep_fst_nm = str(message.reply_to_message.from_user.first_name)
		if 'Хаос' in rep_fst_nm :
			reply_first_name = rep_fst_nm.replace('Хаоса', 'Х@оса')
		else:
			reply_first_name = rep_fst_nm
		usr_name = str(reply_first_name) + ' @' + str(message.reply_to_message.from_user.username)
	except BaseException:
		rpl_id = None
		rp_msg = None
		usr_name = None
		reply_user_id = None

	if '..паст' in msg or '//past' in msg:
		code = str(msb.replace('..паст ', '').replace('//past ', ''))
		link = pst_api.paste(usr_key, raw_code=code, title=None, private=None, api_paste_format='python', expire_date=None)
		edit(ch_id, msg_id, str(link))

	elif '..в' in msg or '//to' in msg:
		msgrp = msb.split()
		trans_from = msb.replace('..в '+msgrp[1]+' ', '').replace('//to '+msgrp[1]+' ', '')
		if msgrp[1] in langs:
			trans_to = translate(trans_from, dest=msgrp[1])
			edit(ch_id, msg_id, trans_to.text)
	
	elif '..рп' in msg or '//rp' in msg or reply_user_id==chaos_id:
		msgrp = msb.split()
		if msgrp[1] in langs:
			trans_to = translate(rp_msg, msgrp[1])
			edit(ch_id, msg_id, usr_name+'__\n\n'+trans_to.text)
		else:
			txt_rp_msg = str(usr_name +'\n__'+ str(rp_msg) +'__\n\n'+ msb)
			edit(ch_id, msg_id, txt_rp_msg.replace("..рп ","").replace('//rp ', ''))

	elif '..кв' in msg or '//ce' in msg:
		txt_exch = exchange(msbs[2], msbs[3], msbs[1])
		edit(ch_id, msg_id, txt_exch)

	elif '..гл' in msg or '//gl' in msg:
		txt1 = str(msg.replace("..гл ","").replace('//gl ',''))
		txt_gl_msg = 'https://google.gik-team.com/?q=' + str(txt1.replace(" ", "+"))
		edit(ch_id, msg_id, txt_gl_msg)

	elif '..ю' in msg or '//yt' in msg:
		txt_ydl_msg = str(msg.replace('..ю ', '').replace('//yt ', ''))
		with youtube_dl.YoutubeDL() as ydl:
			ydl.download([txt_ydl_msg])
		edit(ch_id, msg_id, (txt_ydl_msg + '\nDownloaded'))
	
	elif '..п ' in msg or '//ud' in msg:
		und_txt = '--'+str(msb.replace('..п ', '').replace('//ud ', ''))+'--'
		edit(ch_id, msg_id, und_txt)

	elif '..з' in msg or '//st' in msg:
		stk_txt = '~~'+str(msb.replace('..з ', '').replace('//st ', ''))+'~~'
		edit(ch_id, msg_id, stk_txt)

	elif '..сс' in msg or '//ur' in msg:
		url_msg = msg.replace('..c ', '').replace('//ur ', '').split('\n')
		url_txt = '<a href="'+url_msg[2]+'">'+url_msg[1]+'</a>'
		edit(ch_id, msg_id, url_txt, disable_web_page_preview=True)

	elif '..рмх' in msg or '//rmh' in msg:
		sleep(.050)
		edit(ch_id, msg_id, "Удаляю")
		sleep(1)
		edit(ch_id, msg_id, "Удалено")		
		sleep(2)
		app.delete_messages(ch_id, msg_id)

	elif '..ранд' in msg or '//rand' in msg:
		rand = random.randint(int(msgs[1]), int(msgs[2]))
		edit(ch_id, msg_id, "Рандомизирую между "+str(msgs[1])+" и "+str(msgs[2]))
		sleep(3)
		edit(ch_id, msg_id, 'Результат рандома: '+str(rand))

	elif '..спам' in msg or '//spam' in msg:
		n = int(msgs[1])
		mt = msb.replace('..спам '+str(n), '').replace('//spam '+str(n), '')
		while n != 0:
			app.send_message(ch_id, mt)
			n = n - 1
		app.delete_messages(ch_id,msg_id)
	
	elif '//help_ex' in msg:
		url_txt = '<a href="https://www.exchangerate-api.com/docs/supported-currencies"> Поддерживаемые валюты</a>'
		edit(ch_id, msg_id, url_txt, disable_web_page_preview=True)

	elif '..справка' in msg or '//help_b' in msg: 
		edit(ch_id, msg_id, """**..справка** или **//help_b** - __эта справка__
**//help_ex** - __список поддерживаемых валют__
**..рп** или **//rp** - __для злого реплая сообщения__
**..рп "яз"** или **//rp "lang"** - __перевод реплая__
**..гл** или **//gl** - __погуглить за человека__
**..ю** или **//yt** - __скачать видео на сервер__
**..п** или **//ud** - __подчеркнуть сообщение__
**..з** или **//st** - __зачеркнуть сообщение__
**..сс** или **//ur** - __оформить ссылку__
**..рмх n** или **//rmh n** (где n - число) - __удаляет сообщения бота__
**..рмк n** или **//rmk n** (где n - число) - __удаляет сообщения Кацу__
**..ранд n m** или **//rand n m** - __рандом от n до m__
**..спам n** или **//spam n** - __печатает n сообщений__
**..паст код** или **//past код** - __отправить код в pastebin__ 
**..в "яз"** или **//to "lang"** - __перевод сообщения на английский__
**..кв** или **//ce число валюта-из валюта-в(auto)**
""")

	message.continue_propagation()

@app.on_message(Filters.user(katsu_id))
def rm(Client, message):
	msb = str(message.text)
	msg = msb.lower()
	chat_id	= message.chat.id

	if '..рмк' in msg or '//rmk' in msg:
		n = int(msg.replace('//rmk ','').replace('..рмк', '')) + 1
		for message in app.iter_history(chat_id, 100):
			if message.from_user.id == katsu_id:
				a = message.message_id
				app.delete_messages(chat_id, a)
				sleep(.1)
				n = n - 1
				if n == 0: break

app.run()