from config import katsu_id, nyanpasu_id
from time import sleep
def adminctl(app, message, chat, service):
    k = str(katsu_id)
    n = str(nyanpasu_id)
    msb = str(message.text)
    msg = msb.lower()
    msgs = msg.split()
    mmbr_id = str(message.from_user.id)
    chat_id = str(message.chat.id)
    try:    user = app.get_chat_member(chat_id, mmbr_id)
    except:    user = None
    rp = message.reply

    if (mmbr_id == k or mmbr_id == n or 
    user.status is 'administrator' or 
    user.status is 'creator'):

        print('admin funcs at '+str(chat_id)+' - '+str(message.message_id))

        if 'greet' in msg:
            if msgs[2] == 'on':
                chat.greetc = 1
                msg = rp(service['greet_on'])
            elif msgs[2] == 'off':
                chat.greetc = 0
                msg = rp(service['greet_off'])
            else:
                greet_txt = msb.replace(msgs[0]+' ', '')
                chat.greet = greet_txt
                msg = rp(service['rp_greet'])                    
        elif 'cond' in msg:
            if 'on' == msgs[2]:
                chat.cond = 1
                msg = rp(service['rp_on'])
            if 'off' == msgs[2]:
                chat.cond = 0
                msg = rp(service['rp_off'])
        elif 'nsfw' in msg:
            if 'on' in msgs[2]:
                chat.nsfw = 1
                msg = rp(service['nsfw_on'])
            if 'off' in msgs[2]:
                chat.nsfw = 0
                msg = rp(service['nsfw_off'])
        elif 'ttsm' in msg:
            if 'on' in msgs[2]:
                chat.ttsm = 1
                msg = rp(service['tts_on'])
            if 'off' in msgs[2]:
                chat.ttsm = 0
                msg = rp(service['tts_off'])
        elif 'lang' in msg:
            langs = ('ru', 'en')
            if msgs[2] in langs:
                chat.lang = msgs[2]
                msg = rp(service['ch_lang'])
            else:
                msg = rp(service['er_lang'])
        elif 'mood' in msg:
            moods = ('nyan', 'lewd', 'angr', 'scar')
            if msgs[2] in moods:
                chat.mood = msgs[2]
                msg = rp(service['ch_mood'])
            else:
                msg = rp(service['er_mood'])
        elif '!setkarma' in msg:
            mid = str(message.reply_to_message.from_user.id)
            user = chat.users[mid]
            n = msgs[1]
            user.karma = n
            msg = rp(str(eval(service['karma_ch'])))
        elif 'set_zero' in msg:
            chat.nyanc = []
            chat.lewdc = []
            chat.angrc = []
            chat.scarc = []
            msg = rp(service['zero'])
        elif 'user cond' in msg:
            mid = str(message.reply_to_message.from_user.id)
            usr_name = str(message.reply_to_message.from_user.username) if message.reply_to_message.from_user.username else message.reply_to_message.from_user.first_name
            if 'on' == msgs[2]:
                chat.users[mid].cond = 1
                msg = rp(eval(service['user_ad_on']))
            if 'off' == msgs[2]:
                chat.users[mid].cond = 0
                msg = rp(eval(service['user_ad_off']))    
        elif 'help' in msg:
            msg = rp(service['help_admin'])
        nyanpasu_mmbr = app.get_chat_member(chat_id, nyanpasu_id)
        nyanpasu_stat = nyanpasu_mmbr.status
        if nyanpasu_stat == 'administrator':
            app.delete_messages(chat_id, message.message_id)
            sleep(5)
            app.delete_messages(chat_id, msg.message_id)
    else:
        msg = rp(service['perm_er'])