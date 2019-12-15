def roleplay(app, nyanpasu_id, mode, chat_id, txt, msg_id, usrname):
    nyanpasu = app.get_chat_member(chat_id, nyanpasu_id)
    if mode in '/me':
        txt = txt.replace('/me ', '')
        txt = '**✵'+usrname+'** '+txt
        app.send_message(chat_id, txt)
        if nyanpasu.status == 'administrator': app.delete_messages(chat_id, msg_id)