import requests
import time
from proxymanager import ProxyManager
from multiprocessing import Pool
from multiprocessing import Process
import json
import multiprocessing
import random
import colorama
from colorama import Fore, Back, Style
from colorama import init
from pyfiglet import figlet_format
from termcolor import cprint
import string
import names
init()

with open('config.json') as f:
    config = json.load(f)

webhook = config['settings']['webhook']
firstname = config['settings']['firstname']
lastname = config['settings']['lastname']
domain = config['settings']['domain']

proxy_manager = ProxyManager('proxies.txt')

cprint(figlet_format('welcome,  {}'.format(firstname), font='doom'), attrs=['bold'])

start = input(Fore.GREEN + "Please click" + Fore.MAGENTA  + ' ENTER ' + Fore.GREEN + "to start getting your entries in.")

if start == "":
    print("Starting...")
else:
    exit()

proxiesLoaded = open("proxies.txt").read().splitlines()
#name = firstname + " " + lastname

def enter(domain, webhook):
    name = names.get_full_name()

    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://luckydraw.funko.com/',
    'Origin': 'https://luckydraw.funko.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    proxydict = proxy_manager.random_proxy()
    proxies = proxydict.get_dict()

    link = "https://play.powercore.io/lucky/V1/enter"

    letter1 = random.choice(string.ascii_letters)
    letter2 = random.choice(string.ascii_letters)
    letter3 = random.choice(string.ascii_letters)
    letter4 = random.choice(string.ascii_letters)
    letter5 = random.choice(string.ascii_letters)
    letter6 = random.choice(string.ascii_letters)
    letter7 = random.choice(string.ascii_letters)
    letter8 = random.choice(string.ascii_letters)
    letter9 = random.choice(string.ascii_letters)
    letter10 = random.choice(string.ascii_letters)

    email = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + letter8 + letter9 + letter10 + "@" + domain

    data = [
      ('email', email),
      ('name', name),
    ]

    try:
        response = requests.post("https://play.powercore.io/lucky/V1/enter", headers=headers, proxies=proxies, data=data, timeout=10)
    except:
        print(Fore.WHITE + Style.BRIGHT + "[{}]".format(str(time.ctime())) + Fore.RED + Style.NORMAL + "Failed to enter! Email: {} Name: {}".format(email, name))

    if response.status_code == 200:
        print(Fore.WHITE + Style.BRIGHT + "[{}]".format(str(time.ctime())) + Fore.GREEN + Style.NORMAL + " Successful entry! Email: {} Name: {}".format(email, name))

        data2 = {
            "embeds": [{
                "title": "Funko Luckydraw",
                "url": "https://luckydraw.funko.com/#/lucky",
                "color": 16777215,
                "description": "You will receive an email if you win a prize!",
                "footer": {
                  "icon_url": "https://i.imgur.com/zv41sNz.jpg",
                  "text": ('Powered by @hasterestocks | ' + str(time.ctime()))
                },
                "thumbnail": {
                  "url": "https://www.funko.com/static/media/funko-logo-white.09b7bdff.jpg"
                },
                "author": {
                  "name": "Successful Entry! (https://luckydraw.funko.com/#/lucky)",
                },
                "fields": [
                  {
                    "name": "Name",
                    "value": str(name),
                    "inline": True
                  },
                  {
                    "name": "Email",
                    "value": email,
                    "inline": True
                  }
                ]
              }
            ]
          }

        requests.post(webhook, json=data2)
    else:
        print(response.status_code)
        print(Fore.WHITE + Style.BRIGHT + "[{}]".format(str(time.ctime())) + Fore.RED + Style.NORMAL + "Failed to enter! Email: {} Name: {}".format(email, name))


if __name__ == '__main__':
    threads = []

    for proxy in proxiesLoaded:
        process = Process(target=enter, args=(domain, webhook))
        process.start()
        threads.append(process)

    for thread in threads:
        process.join()
