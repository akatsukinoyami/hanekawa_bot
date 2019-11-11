import random
import time

def ship(app, message, chat):
	chat_id = str(message.chat.id)
	user = chat.users
	usr1 = random.chose(user)
	usr2 = random.chose(user)
	while usr2 == usr1: 
		usr2 = random.chose(user)
		
	chat.shipt = time.time()
	txt = ('Поздравляем пару дня: \n'+usr1.usern+' + '+usr2.usern)
