import time
def mood_func(chat):
    mood_time = 60 * 4
    now = round(time.time())
    for i in chat.nyanc:
        k = now - i
        if k > mood_time:
            chat.nyanc.remove(i)
    for i in chat.lewdc:
        k = now - i
        if k > mood_time:
            chat.lewdc.remove(i)
    for i in chat.angrc:
        k = now - i
        if k > mood_time:
            chat.angrc.remove(i)
    for i in chat.scarc:
        k = now - i
        if k > mood_time:
            chat.scarc.remove(i)

    if len(chat.angrc) > 10:
        chat.mood = 'angr'
    elif len(chat.scarc) > 10:
        chat.mood = 'scar'
    elif len(chat.lewdc) > 10 and chat.nsfw == 1:
        chat.mood = 'lewd'
    elif len(chat.angrc) < 10 and len(chat.scarc) < 10 and len(chat.lewdc) < 10:
    	chat.mood = 'nyan'
    
    mood = chat.mood
    return mood