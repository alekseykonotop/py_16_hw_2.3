import json
import chardet
from pprint import pprint

# Пошаговое описание действий
# 1. Открыть в бинарном режиме, чтобы определить кодировку файла
# 1.1 Превратить данные в текст и передать в json.load
# 2. Создать словарь, в котором будут накапливаться разбитые методом split строки из ключей
#    dict["rss"]["channel"]["description"]   description и title
#    Циклом for по dict["rss"]["channel"]["items"]["description"] и dict["rss"]["channel"]["items"]["title"]
#    dict["rss"]["channel"]["category"] и dict["rss"]["channel"]["title"]
# 3. Использовать код прошлой программы для определения топ 10 самых часто встречающихся
#    в новостях слов длиннее 6 символов для каждого файла
#
#
#
#
#
#
#
#
#


with open('json_files/{0}'.format('newsit.json')) as news_file:
    news = json.load(news_file)
    result = chardet.detect(news)
    print('Используемая кодировка:', result['encoding'])
    # pprint(news)