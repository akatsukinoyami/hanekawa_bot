from config import nyanpasu_id
from funcs.rep import user_make

def chat_stats(chat, service):
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
    service['rep_nps']+str(chat.users[nyanpasu_id].karma))

    return txt

def my_stats(chat, service, mmbr_id):
    if      int(chat.users[mmbr_id].cond)       ==  1:	uc = '✅'
    elif	int(chat.users[mmbr_id].cond)       ==  0: 	uc = '❌'

    if      str(chat.users[mmbr_id].sex)        ==  'men':	us = '🙎‍♂️'
    elif	str(chat.users[mmbr_id].sex)        ==  'fem': 	us = '🙎‍♀️'

    if      str(chat.users[mmbr_id].relt)       ==  'men':
        if      str(chat.users[mmbr_id].sex)        ==  'men':	ur = '👨‍❤️‍👨'
        elif	str(chat.users[mmbr_id].sex)        ==  'fem': 	ur = '💑'
    elif    str(chat.users[mmbr_id].relt)       ==  'fem':
        if      str(chat.users[mmbr_id].sex)        ==  'men':	ur = '💑'
        elif	str(chat.users[mmbr_id].sex)        ==  'fem': 	ur = '👩‍❤️‍👩'
    elif    str(chat.users[mmbr_id].relt)       ==  'all':      ur = 'All'
    elif    str(chat.users[mmbr_id].relt)       ==  'None':     ur = '❌'

    txt = (service['use_stats']+'\n\n'+
    service['use_cond']+uc+'\n'+
    service['use_sex']+us+'\n'+
    service['use_rel']+ur+'\n'+
    service['karma_use']+chat.users[mmbr_id].karma)

def stat(service, message, chat):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username:
            reply_username = str(message.reply_to_message.from_user.username)
        else:
            reply_username = str(message.reply_to_message.from_user.first_name)

        reply_user_id = str(message.reply_to_message.from_user.id)
        if chat.users[reply_user_id].karma:
            karma = str(chat.users[reply_user_id].karma)
        else:
            user_make(message, chat, service)
            karma = str(chat.users[reply_user_id].karma)
        txt = service['karma_for']+' @'+reply_username+': '+karma
    else:
        txt = service['karma_err']
    return txt