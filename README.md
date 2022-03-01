#### About
Script for sending whatsapp via selenium 🇺🇦

#### Prerequirements
- Whatsapp account (can bye lifecell esim)
- Python3
- Venv

#### Installation
1. Clone repo to local
```
git clone https://github.com/fuckputin01/fuck_putin_whatsapp
or download zip from github
```

2. Install python venv
```
python3 -m venv /virtual/environment
source /virtual/environment/bin/activate
pip install -r requirements.txt
```

3  (optional) Update text in `main.py`
```
text = "Остановите Путина! Выходите на протест! Сохраните себя, страну и свою армию!"
```

3.5 ATTENTION: in case of wrong phone number, there is a popup in whatsapp.
If whatsapp language is not Ukrainian need to change `main.py`:
```
if 'неправильний' in driver.page_source:
```
change `неправильний` to whatever available at phone not available popup.
4. run `main.py`
```
python main.py
```

5. After login using QR in Google Chrome, press enter in terminal

6. Enjoy

### TODO
1. Add centralized DB for phones
2. Add more details to this README
3. Clean up the repo
4. Win the war and fuck off putin. 🇺🇦
