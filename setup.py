import pip

pkglist = ['json', 'colorama', 'pyfiglet', 'termcolor', 'requests', 'bs4', 'proxy-manager', 'asyncio', 'pyppeteer', 'urllib3', 'selenium', 'string', 'names', 'random']

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Accept' : 'application/json',
    'dnt' : '1',
    'Accept-encoding' : 'gzip, deflate, br',
    'Accept-language' :	'en-US,en;q=0.9'
}

start = input("Please click ENTER to start first-time setup. ")

if start == "":
    print("Starting...")
else:
    exit()

def install(package):
    pip.main(['install', package])

for package in pkglist:
    install(package)

import colorama
from colorama import Fore, Back, Style
from colorama import init
from pyfiglet import figlet_format
from termcolor import cprint
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup as bs
from proxymanager import ProxyManager
import time
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing
import random
import asyncio
import pyppeteer
from pyppeteer import launch
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init()

def splash(splashurl, taskname):
    print(Fore.WHITE + Style.BRIGHT + "[{}, {}]".format(taskname, str(time.ctime())) + Fore.MAGENTA + Style.NORMAL + " Performing First Time Setup...")
    print(Fore.WHITE + Style.BRIGHT + "[{}, {}]".format(taskname, str(time.ctime())) + Fore.GREEN + Style.NORMAL + " Complete! You can now use enter.py")


splashurl = "http://hasterestocks.io/splash"
taskname = "setup"
splash(splashurl, taskname)
