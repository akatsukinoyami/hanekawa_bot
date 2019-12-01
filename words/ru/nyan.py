from words.classes import T, S, V
from words.config import nyanpasu_name

name = nyanpasu_name

nyan = {
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
	T('Purrr', 'nyan'),
	S('CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA', 'nyan'),),
('ня+', 'ня+к', 'nya+', 'мя+у') : (
	T('Ня ^_^', 'nyan'), 
	T('Няяяя~', 'nyan'), 
	T('Няу *-*', 'nyan'), 
	T('Nya', 'nyan'), 
	T('Мяу', 'nyan'),
	S('CAADAgADaCkAAuCjggc25OCNdwABB-QWBA', 'nyan'),
	S('CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA', 'nyan'),
	S('CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE', 'nyan')),
('ку+сь',) : (
	T('Кусь, няха ^_^', 'nyan'), 
	T('Кусь',), 
	T('Кусь, б-бака >_<', 'scar')),
('ли+зь',) : (
	T("Лизь тебя <3", 'lewd'), 
	T("Лизь~", 'lewd'), 
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