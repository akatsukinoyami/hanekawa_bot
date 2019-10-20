from pyrogram import Client, MessageHandler, Filters
from config import api_id, api_hash, katsu_id, chaos_id, dev_api_pst, usrnm_pst, psswd_pst
from paste_bin import PasteBinApi as pastebin
import youtube_dl
from time import sleep as sleep
import random

app = Client("katsu", api_id, api_hash)
pst_api = pastebin(dev_api_pst)
usr_key = pst_api.user_key(username=usrnm_pst, password=psswd_pst)

@app.on_message(Filters.user("me"))
def buff(Client, message):
	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()
	msg_id = message.message_id
	ch_id = message.chat.id
	try:
		rpl_id = message.reply_to_message.message_id
		reply_user_id = str(message.reply_to_message.from_user.id)
		rep_fst_nm = str(message.reply_to_message.from_user.first_name)
		if 'Хаос' in rep_fst_nm :
			reply_first_name = rep_fst_nm.replace('Хаоса', 'Х@оса')
		else:
			reply_first_name = rep_fst_nm
		usr_name = str(reply_first_name) + ' @' + str(message.reply_to_message.from_user.username)
	except BaseException:
		rpl_id = None
		usr_name = None
		reply_user_id = None

	if '..паст' in msg or '//past' in msg:
		code = str(msb.replace('..паст ', '').replace('//past ', ''))
		link = pst_api.paste(usr_key, raw_code=code, title=None, private=None, api_paste_format='python', expire_date=None)
		app.edit_message_text(ch_id, msg_id, str(link))

	elif '..рп' in msg or '//rp' in msg or reply_user_id==chaos_id:
		txt_rp_msg = str(usr_name +'\n__'+ str(message.reply_to_message.text) +'__\n\n'+ msb)
		app.edit_message_text(ch_id, msg_id, txt_rp_msg.replace("..рп ","").replace('//rp ', ''))

	elif '..гл' in msg or '//gl' in msg:
		txt1 = str(msg.replace("..гл ","").replace('//gl ',''))
		txt_gl_msg = 'https://google.gik-team.com/?q=' + str(txt1.replace(" ", "+"))
		app.edit_message_text(ch_id, msg_id, txt_gl_msg)

	elif '..ю' in msg or '//yt' in msg:
		txt_ydl_msg = str(msg.replace('..ю ', '').replace('//yt ', ''))
		with youtube_dl.YoutubeDL() as ydl:
			ydl.download([txt_ydl_msg])
		app.edit_message_text(ch_id, msg_id, (txt_ydl_msg + '\nDownloaded'))
	
	elif '..п ' in msg or '//ud' in msg:
		und_txt = '--'+str(msb.replace('..п ', '').replace('//ud ', ''))+'--'
		app.edit_message_text(ch_id, msg_id, und_txt)

	elif '..з' in msg or '//st' in msg:
		stk_txt = '~~'+str(msb.replace('..з ', '').replace('//st ', ''))+'~~'
		app.edit_message_text(ch_id, msg_id, stk_txt)

	elif '..сс' in msg or '//ur' in msg:
		url_msg = msg.replace('..c ', '').replace('//ur ', '').split('\n')
		url_txt = '<a href="'+url_msg[2]+'">'+url_msg[1]+'</a>'
		app.edit_message_text(ch_id, msg_id, url_txt, disable_web_page_preview=True)

	elif '..рмх' in msg or '//rmh' in msg:
		sleep(.050)
		app.edit_message_text(ch_id, msg_id, "Удаляю")
		sleep(1)
		app.edit_message_text(ch_id, msg_id, "Удалено")		
		sleep(2)
		app.delete_messages(ch_id, msg_id)

	elif '..ранд' in msg or '//rand' in msg:
		rand = random.randint(int(msgs[1]), int(msgs[2]))
		app.edit_message_text(ch_id, msg_id, "Рандомизирую между "+str(msgs[1])+" и "+str(msgs[2]))
		sleep(3)
		app.edit_message_text(ch_id, msg_id, 'Результат рандома: '+str(rand))

	elif '..спам' in msg or '//spam' in msg:
		n = int(msgs[1])
		mt = msb.replace('..спам '+str(n), '').replace('//spam '+str(n), '')
		while n != 0:
			app.send_message(ch_id, mt)
			n = n - 1
		app.delete_messages(ch_id,msg_id)

	elif '..справка' in msg or '//help' in msg:
		help_txt = """**..справка** или **//help** - __эта справка__
**..рп** или **//rp** - __для злого реплая сообщения__
**..гл** или **//gl** - __погуглить за человека__
**..ю** или **//yt** - __скачать видео на сервер__
**..п** или **//ud** - __подчеркнуть сообщение__
**..з** или **//st** - __зачеркнуть сообщение__
**..сс** или **//ur** - __оформить ссылку__
**..рмх n** или **//rmh n** (где n - число) - __удаляет сообщения бота__
**..рмк n** или **//rmk n** (где n - число) - __удаляет сообщения Кацу__
**..ранд n m** или **//rand n m** - __рандом от n до m__
**..спам n** или **//spam n** - __печатает n сообщений__
**..паст код** или **//past код** - __отправить код в pastebin__ """
		app.edit_message_text(ch_id, msg_id, help_txt)

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