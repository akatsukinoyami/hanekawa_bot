try: 				from StringIO	import StringIO
except ImportError: from io 		import StringIO
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
		del self._stringio	# free up some memory
		sys.stdout = self._stdout

def tiny_url(url):
	apiurl = "http://tinyurl.com/api-create.php?url="
	tinyurl = urllib.request.urlopen(apiurl + url).read()
	return tinyurl.decode("utf-8")

def ut_dl(ydl_opts, link):
	with Capturing() as output:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([link])
	print('Downloaded file.')
	return output

def video_dl(msg_id, chat_id, link, app, name, height='480'):
	ydl_opts = {'format' : 'best[height='+str(height)+']/best',
				'outtmpl': name , 
			'forcetitle' : True,}
	text = str(ut_dl(ydl_opts, link))
	text = text.split(', ')
	for i in range(len(text)):
		if 'webpage' in text[i]:
			title = str(text[i+1])
			title = title.replace('\'', '')
	print('Started upload.')
	app.send_video(chat_id = chat_id, video = name, 
		disable_notification = True, reply_to_message_id = msg_id,
		height=int(height), caption=title)
	remove(name)
	
def audio_dl(msg_id, chat_id, link, app, name):
	ydl_opts = {'format' : 'mp3/bestaudio',
				'outtmpl': name , 
			'forcetitle' : True,}
	text = str(ut_dl(ydl_opts, link))
	text = text.split(', ')
	for i in range(len(text)):
		if 'webpage' in text[i]:
			title = str(text[i+1])
	print('Started upload.')
	app.send_audio(chat_id = chat_id, audio = name, 
		disable_notification = True, reply_to_message_id = msg_id,
		caption=title, title=title)
	remove(name)
	
	
def dirlink(chat_id, link, app, 
			name, height='480'):
	ydl_opts = {
		'format'	: 'best[height='+str(height)+']/best',
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
			app.send_message(chat_id, txt)
	

def down_func(msg_id, chat_id, link, app, upload, service, height='480'):
	file = 'youtube_db'
	try:
			act = app.send_chat_action
			name = str(str(chat_id)+'_'+str(msg_id)+upload)
			link = str(link)
			print('Looking for a file.')
			if upload == 'typing':
				print('Fetching direct link for '+link)
				stat = upload
				act(chat_id, stat)
				dirlink(chat_id, link, app, name, height)
			else:
				stat = 'upload'+upload
				act(chat_id, stat)
				
				print('Start download '+upload.replace('_','')+' from '+link)
				if upload == '_video':
					video_dl(msg_id, chat_id, link, app, name, height)
				elif upload == '_audio':
					audio_dl(msg_id, chat_id, link, app, name)
			
			print('File uploaded to telegram.')
			app.send_chat_action(chat_id, 'cancel')
	except youtube_dl.utils.DownloadError:
			app.send_message(chat_id, service['vid_unav'])