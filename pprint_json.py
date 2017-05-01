import json
import sys

def load_data(filepath):
    with open ( filepath , 'r',  encoding='cp1251') as f:
    	return json.load(f)


def pretty_print_json(data_json):
	pretty_json = json.dumps(data_json, indent=4, sort_keys=True, ensure_ascii=False )
	period=1500
	page_count = len(pretty_json)//period
	print( pretty_json[0:period] )
	get_page(pretty_json, page_count)


def get_page(pretty_json, page_count, period=1500):

	print('\nКоличество страниц в базе: ', page_count + 1, '\nВведите номер интересующей страницы: ')
	try:
		the_number_entered = input()
		number_of_page = int(the_number_entered)
	except ValueError:
		number_of_page = 0

	number_of_page -= 1 
	if number_of_page in range(page_count + 1):
		print ('\n', pretty_json[ number_of_page * period : number_of_page * period + period ])
		get_page(pretty_json, page_count)
	else:
		print ('в документе нет такой страницы')


def start_script(argv_list):
    if len(argv_list) < 2:
    	print('\nДанный скрипт принимает на вход путь до файла, в котором хранится json'
    		'и выводит его содержимое в консоль в удобном для чтения виде.\n'
    		'Для того чтоб узнать как работает программа введите:'
    		'python pprint_json.py --help или python3 pprint_json.py --help\n')
    	return None

    if argv_list[1] == '--help':
        print('\nЧтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <файл.json>\n'
              'Наример: python3 pprint_json.py data-2897-2016-11-23.json\n')
        return None

    filepath = argv_list[1]
    data_json = load_data(filepath)
    pretty_print_json(data_json)


if __name__ == '__main__':
	argv_list = sys.argv
	start_script(argv_list)