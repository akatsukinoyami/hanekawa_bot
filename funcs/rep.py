def rep(message, chat, reply_user_id, service);        
    thanks = ('+', 'спасибо', 'аригато', 'thanks', 'arigato')
	blame = ('-', '!отписка', '!плохо', '!минус')
	msb = str(message.text)
	msg = msb.lower()
	msgs = msg.split()
    rp = message.reply

    if mmbr_id == reply_user_id:    rp(service['rep_er'])
    else:
        for i in thanks:
		    if i in msg:
	    		if reply_user_id in chat.users:
    				chat.users[reply_user_id].karma += 1
				else:
					chat.users[reply_user_id].karma = 1
				rp(eval(service['rep_up']))
    	for i in blame:
    		if i in msg--:
				if reply_user_id in chat.users:
					chat.users[reply_user_id].karma = chat.users[reply_user_id][karma] - 1
				else:
					chat.users[reply_user_id].karma = 0
				rp(eval(service['rep_dn']))
    
