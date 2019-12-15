try:                from StringIO  import StringIO
except ImportError: from io        import StringIO
from time import time
from os import remove
import urllib.request
import youtube_dl
import shelve
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")

def strRoundFloat(number1, number2=0, cat=0):
    if number2 == 0: number = str(round(float(number1)/1000000, 2))
    elif   cat == 0: number = str(round(float(number1/(number2/100)/2)))
    elif   cat == 1: number = str(round(float((number1/(number2/100)/2)+50)))
    return           number

def upload_progress(current, total, app, chat_id, msg_id):
    if round(time())%3  == 0:
        percent = strRoundFloat(current, total, 1)
        current = strRoundFloat(current)
        total   = strRoundFloat(total)
        text    = 'Uploaded '+current+' Mb of '+total+' Mb ('+percent+'%).'
        app.edit_message_text(chat_id, msg_id, text)

def ut_dl(ydl_opts, link):
    with Capturing() as output:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    return output

def title_finder(app, chat_id, msg_id, ut_dl, ydl_opts, link):
    text = str(ut_dl(ydl_opts, link))
    text = text.split(', ')
    for i in range(len(text)):
        if 'webpage' in text[i]:
            title = str(text[i+1])
            title = title.replace('\'', '')
    return title

def dirlink(chat_id, link, app, name, msg, height='480'):
    ydl_opts = {
        'format'    : 'best[height='+str(height)+']/best',
        'forcetitle': True,
        'forceurl'  : True,
        'simulate'  : True,
    } 
    text = str(ut_dl(ydl_opts, link))
    text = text.split(', ')
    for i in range(len(text)):
        print(text[i])
        if 'http' in text[i]:
            url = str(tiny_url(str(text[i]).replace('\'', '')))
            title = str(text[i-1])
            txt = title +'\n' + url
            app.edit_message_text(chat_id, msg.message_id, txt)

def down_func(msg_id, chat_id, link, app, upload, service, height='480'):
    try:
            act = app.send_chat_action
            name = str(str(chat_id)+'_'+str(msg_id)+upload)
            link = str(link)
            msg = app.send_message(chat_id, 'Looking for a file.', reply_to_message_id=msg_id, disable_notification=True)
            if upload == 'typing':
                app.edit_message_text(chat_id, msg.message_id, 'Fetching direct link.')
                stat = upload
                act(chat_id, stat)
                dirlink(chat_id, link, app, name, msg, height)
            else:
                stat = 'upload'+upload
                act(chat_id, stat)
                newMsgId=msg.message_id
                def download_progress(d):
                    if d['status']  == 'downloading' and round(time())%3  == 0:
                        percent = strRoundFloat(d['downloaded_bytes'], d['total_bytes'], 0)
                        current = strRoundFloat(d['downloaded_bytes'])
                        total   = strRoundFloat(d['total_bytes'])
                        text    = 'Downloaded '+current+' Mb of '+total+' Mb ('+percent+'%).'
                        app.edit_message_text(chat_id, newMsgId, text)
                        
                ydl_opts = {'format' : 'best',
                            'outtmpl': name, 
                        'forcetitle' : True,
                    'progress_hooks' : [download_progress]}
                app.edit_message_text(chat_id, msg.message_id,'Started download '+upload.replace('_','')+'.')

                if upload == '_video':
                    ydl_opts['format'] = 'best[height='+str(height)+']/best'
                    title = title_finder(app, chat_id, msg.message_id, ut_dl, ydl_opts, link)
                    app.send_video(chat_id = chat_id, video = name, 
                        disable_notification = True, reply_to_message_id = msg_id,
                        height=int(height), caption=title, 
                        progress=upload_progress, progress_args=(app, chat_id, msg.message_id))

                elif upload == '_audio':
                    ydl_opts['format'] = 'mp3/bestaudio'
                    title = title_finder(app, chat_id, msg.message_id, ut_dl, ydl_opts, link)
                    app.send_audio(chat_id = chat_id, audio = name, 
                        disable_notification = True, reply_to_message_id = msg_id,
                        caption=title, title=title, 
                        progress=upload_progress, progress_args=(app, chat_id, msg.message_id))
                remove(name)
            app.delete_messages(chat_id, msg.message_id)
            app.send_chat_action(chat_id, 'cancel')
    except youtube_dl.utils.DownloadError:
            app.send_message(chat_id, service['vid_unav'])