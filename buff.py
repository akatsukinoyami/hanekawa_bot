from config import api_id, api_hash, katsu_id, nyanpasu_id, chaos_id, dev_api_pst, usrnm_pst, psswd_pst
from pyrogram import Client, MessageHandler, Filters
from funcs.paste_bin import PasteBinApi as pastebin
from funcs.delete import edit_buff_nyan, del_katsu
from googletrans import Translator
from time import sleep as sleep
import youtube_dl
import random

app = Client("katsu", api_id, api_hash)
translator = Translator()
pst_api = pastebin(dev_api_pst)
usr_key = pst_api.user_key(username=usrnm_pst, password=psswd_pst)

@app.on_message(Filters.user("me") & (Filters.group | Filters.private))
def buff(Client, message):
	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()
	msbs = msb.split()
	msg_id = message.message_id
	chat_id = message.chat.id
	edit = app.edit_message_text

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
	
	if '!' in msg:
		if '!id' in msg:
			try:
				if 'stick' in msg:
					txt = ('Sticker set: '+message.reply_to_message.sticker.set_name +' '+ message.reply_to_message.sticker.emoji+'\n'+
					'Stiker ID: '+message.reply_to_message.sticker.file_id)
				if 'msg' in msg:
					txt = ('Chat ID: '+str(chat_id)+'\nUser ID: '+reply_user_id+'\nMessage ID: '+str(rpl_id))
				if 'voice' in msg:
					txt = ('Voice ID: '+message.reply_to_message.voice.file_id)
			except AttributeError:	txt = 'Ошибка нахождения ID'
			edit(chat_id, msg_id, txt)

		elif '!to' in msg:
			langs = ['en', 'ru', 'fr', 'de', 'jp', 'ch']
			msgrp = msb.split()
			trans_from = msb.replace('!в '+msgrp[1]+' ', '').replace('!to '+msgrp[1]+' ', '')
			if msgrp[1] in langs:
				trans_to = translator.translate(trans_from, dest=msgrp[1])
				edit(chat_id, msg_id, trans_to.text)
	
		elif '!rp' in msg or reply_user_id==chaos_id:
			langs = ['en', 'ru', 'ua', 'jp', 'ch']
			msgrp = msb.split()
			if msgrp[1] in langs:
				trans_to = translator.translate(rp_msg, msgrp[1])
				edit(chat_id, msg_id, usr_name+'__\n\n'+trans_to.text)
			else:
				txt_rp_msg = str(usr_name +'\n__'+ str(rp_msg) +'__\n\n'+ msb)
				edit(chat_id, msg_id, txt_rp_msg.replace("!рп ","").replace('!rp ', ''))

		elif '!debug' in msg:
			print(message)

		elif '!sticker' in msg:
			app.delete_messages(chat_id, msg_id)
			app.send_sticker(chat_id, msbs[1])
		
		elif '!паст' in msg or '!past' in msg:
			code = str(msb.replace('!паст ', '').replace('!past ', ''))
			link = pst_api.paste(usr_key, raw_code=code, title=None, private=None, api_paste_format='python', expire_date=None)
			edit(chat_id, msg_id, str(link))

		elif '!ранд' in msg or '!rand' in msg:
			rand = random.randint(int(msgs[1]), int(msgs[2]))
			edit(chat_id, msg_id, "Рандомизирую между "+str(msgs[1])+" и "+str(msgs[2]))
			sleep(3)
			edit(chat_id, msg_id, 'Результат рандома между '+msgs[1]+' и '+msgs[2]+': '+str(rand))

		elif '!спам' in msg or '!spam' in msg:
			app.delete_messages(chat_id,msg_id)
			n = int(msgs[1])
			mt = msb.replace('!спам '+str(n), '').replace('!spam '+str(n), '')
			while n != 0:
				app.send_message(chat_id, mt, reply_to_message_id=rpl_id)
				n = n - 1
				sleep(.2)

		elif '!гл' in msg or '!gl' in msg:
			txt1 = str(msb.replace("!гл ","").replace('!gl ',''))
			txt_gl_msg = '<a href=\"https:\\google.gik-team.com/?q='+str(txt1.replace(" ", "+"))+'\">'+txt1+'</a>'
			edit(chat_id, msg_id, txt_gl_msg, disable_web_page_preview=True)

		elif '!ю' in msg or '!yt' in msg:
			txt_ydl_msg = str(msg.replace('!ю ', '').replace('!yt ', ''))
			with youtube_dl.YoutubeDL() as ydl:
				ydl.download([txt_ydl_msg])
			edit(chat_id, msg_id, (txt_ydl_msg + '\nDownloaded'))

		elif '!п ' in msg or '!ud' in msg:
			und_txt = '--'+str(msb.replace('!п ', '').replace('!ud ', ''))+'--'
			edit(chat_id, msg_id, und_txt)

		elif '!з' in msg or '!st ' in msg:	
			stk_txt = '~~'+str(msb.replace('!з ', '').replace('!st ', ''))+'~~'
			edit(chat_id, msg_id, stk_txt)

		elif '!сс' in msg or '!ur' in msg:
			url_msg = msg.replace('!c ', '').replace('!ur ', '').split('\n')
			url_txt = '<a href="'+url_msg[2]+'">'+url_msg[1]+'</a>'
			edit(chat_id, msg_id, url_txt, disable_web_page_preview=True)

		elif '!справка' in msg or '!helpk' in msg: 
			edit(chat_id, msg_id, """**!справка** или **!help_k** - __эта справка__
**!рп** или **!rp** - __для злого реплая сообщения__
**!рп "яз"** или **!rp "lang"** - __перевод реплая__
**!гл** или **!gl** - __погуглить за человека__
**!ю** или **!yt** - __скачать видео на сервер__
**!п** или **!ud** - __подчеркнуть сообщение__
**!з** или **!st** - __зачеркнуть сообщение__
**!сс** или **!ur** - __оформить ссылку__
**!рмх n** или **!rmh n** (где n - число) - __удаляет сообщения бота__
**!рмк n** или **!rmk n** (где n - число) - __удаляет сообщения Кацу__
**!rma** - __удаляет сообщения Кацу и бота__
**!спам n** или **!spam n** - __печатает n сообщений__
**!паст код** или **!past код** - __отправить код в pastebin__ 
**!в "яз"** или **!to "lang"** - __перевод сообщения на английский__
**!id stick** / **!id msg** - __выдает указанные ID__
**!debug** - __выдает message в консоль__
""")

		elif '!рм' in msg or '!rm' in msg:
			if '!рмх' in msg or '!rmh' in msg:
				edit_buff_nyan(app, chat_id, msg_id)

			elif ('!рмк' in msg or '!рма' in msg 
			or '!rmk' in msg or '!rma' in msg):
				del_katsu(app, chat_id, msgs)
				
app.run()