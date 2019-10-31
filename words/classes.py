class Reply_message:
	def __init__(self, code, attr='none'):
		self.code = code
		self.attr = attr
	
class T(Reply_message):
	def reply(self, message):
		message.reply_text(self.code)
class S(Reply_message):
	def reply(self, message):
		message.reply_sticker(self.code)
class V(Reply_message):
	def reply(self, message):
		message.reply_voice(self.code)