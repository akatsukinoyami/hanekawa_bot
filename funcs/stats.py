from config import nyanpasu_id
from funcs.rep import user_make

def chat_stats(chat, service):
    cc = '✅' if int(chat.cond)   else '❌'
    ct = '✅' if	int(chat.ttsm)   else '❌'
    cn = '✅' if	int(chat.nsfw)   else '❌'
    cg = '✅' if	int(chat.greetc) else '❌'
    if 	 str(chat.lang) == 'ru':cl = '🇷🇺'
    elif str(chat.lang) == 'en':cl = '🇺🇸'

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
    uc = '✅' if int(chat.users[mmbr_id].cond) else '❌'
    us = '✅' if int(chat.users[mmbr_id].ship) else '❌'

    txt = (service['use_stats']+'\n\n'+
    service['use_cond']+uc+'\n'+
    service['use_ship']+us+'\n'+
    service['karma_use']+str(chat.users[mmbr_id].karma))
    return txt

def stat(service, message, chat):
    if message.reply_to_message:
        reply = message.reply_to_message
        reply_user = message.reply_to_message.from_user
        if reply_user.username:
            reply_username = str(reply_user.username)
        else:
            reply_username = str(reply_user.first_name)

        if chat.users[reply_user.id].karma:
            True
        else:
            user_make(message, chat, service)
        karma = str(chat.users[reply_user.id].karma)
        txt = service['karma_for']+' @'+reply_username+': '+karma
    else:
        txt = service['karma_err']
    return txt