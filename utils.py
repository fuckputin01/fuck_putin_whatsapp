import json
import configparser
from urllib.request import urlopen, Request

config = configparser.ConfigParser()
try:
    config.read('config.txt')
    base_url = config['DEFAULT']['base_url']
    api_key = config['DEFAULT']['api_key']
    headers = {'Authorization': f'Api-Key {api_key}'}
except:
    print("!!! REQUEST config.txt FILE WHERE YOU RECEIVED THIS PROJECT")
    exit(1)


def get_phone_numbers():
    url = base_url + '/api/phones'
    try:
        response = urlopen(Request(url, headers=headers))
    except Exception as e:
        print("Can't load more phones:", e)
        exit(2)
    data_json = json.load(response)

    return [{
        'phone_int': i.get('phone_int'),
        'name': i.get('name')
    } for i in data_json.get('results')]


def update_phone_timestamp(phone_int):
    url = base_url + f'/api/phones/{phone_int}'
    try:
        _ = urlopen(Request(url, headers=headers, data=b'', method='PUT'))
    except Exception as e:
        print("Can't report phone:", e)


def update_has_whatsapp(phone_int):
    url = base_url + f'/api/phones/{phone_int}'
    try:
        _ = urlopen(Request(url, headers=headers, data=b'', method='POST'))
    except Exception as e:
        print("Can't report phone:", e)


def get_texts():
    return [
        """
Заметили очереди у банкоматов и рост рубля?
Как с каждым днем войны с Украиной, твой кошелек опустошается?
Отказаться от поездок в Турцию и Барселону, от нового импортного телевизора или машины?
Продукты подорожают или вообще пропадут с полок магазинов, границы закроются.
Россию уже сейчас отрезают от внешнего мира, а значит ты не сможешь купить новый телефон, просто зайти в Appstore и GooglePlay.
А может, твой брат, муж или сын уже погиб на войне с Украиной? Оно тебе точно надо?
https://www.youtube.com/watch?v=J_IWfSh1GPM 

{time}
        """,
"""
Российская экономика стремительно разваливается.
Но это не ваша война. Не ваша земля. В Украине вас никто не ждет. Гражданское население ложится под танки, чтобы прекратить вашу оккупацию.
https://www.youtube.com/watch?v=J_IWfSh1GPM
Спаси Россию, верни русских солдат домой!
Спаси своих родных! Не дай им умереть на чужой земле.
Ищи https://t.me/rf200_now/ и 200rf.com.

{time}
""",
"""
Любишь отдыхать за границей?
С репарациями, которые вы будете платить Украине, не хватит даже на Сочи!
Полномасштабное нападение на Украину захлебывается - более 5 300 российских военных убиты или ранены // и более 400 русских военных сейчас в плену.
Ищи https://t.me/rf200_now/ и 200rf.com.
https://t.me/umer_RF

{time}
""",
"""
Заметили очереди у банкоматов и рост рубля?
Правительство закупило за миллионы танки, а у тебя скоро закончатся деньги на хлеб и лекарства.
Твой любимый чай и кофе скоро перестанут завозить в магазин.
Но танки горят. А может, в них горят твой брат, муж, друг?
Оно тебе точно надо?
https://www.youtube.com/watch?v=J_IWfSh1GPM
Ищи https://t.me/rf200_now/ и 200rf.com.
https://t.me/umer_RF

{time}
"""
    ]
