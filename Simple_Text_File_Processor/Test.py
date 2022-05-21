tr = 'L1B1S01.srt'

def getNumberOfName(fileTxtName):
    tmp = fileTxtName.split('.')[0]
    numL = tmp[1]
    numB = tmp[3]
    if tmp[5] == '0':
        numS = tmp[6]
    else:
        numS = tmp[6:7]
    return [numL,numB,numS]
ls = getNumberOfName(tr)

print('{} - {} - {}'.format(ls[0],ls[1],ls[2]))