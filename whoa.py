from os import system
print('Мы перешли в телеграм\nt.me/echoall_testbot:\n')
a = input('Открыть бота SMS KILLER да/нет >> ')
if a !='нет':
    system('termux-open-url https://t.me/echoall_testbot')
