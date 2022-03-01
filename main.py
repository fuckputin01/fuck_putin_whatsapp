from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse
from selenium.webdriver.support import expected_conditions as EC


import time
from datetime import datetime

text = """Заметили очереди у банкоматов и рост рубля? Как с каждым днем войны с Украиной, твой кошелек опустошается? Готов ли ты платить за эту глупую войну? Продукты подорожают, границы закроются. Россию уже сейчас отрезают от внешнего мира, а значит ты не сможешь купить новый телефон, просто зайти в Appstore и GooglePlay. А может, твой брат, муж или друг уже погиб на войне с Украиной? Оно тебе точно надо? https://www.youtube.com/watch?v=J_IWfSh1GPM 

{time}
"""

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable	.")

verified_phones = open('verified.csv', 'a')
# verified_phones.write('Primary Phone\n')
delay = 30

with open('list.csv', 'r') as phones:
    phones.readline() # HEADER
    while 1:
        try:
            unparsed_phone = phones.readline()
            phone = ''.join(p for p in unparsed_phone if p.isnumeric())
        except:
            break

        print(f'Sending message to {phone}.')
        should_continue = False
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            url = f"https://web.whatsapp.com/send?phone={phone}&text={urllib.parse.quote_plus(text.format(time=current_time))}"
            driver.get(url)
            sent = False
            for j in range(1,5):
                if not sent:
                    try:
                        click_btn = WebDriverWait(driver, 5*j).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))
                    except Exception as e:
                        if 'неправильний' in driver.page_source or 'url is invalid' in driver.page_source:
                            should_continue = True
                            print(f"{phone} doesn't exist")
                            break
                        else:
                            print(f"Something went wrong..\n Failed to send message to: {phone}, retry ({j})")
                    else:
                        time.sleep(1)
                        click_btn.click()
                        sent = True
                        time.sleep(3)
                        print('Message sent to: ' + phone)
                        break
        except Exception as e:
            print('Failed to send message to ' + phone + str(e))
            time.sleep(0.5)

        if should_continue:
            continue

        print(unparsed_phone)
        verified_phones.write(f'{unparsed_phone}')

verified_phones.close()

driver.quit()
