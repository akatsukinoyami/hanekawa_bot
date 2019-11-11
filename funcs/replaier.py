from words.words import reacts
import random
import time
import re

now = round(time.time())

def replaier(chat, message):
	lang = chat.lang
	mood = chat.mood
	msb = str(message.text)
	msg = msb.lower()
	for triggers, reaction in reacts[lang][mood].items():
				for trigger in triggers:
					if re.search(r'\b'+trigger, msg):
						a = random.choice(reaction)
						a.reply(message)
						if a.attr == 'nyan':
							chat.nyanc.append(now)
						elif a.attr == 'lewd':
							chat.lewdc.append(now)
						elif a.attr == 'angr':
							chat.angrc.append(now)
						elif a.attr == 'scar':
							chat.scarc.append(now)