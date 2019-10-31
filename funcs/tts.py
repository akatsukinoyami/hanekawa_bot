from gtts import gTTS

def tts(message, chat, app):

	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()		

	langs = ['en', 'ru', 'fr', 'de', 'jp', 'ch']
	
	if str(msgs[1]) in langs:
		lang = str(msgs[1])
		txt = msb.replace('!tts '+str(msgs[1]), '')
	else: 
		lang = chat.lang
		txt = msb.replace('!tts ', '')			
	try:
		tts = gTTS(text=txt, lang=lang)
		tts.save('nya.mp3')
		app.send_voice(message.chat.id, 'nya.mp3', reply_to_message_id=message.message_id)
	except ValueError:
		txt = 'Ошибка распознавания текста.'
		message.reply(txt)