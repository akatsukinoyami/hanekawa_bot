def stats(chat, service, id):
    if      int(chat.cond)      == 1:	cc = '✅'
    elif	int(chat.cond)      == 0: 	cc = '❌'
    if		int(chat.ttsm)      == 1: 	ct = '✅'
    elif	int(chat.ttsm)      == 0: 	ct = '❌'
    if 		int(chat.nsfw)      == 1: 	cn = '✅'
    elif	int(chat.nsfw)      == 0: 	cn = '❌'
    if 		int(chat.greetc)    == 1: 	cg = '✅'
    elif	int(chat.greetc)    == 0: 	cg = '❌'
    if 		str(chat.lang)      == 'ru':cl = '🇷🇺'
    elif 	str(chat.lang)      == 'en':cl = '🇺🇸'

    txt = (service['count']+'\n\n'+
    service['cond']+cc+'\n'+
    service['nsfw']+cn+'\n'+
    service['ttsm']+ct+'\n'+
    service['greet']+cg+'\n'+
    service['lang']+cl+'\n'+
    service['mood']+str(chat.mood)+'\n\n'+
    service['nyanc']+str(len(chat.nyanc))+'\n'+	
    service['lewdc']+str(len(chat.lewdc))+'\n'+
    service['angrc']+str(len(chat.angrc))+'\n'+
    service['scarc']+str(len(chat.scarc))+'\n\n'+
    service['rep_nps']+str(chat.users[id]))

    return txt