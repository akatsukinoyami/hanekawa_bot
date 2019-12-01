from words.words import reacts
import random
import time
import re

now = round(time.time())

def replaier(chat, app, chat_id, msb, msg_id):
	lang = chat.lang
	mood = chat.mood
	msg = msb.lower()
	for triggers, reaction in reacts[lang][mood].items():
				for trigger in triggers:
					if re.search(r'\b'+trigger, msg):
						a = random.choice(reaction)
						a.reply(app, chat_id, msg_id)
						if a.attr == 'nyan':
							chat.nyanc.append(now)
						elif a.attr == 'lewd':
							chat.lewdc.append(now)
						elif a.attr == 'angr':
							chat.angrc.append(now)
						elif a.attr == 'scar':
							chat.scarc.append(now)