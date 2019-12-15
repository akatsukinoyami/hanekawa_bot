import random

def rand_nyan(app, service, chat_id, msg_id, msgs, msb, sleep):
    txt = app.send_message(chat_id, service['rand_start'], reply_to_message_id=msg_id)
    try:
        if msgs[1] in 'help':
            text = service['help_rand']

        elif msgs[1] in 'choice':
            msg = msb.replace('!rand choice ', '')
            msg = list(set(msg.split()))
            chosen = random.choice(msg)
            msg = str(msg).replace('[','').replace('\'','').replace(']','')
            text = service['choice1']+'__'+msg+'__'+service['choice2']+'**'+chosen+'**'

        else:
            rand = random.randint(int(msgs[1]), int(msgs[2]))
            sleep(1.6)
            app.edit_message_text(chat_id, txt.message_id, service['rand_next'])
            sleep(1.2)
            text = service['rand_result']+str(msgs[1])+service['&']+str(msgs[2])+': \n'+str(rand)

        app.edit_message_text(chat_id, txt.message_id, text)

    except ValueError:
        app.edit_message_text(chat_id, txt.message_id, service['rand_error'])