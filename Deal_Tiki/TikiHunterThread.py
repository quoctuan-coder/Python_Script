# -*- coding: utf-8 -*-
from threading import Thread
from TikiHelper import convertToPrice
from TikiTarget import TikiTarget
from TikiItem import TikiItem
from bs4 import BeautifulSoup
import requests
import time

class TikiHunterThread(Thread):
    MAX_PAGE = 1
    
    def __init__(self,target):
        Thread.__init__(self)
        self.target = target
        self.bestItem = None
        self.name = target.getKeyword()

    def __findBestItem(self):
        for target in self.targets:
            headers = {'User-Agent':'Go to | https://www.whatismybrowser.com/detect/what-is-my-user-agent |, Get your User-Agent and paste here'}
            searchLink = target.getSearchLink(1)
            response = requests.get(searchLink,headers=headers)
            if (response.status_code != 200):
                print('Error')
            else:
                bsoup = BeautifulSoup(response.text,'lxml')
                listElement = bsoup.findAll('a',{'class':'product-item'})
                i = 0
                for e in listElement:
                    print(e.get_text().find('Đã hết hàng'))
                    if (int (e.get_text().find('Đã hết hàng')) >= 0 or int (e.get_text().find('Ngừng kinh doanh')) >= 0):
                        continue
                    
                    newItem = TikiItem()
                    newItem.title = (e.find('div',{'class':'name'}).text)
                    newItem.url = "https://tiki.vn" + e.get("href")
                    span = e.find('div',{'class':'price-discount__price'})
                    newItem.price = convertToPrice(span.text)
                    span = e.find('div',{'class':'price-discount__discount'})
                    if self.bestItem == None:
                        self.bestItem = newItem
                    else:
                        if (newItem.price < self.bestItem.price):
                            self.bestItem = newItem
                    i = i + 1

    def run(self):
        print ('Start Thread: '+ self.name)
        while True:
            try:
                self.__findBestItem()
            except:
                print("something wrong ")
            time.sleep(2)
        print('End Thread: '+ self.name)

                    

        