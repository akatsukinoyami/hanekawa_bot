class ChatDB:
		def __init__(self, cond=0, nsfw=0, lang='ru', mood='nyan', ttsm = 0, greet=None, 
		nyanc=[], lewdc = [], angrc = [], scarc = []):
			self.cond	= cond
			self.nsfw	= nsfw
			self.lang	= lang
			self.mood	= mood
			self.ttsm	= ttsm
			self.greet	= greet
			self.nyanc	= nyanc
			self.lewdc	= lewdc
			self.angrc	= angrc
			self.scarc	= scarc