
import requests, os, sys
from time import sleep
try:
    from bs4 import BeautifulSoup as bs
except:
    os.system('pip3 install bs4')
dataAV = []
RESET = '\033[0m'
UNDERLINE = '\033[04m'
GREEN = '\033[32m'
YELLOW = '\033[93m'
RED = '\033[31m'
CYAN = '\033[36m'
BOLD = '\033[01m'
URL_L = '\033[36m'
LI_G = '\033[92m'
F_CL = '\033[0m'
def num(number):
    try:
        num_P_S = requests.post('https://htmlweb.ru/geo/api.php?json&telcod='+ str(number))
        num_P = num_P_S.json()

        print(f'{YELLOW}{BOLD}[~] {LI_G}Поиск данных... {RESET}\n')
        try:
            country = num_P['country']
            for a in range(1):
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Страна:{F_CL} {country["name"]}, {country["fullname"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Стране не найдены{RESET}'); pass

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Код страны:{F_CL} {country["country_code3"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Коде страны не найдены{RESET}'); pass

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Код номера:{F_CL} {str(country["telcod"])}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Коде номера не найдены{RESET}'); pass

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Длина номера:{F_CL} {str(country["telcod_len"])}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Длине номера не найдены{RESET}'); pass

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Локация:{F_CL} {country["location"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Локации не найдены{RESET}'); pass

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Язык:{F_CL} {country["lang"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Языке не найдены{RESET}');
        except:
            pass


        try:
            region = num_P['region']
            for reg in region:
                endIndex = region['name'].split()

                try:
                    if endIndex[1] == 'край': print(f'{YELLOW}{BOLD}[+] {LI_G}Край:{F_CL} {region["name"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Крае не найдены{RESET}')

                try:
                    if endIndex[1] == 'область':
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Область:{F_CL} {region["name"]}{RESET}')
                    else:
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Название:{F_CL} {region["name"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные об Области не найдены{RESET}')

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Округ:{F_CL} {region["okrug"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные об Округе не найдены{RESET}')

                break
        except:
            print(f'{YELLOW}{BOLD}[!] {RED}Данные Область/Край не найдены{RESET}'); pass

        try:
            capital = num_P['capital']
            for c in capital:
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Столица:{F_CL} {capital["name"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные об Сталице не найдены{RESET}')

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Код домашнего номера столицы:{F_CL} +{str(capital["telcod"])}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Домашнем номере не найдены{RESET}')
                break
        except:
            print(f'{YELLOW}{BOLD}[!] {RED}Данные Код/Столица не найдены{RESET}'); pass

        try:
            data = num_P['0']
            for c in data:
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Город:{F_CL} {data["name"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Городе не найдены{RESET}')

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Район:{F_CL} {str(data["rajon"])}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Районе не найдены{RESET}')

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Оператор:{F_CL} {data["oper_brand"]}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные об Операторе не найдены{RESET}')

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Номера:{F_CL} {str(data["def"])}{RESET}')
                except:
                    print(f'{YELLOW}{BOLD}[!] {RED}Данные о Номерах оператора не найдены{RESET}')

                break
        except:
            print(f'{YELLOW}{BOLD}[!] {RED}Данные Город/Оператор не найдены{RESET}'); pass

        if number[0] == '7' and len(number) > 9:
            if num_P['limit'] == 0:
                pass
            else:

                name = []
                dataAV = []
                dataOB = []

                review_ph = requests.get(f'http://phoneradar.ru/phone/{number}')
                try:
                    reviews_rev = bs(review_ph.text, 'html.parser').find('div', class_='alert alert-danger').text.strip()
                except KeyboardInterrupt:
                    sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
                except:
                    try:
                        reviews_rev = bs(review_ph.text, 'html.parser').find('div', class_='alert alert-info').text.strip()
                    except:
                        reviews_rev = 'Рейтинг номера не определен, отзывов о номере еще нет'
                print(f'{YELLOW}{BOLD}[+] {LI_G}Рейтин: {F_CL}{reviews_rev}{RESET}')

                try:
                    def get_url_name_avito(number):
                        resAV = requests.get('https://mirror.bullshit.agency/search_by_phone/' + str(number))
                        contentAV = bs(resAV.text, 'html.parser')
                        h1 = contentAV.find('h1')
                        if h1 == True:
                            count = 0
                            h1T = h1.text.replace("  ", "")
                            print(f'\n{YELLOW}{BOLD}[~] {LI_G}Поиск данных по Авито: {RESET}')
                            print(f'{YELLOW}{BOLD}[~] {LI_G}Авито: {F_CL}{h1T}{RESET}')
                            print(f'{YELLOW}{BOLD}[+] {LI_G}----------------------------------------- {RESET}\n')
                            for oBV in contentAV.find_all(['h4', 'span']):
                                print(f'{YELLOW}{BOLD}[+] {LI_G}{oBV.text}{RESET}')
                                dataOB.append(oBV.text)

                            with open('dataFile.txt', 'a', encoding='utf-8') as f:
                                for data in dataOB:
                                    f.write('[-] ' + data + '\n')

                            for url in contentAV.find_all(['a']):
                                count += 1
                                user_link = url['href']
                                try:
                                    avito_url = requests.get('https://mirror.bullshit.agency' + user_link)
                                    content = bs(avito_url.text, 'html.parser')
                                    url = content.find(['a'])

                                    linkAV = url['href']
                                    print(f'{YELLOW}{BOLD}[{count}] {URL_L}{UNDERLINE}{linkAV}{RESET}')

                                    u_name = bs(avito_url.text, 'html.parser')
                                    nameU = u_name.find('strong')

                                    name.append(nameU.text)
                                    dataAV.append(f'[{count}] {linkAV}')

                                except:
                                    print(f'{YELLOW}{BOLD}[{count}] {RED}{UNDERLINE}{user_link}{RESET}')
                                    continue
                            if not name:
                                pass
                            else:
                                print('\n' + YELLOW + BOLD + '[+]' + LI_G + ' Все имена с ссылок: ' + RESET + ', '.join(name))
                            get_url_name_avito(number)
                except:
                    pass
    except Exception as e:
        print(e)