import random
import time
import re

def replaier(reacts, lang, mood, chat, message, msg):
	for triggers, reaction in reacts[lang][mood].items():
				for trigger in triggers:
					if re.search(r'\b'+trigger, msg):
						a = random.choice(reaction)
						a.reply(message)
						now = round(time.time())
						if a.attr == 'nyan':
							chat.nyanc.append(now)
						elif a.attr == 'lewd':
							chat.lewdc.append(now)
						elif a.attr == 'angr':
							chat.angrc.append(now)
						elif a.attr == 'scar':
							chat.scarc.append(now)