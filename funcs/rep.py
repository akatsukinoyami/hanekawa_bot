from config import nyanpasu_un
from config import nyanpasu_id as n
from funcs.chat_db import User

def user_make(message, chat, service):
	mmbr = message.from_user
	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()

	if mmbr.id not in chat.users:
		chat.users[mmbr.id] = User(cond=1, karma=0, ship = 0, usern=mmbr.username)
	else: 
		chat.users[mmbr.id].usern = mmbr.username

	if n not in chat.users:
		chat.users[n] = User(cond=1, karma=0, ship =0, usern=nyanpasu_un)

	if message.reply_to_message != None:
		reply = message.reply_to_message
		rmbr = message.reply_to_message.from_user
		
		if rmbr.id not in chat.users:
			if rmbr.username:
				reply_usrname = rmbr.username
			else:
				reply_usrname = rmbr.first_name
			chat.users[rmbr.id] = User(cond=1, karma=0, ship = 0, usern=reply_usrname)
		else:
			if chat.users[rmbr.id].usern != rmbr.username:
				if rmbr.username:
					chat.users[rmbr.id].usern = rmbr.username
				else:
					chat.users[rmbr.id].usern = rmbr.first_name



def user_rep_change(message, chat, reply_user_id, service, rep_usr_name):	
	thanks = ('+', 'спасибо', 'аригато', 'thanks', 'arigato')
	blame = ('-', '!отписка', '!плохо', '!минус')
	mmbr_id = str(message.from_user.id)
	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()
	rp = message.reply
	
	if mmbr_id == reply_user_id:
		rp(service['rep_er'])
	elif message.reply_to_message:
		usr_name = str(message.reply_to_message.from_user.username)
		for i in thanks:
			if i in msg:
				if reply_user_id in chat.users:
					chat.users[reply_user_id].karma += 1
				else:
					chat.users[reply_user_id].karma = 1
				rp(eval(service['rep_up']))
		for i in blame:
			if i in msg:
				if reply_user_id in chat.users:
					chat.users[reply_user_id].karma = chat.users[reply_user_id].karma- 1
				else:
					chat.users[reply_user_id].karma = 0
				rp(eval(service['rep_dn']))