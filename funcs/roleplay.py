def roleplay(app, nyanpasu_id, mode, chat_id, txt, msg_id, usrname):
    if mode in '/me':
        txt = txt.replace('/me ', '')
        txt = '**✵'+usrname+'** '+txt
        app.send_message(chat_id, txt)
    nyanpasu_mmbr = app.get_chat_member(chat_id, nyanpasu_id)
    nyanpasu_stat = nyanpasu_mmbr.status
    if nyanpasu_stat == 'administrator': app.delete_messages(chat_id, msg_id)