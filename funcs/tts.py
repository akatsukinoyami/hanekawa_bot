from gtts	import gTTS
from os		import remove

def tts(message, chat, app):

	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()		

	langs = ['en', 'ru', 'fr', 'de', 'jp', 'ko', 'ua', 'cn']
	
	if str(msgs[1]) in langs:
		lang = str(msgs[1]).replace('jp', 'ja').replace('fr', 'fr-fr').replace('ua', 'uk').replace('cn', 'zh-cn')
		txt = msb.replace('!tts '+str(msgs[1]), '')
	else: 
		lang = chat.lang
		txt = msb.replace('!tts ', '')			
	try:
		tts = gTTS(text=txt, lang=lang)
		name = 'nya.mp3'
		tts.save(name)
		app.send_voice(message.chat.id, name, reply_to_message_id=message.message_id)
		remove(name)
	except ValueError:
		txt = 'Ошибка, язык не поддерживается.'
		message.reply(txt)