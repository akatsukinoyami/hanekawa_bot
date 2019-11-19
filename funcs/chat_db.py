class User:
	def __init__(self, 
	cond=1, karma=0, ship = 0, 
	usern=None):
		self.cond	= cond
		self.karma	= karma
		self.ship	= ship
		self.usern	= usern

class ChatDB:
	def __init__(self, 
	cond=0, nsfw=0, greetc=1, ttsm = 0,	shipt=0,
	lang='ru', mood='nyan', users={}, greet='Добро пожаловать', 
	nyanc=[], lewdc = [], angrc = [], scarc = []):
		self.cond	= cond
		self.nsfw	= nsfw
		self.greetc	= greetc
		self.ttsm	= ttsm
		self.shipt	= shipt

		self.lang	= lang
		self.mood	= mood
		self.users	= users
		self.greet	= greet

		self.nyanc	= nyanc
		self.lewdc	= lewdc
		self.angrc	= angrc
		self.scarc	= scarc