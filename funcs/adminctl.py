from config import katsu_id, nyanpasu_id
def adminctl(app, message, chat, service):
	k = str(katsu_id)
	n = str(nyanpasu_id)
	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()
	mmbr_id = str(message.from_user.id)
	chat_id = str(message.chat.id)
	try:	user = app.get_chat_member(chat_id, mmbr_id)
	except:	user = None
	rp = message.reply
	if (mmbr_id == k or mmbr_id == n or 
	user.status is 'administrator' or user.status is 'creator'):
		if '!greet' in msg:
			if msgs[1] == 'on':
				chat.greetc = 1
				rp(service['greet_on'])
			elif msgs[1] == 'off':
				chat.greetc = 0
				rp(service['greet_off'])
			else:
				greet_txt = msb.replace(msgs[0]+' ', '')
				chat.greet = greet_txt
				rp(service['rp_greet'])					
		elif '!cond' in msg:
			if 'on' == msgs[1]:
				chat.cond = 1
				rp(service['rp_on'])
			if 'off' == msgs[1]:
				chat.cond = 0
				rp(service['rp_off'])
		elif '!nsfw' in msg:
			if 'on' in msgs[1]:
				chat.nsfw = 1
				rp(service['nsfw_on'])
			if 'off' in msgs[1]:
				chat.nsfw = 0
				rp(service['nsfw_off'])
		elif '!ttsm' in msg:
			if 'on' in msgs[1]:
				chat.ttsm = 1
				rp(service['tts_on'])
			if 'off' in msgs[1]:
				chat.ttsm = 0
				rp(service['tts_off'])
		elif '!lang' in msg:
			langs = ('ru', 'en')
			if msgs[1] in langs:
				chat.lang = msgs[1]
				rp(service['ch_lang'])
			else:
				rp(service['er_lang'])
		elif '!mood' in msg:
			moods = ('nyan', 'lewd', 'angr', 'scar')
			if msgs[1] in moods:
				chat.mood = msgs[1]
				rp(service['ch_mood'])
			else:
				rp(service['er_mood'])
		elif '!setkarma' in msg:
			user = chat.users[message.reply_to_message.from_user.id]
			n = msgs[1]
			user.karma = n
			rp(str(eval(service['karma_ch'])))
		elif '!set_zero' in msg:
			chat.nyanc = []
			chat.lewdc = []
			chat.angrc = []
			chat.scarc = []
			rp(service['zero'])
	elif ('!greet' in msg 
	or '!cond' in msg 
	or '!nsfw' in msg
	or '!ttsm' in msg  
	or '!lang' in msg 
	or '!mood' in msg 
	or '!setkarma' in msg 
	or '!set_zero' in msg):
		rp(service['perm_er'])