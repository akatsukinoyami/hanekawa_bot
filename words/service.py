from words.ru.service import service as ru_service
from words.en.service import service as en_service

def lang_service(chat):
	service = eval(chat.lang+'_service')
	return service