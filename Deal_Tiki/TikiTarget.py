
from cmath import pi


class TikiTarget:
    def __init__(self,patternStr = "", categoryStr = ""):
        self.patternsString = patternStr
        self.patterns = self.__splitPattern()
        self.categoryUrl = categoryStr

    def info(self):
        return "Patterns: " + str(self.patterns) + " | category: " + self.categoryUrl

    def __splitPattern(self):
        newList = self.patternsString.split(',')
        i = 0
        while i < len(newList):
            newList[i] = newList[i].strip()
            i = i + 1
        return newList

    def getKeyword(self):
        keyword = ""
        for key in self.patterns:
            keyword = keyword + " " + key
        return keyword

    def getSearchLink(self, pageNum):
        return self.categoryUrl +"?q="+ self.getKeyword() + "&ref=categorySearch&page=" + str(pageNum)