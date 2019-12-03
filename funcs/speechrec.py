from pydub  import AudioSegment
from config import wit_en_token, wit_ru_token
from wit	import Wit
from os	 import remove

def speech_recognition(app, message, lang):
	if   str(lang) == 'ru': 
		wit_cli = Wit(wit_ru_token)
	elif str(lang) == 'en': 
		wit_cli = Wit(wit_en_token)

	m		= message
	mf	  = message.from_user
	voice   = m.voice
	folder  = '/home/katsu/Documents/katsu_bots/audio/'
	name	= str(str(m.chat.id) +'_'+ str(m.message_id))
	name_p  = 'audio/'+'ogg'+name+'.ogg'
	name_i  = folder+'ogg'+name+'.ogg'
	name_o  = folder+'wav'+name+'.wav'

	app.download_media(voice.file_id, file_ref=voice.file_ref, file_name=name_p)

	song = AudioSegment.from_file(name_i, format='ogg')
	song.export(name_o, format="wav")
	remove(name_i)
	
	with open(name_o, 'rb') as f:
		resp = wit_cli.speech(f, None, {'Content-Type': 'audio/wav'})
	
	usrname = ('@' + str(mf.username)) if mf.username else mf.first_name
	txt = usrname + ' \n' + resp['_text']
	remove(name_o)

	message.reply(txt)