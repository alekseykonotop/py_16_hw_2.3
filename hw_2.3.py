import chardet
import json
from pprint import pprint

# Пошаговое описание действий
# 1. Открыть в бинарном режиме, чтобы определить кодировку файла -- DONE
# 1.1 Еше раз открыть файл с учетом кодировки для  json.load -- DONE
# 2. Создать словарь, в котором будут накапливаться разбитые методом split строки из ключей
#    dict["rss"]["channel"]["description"]   description и title
#    Циклом for по dict["rss"]["channel"]["items"]["description"] и dict["rss"]["channel"]["items"]["title"]
#    dict["rss"]["channel"]["category"] и dict["rss"]["channel"]["title"]
# 3. Использовать код прошлой программы для определения топ 10 самых часто встречающихся
#    в новостях слов длиннее 6 символов для каждого файла


with open('json_files/{0}'.format('newsit.json'), 'rb') as f:
    data = f.read()
    result = chardet.detect(data)
    print('Используемая кодировка:', result['encoding'])
    # pprint(news)


with open('json_files/{0}'.format('newsit.json'), encoding=result['encoding']) as news_file:
    news = json.load(news_file)
    pprint(news["rss"]["channel"]["description"])  # Зная кодировку - получили читаемый текст. -- ALL OK
    print('=========')
    pprint((news["rss"]["channel"]["items"][0]["description"]))  # Обратился к ключу словаря списка "items" - All OK