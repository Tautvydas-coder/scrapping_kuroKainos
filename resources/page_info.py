import requests
from resources.variables import *

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}

page = requests.get(url=URL, headers=HEADERS)
# page = requests.get(url='https://www.messenger.com')
