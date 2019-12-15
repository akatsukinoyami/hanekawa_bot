service = {
	'rp_greet'		: 'Приветствие сохранено.',
	'cond'			: 'Ответчик: ',
	'lang'			: 'Язык: ',
	'ttsm'			: 'TTS: ',
	'nsfw'			: 'NSFW: ',
	'mood'			: 'Настроение: ',
	'greet'			: 'Приветствие: ',
	'greet_on'		: 'Приветствие включено.',
	'greet_off'		: 'Приветствие выключено.',
	'exit'			: 'Бот полностью выключен.',
	'rp_on'			: 'Ответчик для чата включен.',
	'rp_off'		: 'Ответчик для чата выключен.',
	'tts_on'		: 'Текст в речь включен.',
	'tts_off'		: 'Текст в речь выключен.',
	'nsfw_on'		: 'NSFW-режим включен.',
	'nsfw_off'		: 'NSFW-режим выключен.',
	'punt_lang'		: 'Язык не поддерживается.',
	'ch_lang'		: 'Язык изменен.',
	'er_leng'		: 'Ошибка изменения языка.',
	'ch_mood'		: 'Режим изменен.',
	'er_mood'		: 'Ошибка изменения режима.',
	'feedback'		: 'Ваш комментарий отправлен',
	'perm_er'		: 'Как будто я тебе позволю!',
	'nyan_admin_err': 'Для этого мне нужны права администратора.',
	'punto'			: ' ошибся в раскладке и написал:\n',
	'rep_nps'		: 'Репутация Ханекавы: ',
	'rep_er'		: 'А ну-ка не накручвай!',
	'rep_up'		: ("'Репутация @'+usr_name+' повышена'"),
	'use_stats'		: 'Твоя статистика: ',
	'use_cond'		: 'Ответчик: ',
	'use_ship'		: 'Шиппер:',
	'user_rp_on'	: 'Личное реагирование включено.',
	'user_rp_off'	: 'Личное реагирование выключено.',
	'user_ad_on'	: ("'Реагирование на пользователя @'+usr_name+' включено.'"),
	'user_ad_off'	: ("'Реагирование на пользователя @'+usr_name+' выключено.'"),
	'user_ship_on'	: 'Вы включены в списки поиска пар.',
	'user_ship_off'	: 'Вы исключены из списков поиска пар.',
	'karma_use'		: 'Твоя карма: ',
	'karma_for'		: 'Карма пользователя',
	'karma_err'		: 'Ошибка. Необходимо "ответить" на сообщение',
	'karma_ch'		: ("'Карма юзера '+user.usern+' изменена на '+n"),
	'count'			: 'Параметры чата: ',
	'nyanc'			: 'Няшность: ',
	'lewdc'			: 'Пошлость: ',
	'angrc'			: 'Злость: ',
	'scarc'			: 'Испуг: ',
	'zero'			: 'Счетчики обнулены',
	'vid_unav'		: 'Ошибка. Видео недоступно.',
	'rand_start'	: 'Запускаю генератор случайных чисел.',
	'rand_next'		: 'Ваш рандом почти готов.',
	'rand_result'	: 'Результат рандома между ',
	'&'				: ' и ',
	'rand_error'	: 'Неправильные значения.\n Попробуй так: !rand 5 10',
	'choice1'		: 'Из последовательности: ',
	'choice2'		: '\nВыбран элемент: ',
	'trans_start'	: 'Сейчас переведу',
	'trans_next'	: ' попросил перевести: \n',
	'sprec_start'	: 'Голосовое сообщение принято к обработке.',
	'id_error'		: 'Ошибка нахождения ID',
	'helpe'			: """!exch № валюта-из валюта-в(или auto)
!exch add валюта - добавить валюту в auto
!exch del валюта - удалить валюту из auto
	""",
	'help'			: """!help - эта справка
!exch help - справка по курсам валют
!config help - справка админ команд
!user help - справка настроек пользователя
!ut help - справка по модулю youtube-dl
!rand help - справка по модулю рандома
!trans help - cправка по переводчику
!stats - показатели чата
!admins - админы чата
!karma - репутация cвоя
!karma - репутация пользователя (reply)
!tts "яз" - текст в речь
!feedback - отправить комментарий создателю""",
	'help_admin'	: """!config lang - изменить язык ответчика (ru, en)
!config mood - изменить режим ответчика (nyan, lewd, brut, scar)
!config greet - указать приветствие новому учаснику
!config greet on/off - вкл/выкл приветствие
!config cond on/off - вкл/выкл ответчик в чате
!config nsfw on/off - вкл/выкл пошлый режим
!config ttsm on/off - вкл/выкл текст-в-речь
!config set_zero - обнуляет счетчики настроения
!kick (число) (s, m, h, d) - кикнуть человека на определенное время
!mute (число) (s, m, h, d) - рид-онли человека на определенное время
!setkarma - установить карму пользователя (reply)""",
	'help_usr_set'	: """!user cond on/off - вкл/выкл бота для себя
!user shipper on/off - вкл/выкл шиппер для себя""",
	'help_youtube'	: """!ut vid (link) - скачать видео в телеграм (480р)
!ut vid (res) (link) - скачать в указанном разрешении
!ut aud (link) - скачать аудиодорожку
!ut link (link) - получить прямую ссылку на видео (480р)
!ut link (res) (link) - ссылка в указанном разрешении
Вместо (res) - 144, 240, 360, 480, 720, 1080, 1440, 2160""",
	'help_trans'	: """!translate "яз" - перевести сообщ или реплай
!trans "яз" 
!tl "яз" """,
	'help_rand'		: """!rand choice (слова) - выбрать одно слово из последовательности
!rand "от" "до" - рандом в промежутке""",
}