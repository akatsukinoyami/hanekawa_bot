class User:
	def __init__(self, karma=0, cond=1, sex=None, ship=1):
		self.cond	= cond
		self.karma	= karma
		self.sex 	= sex
		self.ship	= ship

class ChatDB:
	def __init__(self, 
	cond=0, nsfw=0, greetc=0, ttsm = 0, 
	lang='ru', mood='nyan', users={}, greet='Добро пожаловать', 
	nyanc=[], lewdc = [], angrc = [], scarc = []):
		self.cond	= cond
		self.nsfw	= nsfw
		self.greetc	= greetc
		self.ttsm	= ttsm

		self.lang	= lang
		self.mood	= mood
		self.users	= users
		self.greet	= greet

		self.nyanc	= nyanc
		self.lewdc	= lewdc
		self.angrc	= angrc
		self.scarc	= scarc