from shutil import get_terminal_size

from colorama import Fore, init

from passport import *

SIZE = get_terminal_size((80, 20))
init()

banner = """ 
███████████                                                          █████                           
░░███░░░░░███                                                        ░░███                            
 ░███    ░███  ██████    █████   █████  ████████   ██████  ████████  ███████      ████████  █████ ████
 ░██████████  ░░░░░███  ███░░   ███░░  ░░███░░███ ███░░███░░███░░███░░░███░      ░░███░░███░░███ ░███ 
 ░███░░░░░░    ███████ ░░█████ ░░█████  ░███ ░███░███ ░███ ░███ ░░░   ░███        ░███ ░███ ░███ ░███ 
 ░███         ███░░███  ░░░░███ ░░░░███ ░███ ░███░███ ░███ ░███       ░███ ███    ░███ ░███ ░███ ░███ 
 █████       ░░████████ ██████  ██████  ░███████ ░░██████  █████      ░░█████  ██ ░███████  ░░███████ 
░░░░░         ░░░░░░░░ ░░░░░░  ░░░░░░   ░███░░░   ░░░░░░  ░░░░░        ░░░░░  ░░  ░███░░░    ░░░░░███ 
                                        ░███                                      ░███       ███ ░███ 
                                        █████                                     █████     ░░██████  
                                       ░░░░░                                     ░░░░░       ░░░░░░   """

banner_width = len(banner.split('\n')[2])

if banner_width < SIZE.columns:
    print(f'{Fore.YELLOW}{banner}')
else:
    print(f'{Fore.YELLOW} [Passport.py]')

print('\n\n')

fio = input(f'{Fore.CYAN}😊 ФИО: {Fore.RED}')
birth_date = input(
    f'{Fore.CYAN}⏰ Дата Рождения (в формате DD.MM.YYYY): {Fore.RED}')
passport = input(
    f'{Fore.CYAN}🔐 Серия и номер паспорта (в формате СССС НННННН): {Fore.RED}')

print('')
print(f'{Fore.RED} Вот что удалось найти:')

serial = passport[0:4]

print('=' * int(SIZE.columns * 0.5))

print(f'{Fore.YELLOW}🗺️ Регион выдачи: {Fore.RED}{get_region(serial)}')
print(f'{Fore.YELLOW}🕰️ Примерная дата выдачи: {Fore.RED}{get_date_of_issue(serial, birth_date)}')

passport_for_inn = f'{passport[0:2]} {passport[2:4]} {passport[5:]}'


try:
    inn = get_inn(fio, birth_date, passport_for_inn)
    print(f'{Fore.YELLOW}🧾 ИНН: {Fore.RED}{inn}')
except Exception as e:
    inn = None
    print(f'{Fore.RED} Не удалось получить ИНН', e)

if inn:
    try:
        if is_self_employed(inn):
            print(f'{Fore.GREEN}🔨 Физ. лицо имеет статус самозанятого')
    except Exception as e:
        print(f'{Fore.RED} Не удалось статус самозанятости', e)
