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


def get_encoding_type(folder, file_name):
    """Функция принимает имя папка и имя файла для
    определения кодировки, возвращает тип кодировки
    файла.
    """
    with open('{0}/{1}'.format(folder, file_name), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print('Используемая кодировка:', result['encoding'])
    return result['encoding']


def get_data_from_file(folder, file_name, encod_type):
    """Функция получает на вход строку folder и строку file_name
    и используемую кодировку encod_type.
    """
    # Чтение json файлов
    with open('{0}/{1}'.format(folder, file_name), encoding=encod_type) as news_file:
        news = json.load(news_file)

    # Чтение xml-файлов в разработке
    return news


def get_count_of_words(some_set, lst):
    """Функция получает на вход список и подсчитывает какое кол-во
    раз каждый элемент встречается в списке.
    Для этого создается множество не повторяющихся элементов списка.
    Возвращается новый список вида [['word1', quantity], ['word2', quantity]].
    """
    word_quantity_list = []
    for word in some_set:
        word_quantity_list.append([word, lst.count(word)])
    return word_quantity_list


def get_long_words_list(lst, x):
    """Функция принимает итеррируемых объект lst и целое число x.
    Возвращает новый список long_words состоящий из элементов переданного
    итеррируемого объекта lst, отвечающего условию len(элемент) > x.
    """

    long_words = []
    for word in lst:
        if len(word) > x:
            long_words.append(word)
    return long_words


def get_all_words(data_array):
    all_words_list = []
    if type(data_array) == dict:  # Задаем алгоритм получения слов при чтении файла json
        all_words_list += data_array['rss']['channel']['description'].split()
        for item in data_array['rss']['channel']['items']:
            all_words_list += item['description'].split()
            all_words_list += item['title'].split()
        all_words_list += data_array['rss']['channel']['category'].split()
        all_words_list += data_array['rss']['channel']['title'].split()
    return all_words_list  # Вернули полный список слов, разбитый методом split()


def quantity(lst):
    """Данная функция принимает список вида ['word1', quantity],
    состоящий их 2-х элементов и возвращает второй элемент,
    т.е. quantity.
    """
    return lst[1]


def run():
    data_way = {'json': {'folder': 'json_files', 'files': ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']},
                'xml': {'folder': 'xml_files', 'files': ['newsafr.xml', 'newscy.xml', 'newsfr.xml', 'newsit.xml']}
                }
    # Словарь для отладки программы, позже удалить
    # data_way = {
    #     'json': {'folder': 'json_files', 'files': ['newsit.json']},
    #     'xml': {'folder': 'xml_files', 'files': ['newsit.xml']}
    #     }

    print('Определим 10 самых высокочастотных слов.')
    world_length = int(input('Укажите количество символов в слове: '))
    choice = input('Какой тип файла вы хотите проанализировать (json / xml):')
    if choice in data_way:
        for file in data_way[choice]['files']:
            print('file:', file)
            encoding_type = get_encoding_type(data_way[choice]['folder'], file)  # Получаем значение кодировки для каждого файла
            data_from_file = get_data_from_file(data_way[choice]['folder'], file, encoding_type)  # Получили данные из файла в раскодированном виде
            all_words_list = get_all_words(data_from_file)  # Получим все слова из файла data_from_file
            long_words_list = get_long_words_list(all_words_list, world_length)  # Получили список слов, длиннее world_length
            set_words = set(long_words_list)  # Получили множество слов из файла
            word_quantity_list = get_count_of_words(set_words, long_words_list)  # Узнали сколько раз каждое слово встречается в тексте
            sorted_list = sorted(word_quantity_list, key=quantity, reverse=True)  # Отсортировали сложенные списки по значению второго элемента
            res_list = [i[0] for i in sorted_list[:10]]  # Список из 10 самых высокочастотных слов в файле
            print('10 самых высокочастотных слов длиннее {0} символов:\n'.format(world_length), res_list)
            print('===============\n')

    else:
        print('\n\tВНИМАНИЕ!\nНе верный выбор. Повторите.')

run()



