from googletrans import Translator
translator = Translator()

def translates(app, lang, msb, chat_id, message, usrname, reply_usrname):
    langs = ['en', 'ru', 'fr', 'de', 'jp', 'ch']
    msgrp = msb.split()
    sleep(1)
    if msgs[1] == 'help':
        app.send_message(chat_id, service['help_trans'], 
            reply_to_message_id = msg_id, disable_notification=True)
    elif msgrp[1] in langs:
        new_msg = app.send_message(chat_id, service['trans_start'], 
            reply_to_message_id = msg_id, disable_notification=True)
        if message.reply_to_message:
            text = (message.reply_to_message.text)
            txt = (translator.translate(text, dest=msgrp[1])).text
            txt = reply_usrname+service['trans_next']+txt
        else:
            text = msb.replace('!translate '+msgrp[1]+' ', '').replace('!trans '+msgrp[1]+' ', '').replace('!tl '+msgrp[1]+' ', '')
            txt = (translator.translate(text, dest=msgrp[1])).text
            txt = usrname+service['trans_next']+txt
    app.edit_message_text(chat_id, new_msg.message_id, txt)