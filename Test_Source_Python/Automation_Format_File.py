import re


class SourceCode():
    def __init__(self):
        self.pathFileSource = 'Test.py'
        self.pathFileOutput = 'TestOut.py'
        self.listSourceCode = []
        self.lineCode = ''

    #    a   = 5 -> a = 5
    def replaceSpaceDeclare(self):
        self.lineCode = re.sub(' *= *', ' = ', self.lineCode)

    def addInformation(self):
        author = '# Author: TuanTran\n'
        github = '# Github: https://github.com/quoctuan-iot\n'
        email = '# Email: quoctuan.iot@gmail.com\n'
        listInfor = [author, github, email]
        for cnt, item in enumerate(listInfor):
            self.listSourceCode.insert(cnt, item)

    def removeEndSpaces(self):
        self.lineCode = re.sub('[^a-zA-Z0-9_] *[\\n]', '', self.lineCode)

    def removeWhitespaceExpressions():
        pass

    def removeWhitespacedeclare(string):
        pass

    def checkFunction():
        pass

    def readCode(self):
        self.readLineSource = open(self.pathFileSource).readlines()
        for cnt, self.line in enumerate(self.readLineSource):
            self.listSourceCode.append(self.line)
            

    def writeCode(self):
        fileWrite = open(self.pathFileOutput, 'w')
        for self.lineCode in self.listSourceCode:

            self.replaceSpaceDeclare()
            self.removeEndSpaces()

            fileWrite.write(self.lineCode)

        fileWrite.close()


def main():
    sourceCode = SourceCode()
    sourceCode.readCode()
    sourceCode.addInformation()
    

    sourceCode.writeCode()


main()
