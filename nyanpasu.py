from pyrogram import Client, MessageHandler, Filters, ChatMember
from time import sleep as sleep
import random
import shelve
import time

from config import api_id, api_hash, chaos_id, nyanpasu_un, nyanpasu_id, katsu_id
from words.service		import lang_service
from funcs.rep 			import user_make, user_rep_change
from funcs.chat_db		import ChatDB as chat_db
from funcs.functions	import functions
from funcs.mood 		import mood_func
from funcs.replaier 	import replaier
from funcs.adminctl 	import adminctl
from funcs.chat_db 		import User
from funcs.ship 		import ship

with shelve.open('DB') as db:
	app = Client("hebushek", api_id, api_hash)
	@app.on_message((Filters.group | Filters.private))
	def nyanpasu(Client, message):
		k = str(katsu_id)
		n = str(nyanpasu_id)
		chat_id = str(message.chat.id)
		mmbr = message.from_user
		reply = message.reply_to_message
		try:
			reply_msg_id = reply.message_id
			reply_msg_txt = reply.text
			reply_user_id = str(reply.from_user.id)
			reply_user_fname  = str(reply.from_user.first_name)
			if reply.from_user.username:
				reply_usrname = '@' + str(reply.from_user.username)
			else:
				reply_usrname = reply_first_name
		except BaseException:
			reply_msg_id = None
			reply_msg_txt = None
			reply_user_id = None
			reply_user_fname  = None
			reply_usrname = None

		if chat_id not in db:
			db[chat_id] = chat_db()
		chat	= db[chat_id]

		msb = str(message.text)
		msg = msb.lower()
		msgs = msg.split()

		service = lang_service(chat)
		chat.mood = mood_func(chat)
		user_make(message, chat, service)
		
		if message.new_chat_members and chat.greetc == 1: rp(chat.greet)

		elif '!' in msg:
			functions(app, message, chat, service)
			if message.chat.type == 'supergroup':
				adminctl(app, message, chat, service)

		elif chat.cond == 1 and chat.users[mmbr.id].cond == 1:
			if (reply_user_id == n or reply_user_id == None):
				replaier(chat, message)

		elif chat.cond == 0 or chat.users[mmbr.id].cond == 0:
			if (reply_user_id == n or nyanpasu_un in msg):
				replaier(chat, message)
		
		elif (
			'!rma ' in msg	or '!rmh ' in msg	or 
			'!рма ' in msg	or '!рмх ' in msg)	and (
			mmbr.id == k	or mmbr.id == n):
					с = int(msg.replace('!rma ','').replace('!rmh ','').replace('!рмх ', '').replace('!рма ', ''))
					for message in app.iter_history(chat_id, 100):
						if message.from_user.id == n:
							sleep(.1)
							app.delete_messages(chat_id, message.message_id)
							с = с - 1
							if с == 0: break
		
		elif reply_user_id:
			user_rep_change(message, chat, reply_user_id, service, rep_usr_name)

		db[chat_id] = chat
		db.sync()
	
	app.run()