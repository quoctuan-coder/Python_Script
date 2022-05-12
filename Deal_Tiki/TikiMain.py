import requests
import time
from TikiDisplayThread import TikiDisplayThread
from TikiItem import TikiItem
from TikiHelper import *
from TikiTarget import TikiTarget
from TikiHunterThread import TikiHunterThread
from bs4 import BeautifulSoup


TARGET_FILE = 'target_list.txt'

targets = getTargetsFromFile(TARGET_FILE)
threads = []
displayThread = TikiDisplayThread()

for t in targets:
    hunter = TikiHunterThread(t)
    hunter.start()
    threads.append(hunter)
    displayThread.addHunter(hunter)

displayThread.start()
for t in threads:
    t.join()



print('=========End=========')
