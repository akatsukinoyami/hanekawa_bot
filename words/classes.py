class Reply_message:
	def __init__(self, code, attr='none'):
		self.code = code
		self.attr = attr
	
class T(Reply_message):
	def reply(self, app, chat_id, msg_id):
		app.send_message(chat_id, text=self.code, reply_to_message_id=msg_id)
class S(Reply_message):
	def reply(self, app, chat_id, msg_id):
		app.send_sticker(chat_id, sticker=self.code, reply_to_message_id=msg_id)
class V(Reply_message):
	def reply(self, app, chat_id, msg_id):
		app.send_voice(chat_id, voice=self.code, reply_to_message_id=msg_id)