class Reply_message:
	def __init__(self, code):
		self.code = code
	
class T(Reply_message):
	def reply(self, message):
		message.reply_text(self.code)

class S(Reply_message):
	def reply(self, message):
		message.reply_sticker(self.code)

name = 'Хдебушек'

ru_nyan = {
('акацуки',) : (
	T("Кто взывает к Рассвету Тьмы?"),),
('awoo+', 'аву+') : (
	T("Awoo =^o^= ~"), T('Awoo'), T('Авууу!')),
('му*р', 'пур+') : (
	T('Мур'), T('Пурр'), T('Murrr'), T('Purrr')),
('ня+', 'ня+к', 'nya+', 'мя+у') : (
	T('Ня ^_^'), T('Няяяя~'), T('Няу *-*'), T('Nya'), T('Мяу'),
	S('CAADAgADaCkAAuCjggc25OCNdwABB-QWBA'),
	S('CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE')),
('ку+сь',) : (
	T('Кусь, няха ^_^'), T('Кусь, б-бака >_<')),
('ли+зь',) : (
	T("Лизь тебя <3"), T('*покраснела*')),
('ла+пк',) : (
	S('CAADAgAD_GcAAuCjggcc4yEXnt2GTBYE'),),
('ра+вр+', 'ррр+', 'ra+wr+', 'rrr+') : (
	T('Ррр!'), T('Равр!'), T('Rawr!'), T('Rrr!')),
('тыгыдык',) : (
	T('Тыгыдык!',)),
('ме+х','me+h') : (
	T('Вздыхает'), T('Пушисто!')),
('хз',) : (
	T("Хрен знает!"),
	S("CAADAgADxgADFTCdEMtnrnydTqyFFgQ"),
	S("CAADAQADgyMAAnj8xgVdT-nJb8X-4RYE")),
('утра', 'утречка', 'охайо', 'охаё') : (
	T('Утречка, няшка^^'), T('Утра'), T('Привет)'), T('Охайо^^'),
	S('CAADAgAD0mMAAuCjggfe1LWingZagRYE'),
	S('CAADAgADkCUAAuCjggeCPV98a6NIvhYE'),
	S('CAADAgADQikAAuCjggcJ3jT9RTZm-hYE'),
	S('CAADAgADXgEAAu243wpLqt8sTQivpRYE')),
('ночи', 'снов') : (
	T('Доброй ночи'), T('Приятных снов'), T('Оясуминасай'),
	S('CAADAgADuGcAAuCjggcEK4Wuw6OReBYE'),
	S('CAADAgADsyUAAuCjggerF63AIh5OCRYE')),
('приве+т', 'здравствуй') : (
	T('Приветствую'), T('Здравствуй'),
	S('CAADAgAD0mMAAuCjggfe1LWingZagRYE'),
	S('CAADAgADkCUAAuCjggeCPV98a6NIvhYE'),
	S('CAADAgADQikAAuCjggcJ3jT9RTZm-hYE')),
('вививи',) : (
	T('Вививи'), T('*'+name+' заводит старый жигуль*')),
('жарко',) : (
	T('*'+name+' открывает окно*'), T('*'+name+' кушает мороженое*'), 
	T('*'+name+' включает кондиционер*')),
('холодно',) : (
	T('*'+name+' укутывается в пледик*'), T('Бррр!'), 
	T('*'+name+' дрожжит от холода*'), T('*'+name+' включает обогреватель*')),
('тимур',) : (
	T('*'+name+' прячется за занавеской* >_<'),
	S('CAADAgADWCkAAuCjggdo5gnw-q-JfRYE'))}

ru_lewd ={
('акацуки',) : (
	T("Зачем тебе папочка?"),),
('awoo+', 'аву+') : (
	T("Awoo =^o^= ~"), T('Awoo'), T('Авууу!')),
('му*р', 'пур+') : (
	T('Муррр'), T('Мур'), T('Пурр'),),
('ла+пк',) : (
	T('*'+name+' расстегивает пуговку расширяя декольте*'),),
('ня+', 'ня+к', 'nya+', 'мя+у') : (
	T('Ня ^_^'), T('Няяяя~'), T('Няу *-*'), T('Nya'), T('Мяу')),
('ку+сь',) : (
	T('Кусь, няха ^_^'), T('*Нежно кусь за ушко*')),
('ли+зь',) : (
	T("Лизь тебя в щечку"), T('*покраснела*'), T("Нежно лизь ушко")),
('це+м',) : (
	T('*'+name+' нежно целует в щечку'), T('*'+name+' эротично целует по-французски')),
('утра', 'утречка', 'охайо', 'охаё') : (
	T('Утречка, не устал после вчерашнего?'), T('Привет))'), T('Охайо^^')),
('ночи', 'снов') : (
	T('Эротических сновидений, *цем*'), T('Сладких снов, дорогуша'), T('Оясуминасай, Аната *-*')),
('приве+т', 'здравствуй') : (
	T('*'+name+' приветственно целует*',)),
('жарко',) : (
	T('*'+name+' садится голышом на подоконник*'), 
	T('*У '+name+' вода пролилась на маечку и просвечивает*'), 
	T('*'+name+' раздевается, чтобы охладится*')),
('холодно',) : (
	T('*'+name+' шалит под котацу чтобы согрется*'), 
	T('*'+name+' дрожжит от холода прикасающихся рук*'), 
	T('*'+name+' греется, обнимая голышом*'),)}

ru_brut = {
('акацуки',) : (
	T("Кто взывает к Рассвету Тьмы?"),),
('awoo+', 'аву+') : (
	T('Awoo'), T('Авууу!')),
('ку+сь',) : (
	T('Грызь за ногу'), T('Грызь в шею')),
('ра+вр+', 'ррр+') : (
	T('Ррр!'), T('Равр!')),
('тыгыдык',) : (
	T('Тыгыдык по лицу'),),
('утра', 'утречка', 'охайо', 'охаё') : (
	T('Утра, чёрт'), T('Зачем приперся?'), T('Иди, досыпай вечным сном')),
('ночи', 'снов') : (
	T('Надеюсь, ты не проснешься'), T('Ты же больше не вернешься?'), T('Наконец-то')),
('приве+т', 'здравствуй') : (
	T('Что ты тут забыл?'), T('Проваливай!')),
('жарко',) : (
	T('*'+name+' включает обогреватель*'), T('*'+name+' подсыпает углей в печь*'), 
	T('*'+name+' включает кондиционер на обогрев*')),
('холодно',) : (
	T('*'+name+' включает кондиционер*'), T('*'+name+' тыкает мороженым в щеку*'), 
	T('*'+name+' протягивает ледяной коктейль*')),
('тимур',) : (
	T('*'+name+' выносит надоевший мусор*'),)}

ru_scar = {
('акацуки',) : (
	T("Кацу, спаси! >_<"),),
('awoo+', 'аву+') : (
	T("Aв-ву... >_<"), T('Aw-wo')),
('му*р', 'пур+') : (
	T('Мр'), T('*'+name+' испуганно тихо мурлыкает*')),
('ня+', 'ня+к', 'nya+', 'мя+у') : (
	T('Н-н-н-я...'), T('*'+name+' някнула из-за дивана*')),
('ку+сь',) : (
	T('Помогите!'), T('Ааа, кусают!')),
('ла+пк',) : (
	T("Ааа, не надо!*"+name+' убегает в страхе*')),
('ли+зь',) : (
	T('Отстань, извращенец!'), T('*'+name+' сжалась от страха, не в силах пошевелится*')),
('ра+вр+', 'ррр+') : (
	T('*'+name+' тихо рычит за углом*'),),
('ме+х',) : (
	T('Вздыхает'),),
('утра', 'утречка', 'охайо', 'охаё') : (
	T('Ут-тра...>_<'),),
('ночи', 'снов') : (
	T('*'+name+' пытается тихонько выйти из комнаты*'),),
('приве+т', 'здравствуй') : (
	T('Здравствуй'),),
('жарко',) : (
	T('*'+name+' открывает окно*'), T('*'+name+' включает кондиционер*')),
('холодно',) : (
	T('*'+name+' укутывается в пледик*'), T('Бррр!'), 
	T('*'+name+' дрожжит от холода*'), T('*'+name+' включает обогреватель*')),
('тимур',) : (
	T('*'+name+' прячется за занавеской* >_<'),)}

en_nyan = {
('akatsuki',) : (
	T("Who is calling for Katsu?"),),
('awoo+') : (
	T("Awoo =^o^= ~"), T('Awoo'), T('Аwoooo!')),
('mu*r', 'pur+') : (
	T('Murrr'), T('Purr')),
('mya+', 'nya+c') : (
	T('Nya ^_^'), T('Nyaaaaa~'), T('Nyau *-*'), T('Nya'), T('Meow!')),
('ra+wr+', 'rrr+') : (
	T('Rrr!'), T('Rawr!')),
('me+h',) : (
	T('Вздыхает'), T("Pawww!")),
('morning', 'ohaio') : (
	T('Утречка, няшка^^'), T('Утра'), T('Привет)'), T('Охайо^^')),
('ночи', 'снов') : (
	T('Доброй ночи'), T('Приятных снов'), T('Оясуминасай')),
('приве+т', 'здравствуй') : (
	T('Приветствую'), T('Здравствуй')),
('жарко',) : (
	T('*'+name+' открывает окно*'), T('*'+name+' кушает мороженое*'), 
	T('*'+name+' включает кондиционер*')),
('холодно',) : (
	T('*'+name+' укутывается в пледик*'), T('Бррр!'), 
	T('*'+name+' дрожжит от холода*'), T('*'+name+' включает обогреватель*')),}

en_lewd = {}
en_brut = {}
en_scar = {}

reacts = {
	'ru': {
	'nyan':ru_nyan,
	'lewd':ru_lewd,
	'brut':ru_brut,
	'scar':ru_scar
	},
	'en': {
	'nyan':en_nyan,
	'lewd':en_lewd,
	'brut':en_brut,
	'scar':en_scar
	}
}