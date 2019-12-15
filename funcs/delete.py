from config import nyanpasu_id, katsu_id
from time import sleep as sleep

def edit_buff_nyan(app, chat_id, msg_id):
    sleep(.050)
    app.edit_message_text(chat_id, msg_id, "Удаляю")
    sleep(1)
    app.edit_message_text(chat_id, msg_id, "Удалено")        
    sleep(2)
    app.delete_messages(chat_id, msg_id)

def delete(app, chat_id, c, uid):
    for message in app.iter_history(chat_id, 100):
        if str(message.from_user.id) == uid:
            a = message.message_id
            app.delete_messages(chat_id, a)
            sleep(.1)
            c = c - 1
            if c == 0: break

def del_nyanpasu(app, chat_id, msgs, msg_id, n, k, nyanpasu_stat):
    app.send_message(chat_id, 'Удаляю.')
    c = int(msgs[1])+1
    if msgs[0] in '!rmh':
        delete(app, chat_id, c, n)
        k_k = 1
    elif msgs[0] in '!rmk':
        delete(app, chat_id, 1, n)
        k_k = c
    elif msgs[0] in '!rma ':
        delete(app, chat_id, c, n)
        k_k = c
        
    if nyanpasu_stat == 'administrator':
        delete(app, chat_id, k_k, k)

def del_katsu(app, chat_id, msgs):
    delete(app, chat_id, msgs[1], str(katsu_id))