import sys
import time
import urllib.parse
from datetime import datetime
from random import choice

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from utils import update_phone_timestamp, get_phone_numbers, get_texts

CHROME_USER_DATA_ID=0
if len(sys.argv) == 2:
    try:
        CHROME_USER_DATA_ID=int(sys.argv[1])
    except:
        pass

options = webdriver.ChromeOptions()
options.add_argument(f'--user-data-dir=./User_Data{CHROME_USER_DATA_ID}')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visible.")

delay = 30

counter = 0
GO_SENDING = True
while GO_SENDING:
    phones_list_from_api = get_phone_numbers()
    for record in phones_list_from_api:
        current_time = datetime.now().strftime("%H:%M:%S")
        if 'To use WhatsApp on your computer:' in driver.page_source or 'Щоб використовувати WhatsApp на комп' in driver.page_source:
            print(f'[{current_time}] {counter} PHONE NUMBER IS BLOCKED BY WHATSAPP')
            driver.quit()
            exit(3)
        counter += 1

        try:
            phone = int(record.get('phone_int'))
        except:
            continue

        name = record.get('name')

        print(f'[{current_time}] {counter} Sending message to {phone}.')
        should_continue = False
        try:
            text = choice(get_texts()).format(time=current_time, name=name).strip()
            url = f"https://web.whatsapp.com/send?phone={phone}&text={urllib.parse.quote_plus(text.format(time=current_time))}"
            driver.get(url)
            sent = False
            for j in range(1,5):
                if not sent:
                    try:
                        click_btn = WebDriverWait(driver, j).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))
                    except Exception as e:
                        update_phone_timestamp(phone_int=phone)
                        if 'неправильний' in driver.page_source or 'url is invalid' in driver.page_source:
                            should_continue = True
                            print(f"[{current_time}] {counter} {phone} doesn't exist")
                            break
                        else:
                            print(f"    Something went wrong..\n    Failed to send message to: {phone}, retry ({j})")
                    else:
                        time.sleep(0.7)
                        click_btn.click()
                        sent = True
                        time.sleep(3.0)
                        print(f'[{current_time}] {counter} Message sent to:', phone)
                        break
        except Exception as e:
            print(f'[{current_time}] {counter} Failed to send message to:', phone, str(e))
            update_phone_timestamp(phone_int=phone)
            time.sleep(0.5)

        if should_continue:
            continue

        update_phone_timestamp(phone_int=phone)

driver.quit()
