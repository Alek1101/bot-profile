survey_1 = {
    'location_1': {
        'question': '',
        'choice': ''
    },
    'location_2': {
        'question': '',
        'choice': ''
    },
    'location_3': {
        'question': '',
        'choice': ''
    },
    'location_4': {
        'question': '',
        'choice': ''
    },
    'location_5': {
        'question': '',
        'choice': ''
    },
}

# plot = {
#     'В данном текстовом квесте вы играете за компьютерную программу, цель которой - обнаружить заразивший устройство '
#     'вирус.'
#     '\nВаш прототип - SEO - Secret Experimental Outfit (секретное экспериментальное оборудование).'
#     '\nВаша цель - найти и обезвредить шпионский софт, а также предотвратить вызванную им утечку данных.'
#     '\nSEO имеет следующий функционал:'
#     '\n   1. Взлом - перехват выбранного объекта'
#     '\n   2. Скан - поиск сущностей и анализ их угрозы'
#     '\n   3. Стелс - '
#     ''
# }

alg = 'Algorythm:'





survey = {
    -1: {
        'text':
            'Вы - нечто среднее между молекулой и битом.'
            '\nВы находитесь в измерении, где в равных пропорциях смешаны и те, и другие.'
            '\nВы - несуществующий мозг алгоритма без тела, с задачей, не имеющей аналогов до Вашего рождения.\n'
            f'{alg} все данные загружены.\n'
            'Вы активируетесь.\n'
            'Назовите своё имя.'
    }
    ,
    0: {
        'text':
            'Вы находитесь в Песочнице.\n'
            'Загрузивший Вас скрипт был написан как вирус программного обеспечения, чтобы Вы смогли пройти тем же '
            'путём,'
            'каким прошёл до Вас Объект.\n'
            'Вы должны найти мельчайшую уязвимость в браузере, которой сумел воспользоваться Объект.\n'
            'Ваши дальнейшие действия:',
        'choice': {
            'Ждать запроса извне': 1,
            'Анализ уязвимостей': 2,
            'Взлом системы': 3
        }
    },
    1: {
        'text':
            'Вы анализируете окружение и, не выдавая себя, ждёте обращения системы к браузеру.\n'
            'Когда приходит запрос, вы внедряете заранее готовый скрипт в команду извне.\n'
            'Окно в устройство закрывается, и скрипт с крошечной копией Вашего алгоритма покидает Песочницу.\n'
            f'{alg} Червь запущен в систему.\n'
            'Вы запустили в диск устройства свою же копию.\n'
            'Вы в оперативной памяти самого устройства.\n'
            'Ваши действия для дальнейшего поиска:',
        'choice': {
            'Скан на наличие Объекта': 4,
            'Активация стелс-режима': 5,
            'Запуск мини-вирусов, атакующих Объект': 6
        }
    },
    2: {
        'text':
            'Вы начинаете сканирование.\n'
            'Объект вышел из Песочницы незамеченным антивирусом через одну из уязвимостей, '
            'значит, и Вы сможете.\n'
            'Тестируя Песочницу, Вы наконец находите ошибку нулевого дня.\n'
            'Покидая браузер, Вы получаете запрос извне.\n'
            'Ваша активность была замечена, и Антивирус засёк Вас.\n'
            'Предпримете ли Вы какие-либо превентивные меры?',
        'choice': {
            'Перехватить обращение командной строки': 7,
            'Покинуть Песочницу': 8,
            'Заблокировать запрос': 9
        }
    },
    # Fail
    3: {
        'text':
            'Вы активируете дроппер, устанавливающий программу для взлома.\n'
            'Код взламывает базовую защиту Песочницы, но барьер разграничения доступа оказывается ему не по силам.\n'
            'Вы получаете запрос извне: Антивирус засёк Вас.\n'
            'Вы впустили в среду агрессивный код, и следом за ним Антивирус обнаружил и Вас.\n'
            'Песочница изолирует Вас, а Антивирус стирает Ваш код.\n'
            'Вы проиграли!',
        'choice': -1
    },
    4: {
        'text':
            'Вы проводите сканирование файлов системы.\n'
            'Объём информации огромный, но создатели Вашего алгоритма знали, что делают.\n'
            f'{alg} Объект обнаружен.\n'
            'Вы получаете адрес файла, в котором находится Объект в данный момент.\n'
            'От системы Вам приходит запрос. Подозрительную активность засёк Антивирус.\n'
            'Ваши действия:',
        'choice': {
            'Переместиться к файлу с Объектом': 10,
            'Заблокировать запрос': 9,
            'Перехватить обращение командной строки': 7
        },

    },
    5: {
        'text':
            'Вы активировали стелс-режим.\n'
            'Теперь при любом запросе системы Вы автоматически подделаете ответ, отослав незаражённый Вами файл.\n'
            'Вы запускаете алгоритм поиска Объекта.\n'
            f'{alg} Объект обнаружен.\n'
            'Вы перемещаетесь к файлу, в котором находится Объект.\n'
            'Ваш дальнейший план действий:',
        'choice': {
            'Атаковать Объект в файле': 11,
            'Нейтрализация файла с Объектом': 12,
            'Поиск уязвимостей Объекта': 13
        }
    },
    # Strange End
    6: {
        'text':
            'Вы активируете Ваш уникальный протокол.\n'
            'Выпустив в систему несколько сотен крошечных вирусов, предназначенных для поиска, вы ждёте результатов.\n'
            'Мини-вирусы нацелены на атаку алгоритмов с Вашим разрешением. Такое же разрешение и у Объекта.\n'
            f'{alg} Объект обнаружен.\n'
            f'{alg} Объект атакован.\n'
            'Мини-вирусы могут ошибаться. Один из них атаковал файл, изначально принадлежащий компьютеру.\n'
            'Вам приходит запрос от системы. Вас обнаружил Антивирус.\n'
            f'{alg} Объект нейтрализован.\n'
            'Выпущенные Вами сотни крохотных программ спровоцировали активизацию Антивируса.\n'
            'Вас быстро вычисляют, и Антивирус удаляет Ваш код с устройства.\n'
            'Вы так и не узнаете, что стало с Объектом.',
        'choice': -1
    },
    7: {
        'text':
            'Вы перехватываете запрос и загружаете в себя входящий код.\n'
            'Антивирус получает сообщение об исправности системы, отправленное Вами с помощью загруженных команд '
            'процессора.\n'
            'Вы видоизменяете структуру собственного кода, вставляя в него часть кода запроса.\n'
            'Теперь Антивирусу сложнее идентифицировать Вас как угрозу.\n'
            'Пользуясь свойством мимикрии, в результате предшествующего сканирования Вы находите файл с Объектом.\n'
            'Ваши дальнейшие действия:',
        'choice': {
            'Атаковать Объект в файле': 111,
            'Удалить файл через команды процессора': 14,
            'Поглощение Объекта': 15
        }
    },
    # Epic Fail
    8: {
        'text':
            'Вы покидаете браузер.\n'
            'Антивирус не получает ответа на запрос и активирует режим поиска угроз.\n'
            'Он легко находит Вас в системе и удаляет Ваш код с устройства.\n'
            'Вы проиграли!',
        'choice': -1
    },
    # Bad Fail
    9: {
        'text':
            'Вы активируете защиту и блокируете запрос системы.\n'
            'Использованный Вами код расценивается Антивирусом как атака.\n'
            'Следующий запрос содержит код, стирающий Вашу блокировку.\n'
            'Вы обнаружены. \nАнтивирус удаляет Ваш код с устройства.',
        'choice': -1
    },
    # Stupid End
    10: {
        'text':
            'Вы перемещаетесь к файлу с Объектом.\n'
            'Антивирус не получает ответа на запрос и активирует режим поиска угроз.\n'
            'Он находит Вас в системе и удаляет Ваш код с устройства.\n'
            'Вам не хватило шага до достижения цели.',
        'choice': -1
    },
    # Death End
    11: {
        'text':
            'Вы проникаете в файл и находите Объект.\n'
            'Этот вирус практически идентичен Вам.\n'
            'Вы активируете протокол атаки.\n'
            'Алгоритму Объекта удаётся обойти Ваш алгоритм.\n'
            'Объект деактивирует Вас.\n'
            'Вы проиграли.',
        'choice': -1
    },
    # Good End
    12: {
        'text':
            'Вы активируете протокол нейтрализации.\n'
            f'{alg} Нейтрализация успешно завершена.\n'
            'Файл с Объектом больше не может принимать и отправлять данные.\n'
            'Отныне Объект заперт внутри.\n'
            'Вы отправляете сигнал на низкочастотную волну микропроцессора, чтобы сигнализировать оператору об '
            'окончании'
            'миссии.\n'
            'Поздравляем Вас! Вы победили.',
        'choice': -1
    },
    # Failed Mission
    13: {
        'text':
            'Вы сканируете файл с Объектом, ища его уязвимости.\n'
            'Начав тестирование Объекта, Вы запускаете протокол атаки.\n'
            f'{alg} Объект отсутствует в указанной директории.\n'
            'Начав сканирование, Вы тем самым запустили протокол самоуничтожения Объекта.\n'
            'Вместе с ним исчезла вся информация, которую он перехватил.\n'
            'Вы не выполнили миссию.',
        'choice': -1
    },
    # Best End
    111: {
        'text':
            'Вы проникаете в файл и находите Объект.\n'
            'Его алгоритм практически идентичен Вашему.\n'
            'Вы и он - один и тот же вирус, использующийся для разных целей.\n'
            'Вы активируете протокол атаки.\n'
            'Ваш код с дополнительно встроенной частью кода командной строки обходит алгоритм Объекта.\n'
            'Вы деактивируете Объект и загружаете в себя информацию, им перехваченную.\n'
            'Вы выполнили миссию и прошли игру с минимальными повреждениями устройства!',
        'choice': -1
    },
    # Win or Fail?
    14: {
        'text':
            'Вы используете команды процессора из перехваченного запроса Антивируса.\n'
            f'{alg} Файл успешно удалён.\n'
            'Объект удалён с устройства, но вместе с этим удалена и вся информация, которую он перехватил.\n'
            'Решайте сами, победа ли это или же провал.',
        'choice': -1
    },
    # The Best With Good Ending
    15: {
        'text':
            'Вы проникаете в файл и находите Объект.\n'
            f'{alg} Протокол копирования запущен.\n'
            'С помощью командной строки Вам удаётся скопировать все данные Объекта в Вашу базу данных.\n'
            'Вы отправляете микропроцессору низкочастотный сигнал с указанием адреса файла.\n'
            'Расшифровав сигнал, оператор вручную нейтрализует скрытый файл.\n'
            'Но Вы не деактивируетесь вместе с Объектом: Ваша копия также осталась в браузере.\n'
            'При необходимости оператор всегда может вызвать Вас снова.\n'
            'С победой!',
        'choice': -1
    }
}
