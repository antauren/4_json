import json
import sys
import os.path

def load_data(filepath):
    with open ( filepath , 'r',  encoding='cp1251') as f:
    	return json.load(f)


def pretty_print_json(data_json):
	print( json.dumps(data_json, indent=4, sort_keys=True, ensure_ascii=False ))


def start_script(argv_list):
    if len(argv_list) < 2:
    	print('\nДанный скрипт принимает на вход путь до файла, в котором хранится json '
    		'и выводит его содержимое в консоль в удобном для чтения виде.\n'
    		'Для того чтоб узнать как работает программа введите: '
    		'python pprint_json.py --help или python3 pprint_json.py --help\n')
    	return None

    if argv_list[1] == '--help':
        print('\nЧтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <файл.json>\n'
              'Наример: python3 pprint_json.py data-2897-2016-11-23.json\n')
        return None

    if not os.path.exists(argv_list[1]):
        print('Ошибка: программа не может найти файл\n'
              'Воспользуйтесь помощью (--help)')
        return None

    filepath = argv_list[1]
    data_json = load_data(filepath)
    pretty_print_json(data_json)


if __name__ == '__main__':
	argv_list = sys.argv
	start_script(argv_list)