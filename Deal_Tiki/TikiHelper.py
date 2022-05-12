#-*- coding: utf-8 -*-
from TikiTarget import TikiTarget
from sys import platform

def getTargetsFromFile(fileName):
    if platform == 'win32':
        targetFile = open(fileName,'r',encoding='utf8')
    else:
        targetFile = open(fileName,'r')

    lines = targetFile.readlines()
    targetFile.close()
    targets = []
    n = len(lines)
    print('n = ' + str(n))
    i = 0
    while i < n:
        newTarget = TikiTarget(lines[i].strip(),lines[i+1].strip())
        
        targets.append(newTarget)
        i = i + 2

    return targets

def convertToPrice(strPrice):
    strPrice = strPrice.replace('.','')
    strPrice = strPrice.replace('đ','')
    return strPrice

def convertToDiscount(strDiscount):
    strDiscount = strDiscount.replace('-','')
    strDiscount = strDiscount.replace('%','')
    return (int(strDiscount))

