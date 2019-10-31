class Reply_message:
	def __init__(self, code, attr='none'):
		self.code = code
		self.attr = attr
	
class T(Reply_message):
	def reply(self, message):
		message.reply_text(self.code)

class S(Reply_message):
	def reply(self, message):
		message.reply_sticker(self.code)

class V(Reply_message):
	def reply(self, message):
		message.reply_voice(self.code)

name = 'Хдебушек'

ru_nyan = {
('акацуки',) : (
	T("Кто взывает к Рассвету Тьмы?"),),
('awoo+', 'аву+') : (
	T("Awoo =^o^= ~", 'nyan'), 
	T('Awoo', 'nyan'), 
	T('Авууу!', 'nyan')),
('му*р', 'пур+') : (
	T('Мур', 'nyan'), 
	T('Пурр', 'nyan'), 
	T('Murrr', 'nyan'), 
	T('Purrr', 'nyan')),
('ня+', 'ня+к', 'nya+', 'мя+у') : (
	T('Ня ^_^', 'nyan'), 
	T('Няяяя~', 'nyan'), 
	T('Няу *-*', 'nyan'), 
	T('Nya', 'nyan'), 
	T('Мяу', 'nyan'),
	S('CAADAgADaCkAAuCjggc25OCNdwABB-QWBA', 'nyan'),
	S('CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE', 'nyan')),
('ку+сь',) : (
	T('Кусь, няха ^_^', 'nyan'), T('Кусь, б-бака >_<', 'scar')),
('ли+зь',) : (
	T("Лизь тебя <3", 'lewd'), 
	T('*покраснела*', 'lewd')),
('ла+пк',) : (
	S('CAADAgAD_GcAAuCjggcc4yEXnt2GTBYE', 'lewd'),),
('ра+вр+', 'ррр+', 'ra+wr+', 'rrr+') : (
	T('Ррр!', 'angr'),
	T('Равр!', 'angr'), 
	T('Rawr!', 'angr'), 
	T('Rrr!', 'angr')),
('тыгыдык',) : (
	T('Тыгыдык!'),),
('ме+х','me+h') : (
	T('Вздыхает'), T('Пушисто!')),
('бу+ль',) : (
	T('Буууульк!', 'nyan'), 
	T('Бууууль', 'nyan'), 
	T('Буль-буль', 'nyan')),
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
	T('Приветствую'), T('Здравствуй'), T('Добро Пожаловать'),
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
	T('*'+name+' дрожит от холода*'), T('*'+name+' включает обогреватель*')),
('тимур',) : (
	T('Копай, бля!', 'scar'),
	T('*'+name+' прячется за занавеской* >_<', 'scar'),
	S('CAADAgADWCkAAuCjggdo5gnw-q-JfRYE', 'scar'))}

ru_lewd ={
('акацуки',) : (
	T("Зачем тебе папочка?"),),
('awoo+', 'аву+') : (
	T("Awoo =^o^= ~"), T('Awoo'), T('Авууу!')),
('му*р', 'пур+') : (
	T('Муррр'), T('Мур'), T('Пурр'),),
('ла+пк',) : (
	T('*'+name+' расстегивает пуговку расширяя декольте*', 'lewd'),),
('ня+', 'ня+к', 'nya+', 'мя+у') : (
	T('Ня ^_^', 'nyan'), 
	T('Няяяя~', 'nyan'), 
	T('Няу *-*', 'nyan'), 
	T('Nya', 'nyan'), 
	T('Мяяяяяу', 'nyan')),
('ку+сь',) : (
	T('Кусь, няха ^_^', 'nyan'), 
	T('*Нежно кусь за ушко*', 'lewd'), 
	T('*'+name+' аккуратно кусает шею*', 'lewd')),
('ли+зь',) : (
	T("Лизь тебя в щечку", 'lewd'), 
	T('*покраснела*', 'lewd'), 
	T("Нежно лизь ушко", 'lewd')),
('це+м',) : (
	T('*'+name+' нежно целует в щечку', 'lewd'), 
	T('*'+name+' эротично целует по-французски', 'lewd')),
('утра', 'утречка', 'охайо', 'охаё') : (
	T('Утречка, не устал после вчерашнего?', 'lewd'), 
	T('Привет))'), 
	T('Охайо^^')),
('ночи', 'снов') : (
	T('Эротических сновидений, *цем*', 'lewd'), 
	T('Сладких снов, дорогуша'), 
	T('Оясуминасай, Аната *-*')),
('приве+т', 'здравствуй') : (
	T('*'+name+' приветственно целует*', 'lewd'),),
('жарко',) : (
	T('*'+name+' садится голышом на подоконник*', 'lewd'), 
	T('*У '+name+' вода пролилась на маечку и просвечивает*', 'lewd'), 
	T('*'+name+' раздевается, чтобы охладится*', 'lewd')),
('холодно',) : (
	T('*'+name+' шалит под котацу чтобы согрется*', 'lewd'), 
	T('*'+name+' дрожит от холода прикасающихся рук*', 'lewd'), 
	T('*'+name+' греется, обнимая голышом*', 'lewd'),)}

ru_angr = {
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
en_angr = {}
en_scar = {}

reacts = {
	'ru': {
	'nyan':ru_nyan,
	'lewd':ru_lewd,
	'angr':ru_angr,
	'scar':ru_scar
	},
	'en': {
	'nyan':en_nyan,
	'lewd':en_lewd,
	'angr':en_angr,
	'scar':en_scar
	}
}