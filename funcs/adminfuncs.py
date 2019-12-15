from pyrogram import ChatPermissions
import time as clock
import traceback

def adminfuncs(app, chat_id, user_id, nyanpasu_id, katsu_id, mmbr_id, msgs, message):
    user = app.get_chat_member(chat_id, user_id)
    if (user.status is 'administrator' or 
        user.status is 'creator' or 
        mmbr_id == katsu_id or 
        mmbr_id == nyanpasu_id):

        nyanpasu = app.get_chat_member(chat_id, nyanpasu_id)
        if (nyanpasu.status is 'administrator' or 
            nyanpasu.status is 'creator'):

            print('admin funcs at '+str(chat_id)+' - '+str(message.message_id))
            
            if len(msgs) == 3:
                if   'd' in msgs[2]: mult = 86400
                elif 'h' in msgs[2]: mult = 3600
                elif 'm' in msgs[2]: mult = 60
                elif 's' in msgs[2]: mult = 1
                time = int(msgs[1])*mult
            elif len(msgs) == 2: time = int(msgs[1])
            elif len(msgs) == 1: time = 120
            time = int(clock.time() + time)

            try:
                if msgs[0] in '!kick':
                    app.kick_chat_member(chat_id, user_id, time)
                    txt = '**'+message.reply_to_message.from_user.first_name+'** кикнут из чата.'
                elif msgs[0] in '!mute':
                    app.restrict_chat_member(chat_id, user_id, 
                        ChatPermissions(can_send_messages=False), time)
                    txt = '**'+message.reply_to_message.from_user.first_name+'** отправлен в Р/О.'
            except Exception as e:
                if 'USER_ADMIN_INVALID' in str(e):
                    txt = 'Невозможно забанить администратора.'
        else: txt = service['nyan_admin_err']
    else: txt = service['perm_err']
    app.send_message(chat_id, txt, reply_to_message_id=message.message_id)