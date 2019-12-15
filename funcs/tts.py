from gtts	import gTTS
from os		import remove

def tts(chat, app, msb, mid, chat_id):

	msg = msb.lower()
	msgs = msg.split()
	act = app.send_chat_action

	langs = ['en', 'ru', 'fr', 'de', 'jp', 'ko', 'ua', 'cn']
	
	if str(msgs[1]) in langs:
		lang = str(msgs[1]).replace('jp', 'ja').replace('fr', 'fr-fr').replace('ua', 'uk').replace('cn', 'zh-cn')
		txt = msb.replace('!tts '+str(msgs[1]), '')
	else: 
		lang = chat.lang
		txt = msb.replace('!tts ', '')			
	try: 
		act(chat_id, "record_audio")
		tts = gTTS(text=txt, lang=lang)
		name = 'nya.mp3'
		tts.save(name)
		app.send_voice(chat_id, name, reply_to_message_id=mid)
		remove(name)
		act(chat_id, "cancel")
	except ValueError:
		act(chat_id, "typnig")
		txt = 'Ошибка, язык не поддерживается.'
		act(chat_id, "cancel")
		msg = message.reply(txt)
		sleep(5)
		app.delete_messages(msg.chat.id, msg.message_id)