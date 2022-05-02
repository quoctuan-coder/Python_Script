import os
import Ruledata
import glob
import enchant
import re
import sys

MSN = 'ADC'
# MSN = sys.argv[1]

msn = MSN.lower()
path = f"D:\\00_Repo\\00_X2x_Trunk\\internal\\Module\\{msn}\\06_CD\\01_WorkProduct\\generator_cs"
Dict_US = enchant.Dict("en_US") #Create Dict to check word
Dict_User = Ruledata.CodingRule_CSharp["Dict"] #Create Dict of user
# print (Dict_User)
for i in Dict_User:
    Dict_US.add(i)

path_total = []
path_total.append(glob.glob(os.path.join(path, "*")))
path_total.append(glob.glob(os.path.join(path, "*", "*")))
path_total.append(glob.glob(os.path.join(path, "*", "*", "*")))
path_total.append(glob.glob(os.path.join(path, "*", "*", "*", "*")))

class CodingRule():
    def __init__(self, pathFile, link):
        self.location = link
        self.dataJson = Ruledata.CodingRule_CSharp
        self.pathFile = pathFile
        basename = os.path.basename(self.pathFile)
        self.nameFile = os.path.splitext(basename)[0]
        with open(self.pathFile, 'r', errors="ignore") as File:
            self.content = File.read()

    def Check_Line_Number(self, var):
        with open(self.pathFile, 'r', errors="ignore") as inputFile:
            for line_i, line in enumerate(inputFile, 1):
                if (var in line):
                    return line_i
    
    def Check_Camel(self, var):
        variable = []
        check = True
        k = 0
        i = len(var)
        while(i > k):
            name_t = var[k:i+1]
            if(Dict_US.check(name_t) == True):
                if (len(name_t) > 1):
                    variable.append(name_t)
                    k += len(name_t)
                    i = len(var)
                else:
                    i -= 1
            else:
                i -= 1
        #Check_Camel
        for i in range(0, len(variable)):
            if(i == 0):
                if(variable[i][0].isupper()):
                    check *= False
            else:
                if(variable[i][0].islower()):
                    check *= False
        return check

    def Check_Spell(self, var):
        variable = []
        check = True
        k = 0
        i = len(var)
        while(i > k):
            name_t = var[k:i]
            if(Dict_US.check(name_t) == True):
                variable.append(name_t)
                # print(name_t)
                k += len(name_t)
                i = len(var)
            else:
                i -= 1
        # print(variable)
        for i in range(0, len(variable)):
            if(len(variable[i]) < 2):
                check *= False
        return check

    def Check_Pascal(self, var):
        variable = []
        check = True
        k = 0
        i = len(var)
        while(i > k):
            name_t = var[k:i+1]
            # print(name_t)
            # print(Dict_US.check(name_t))
            if(Dict_US.check(name_t) == True):
                if (len(name_t) > 1):
                    variable.append(name_t)
                    # print(name_t)
                    k += len(name_t)
                    i = len(var)
                else:
                    i -= 1
            else:
                i -= 1
        # print(variable)
        #Check_Pascal
        for i in range(0, len(variable)):
            if(variable[i][0].islower()):
                check *= False
        return check

    #2.1 FILE NAMING
    def Check_File_Name(self):
        nameFile = self.nameFile
        #Name_File_001
        if(nameFile[0].isdecimal()):
            print(f'{self.location}\{self.nameFile}\nName_File_001:\nNG: {self.dataJson["File_Name"][1]["message"]}')
        # else:
        #     print('OKE1')

        #Name_File_002
        if((len(nameFile)) > self.dataJson["File_Name"][2]["Rule"]):
            print(f'{self.location}\{self.nameFile}\nName_File_002:\nNG: {self.dataJson["File_Name"][2]["message"]}')
        # else:
        #     print('OKE2')

        #Name_File_004
        pattern = r'(.*interface)'
        check = True
        regex = re.findall(pattern, self.content)
        if(regex != []):
            for i in range(len(regex)):
                if('//' not in regex[i]):
                    check *= False
        else: 
            check = True
        if (check == 0):
            if(nameFile[0] != 'I'):
                print(f'{self.location}\{self.nameFile}\nName_File_004:\nNG: {self.dataJson["File_Name"][4]["message"]}')
        #     else: 
        #         print('OKE4')
        # else:
        #     print('OKE4')

        #Name_File_003
        num = len(MSN)
        if(check == 0):
            if (nameFile[1:num+1] != MSN.capitalize()):
                print(f'{self.location}\{self.nameFile}\nName_File_003:\nNG: {self.dataJson["File_Name"][3]["message"]}')
            # else:
            #     print('OKE3')
        else:
            if (nameFile[:num] != MSN.capitalize()):
                print(f'{self.location}\{self.nameFile}\nName_File_003:\nNG: {self.dataJson["File_Name"][3]["message"]}')
            # else:
            #     print('OKE3')

        #Name_File_005
        if(check == 0):
            name = nameFile[1:].split('.')
        else:
            name = nameFile.split('.')
        result = True
        for j in range(len(name)):
            k = 0
            i = len(name[j])
            while(i > k):
                name_t = name[j][k:i+1]
                # print(Dict_US.check(name_t))
                if(Dict_US.check(name_t) == True):
                    if (len(name_t) > 1):
                        # print(name_t)
                        k += len(name_t)
                        i = len(name[j])
                        result = True
                    else:
                        result = False
                        i-= 1
                else:
                    result = False
                    i -= 1
        if(result == 0):
            print(f'{self.location}\{self.nameFile}\nName_File_005:\nNG: {self.dataJson["File_Name"][5]["message"]}')
        # else:
        #     print('OKE5')

    #2.2 VARIABLE NAMING
    def Check_Variable_Name(self):
        #Name_Var_001
        line = []
        var_total =[] #for 003 and 005
        regex_total = []
        pattern = r'(private (.*) ([a-zA-Z0-9_]*) = .*;)'
        regex = (re.findall(pattern, self.content))
        # print(regex)
        if(regex != []):
            for i in range(0, len(regex)):
                regex_total.append(regex[i])
        pattern = r'(protected (.*) ([a-zA-Z0-9_]*) = .*;)'
        regex = (re.findall(pattern, self.content))
        if(regex != []):
            for i in range(0, len(regex)):
                regex_total.append(regex[i])
        vars_type = []
        vars_loca = []
        check = True
        for i in range(0, len(regex_total)):
            var = regex_total[i][2]
            type_t = regex_total[i][1]
            var_total.append(var)
            vars_type.append(type_t)
            vars_loca.append(regex_total[i][0])
            if(self.Check_Camel(var) == False):
                line.append(self.Check_Line_Number(regex_total[i][0]))
                check *= False
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Var_001:\nNG: {self.dataJson["Variable_Name"][1]["message"]}')
        # else:
        #     print('OKE1')

        #Name_Var_002
        line = []
        pattern = r'(public (.*) ([a-zA-Z0-9_]*) = .*;)'
        regex = (re.findall(pattern, self.content)) 
        check = True
        # print(regex)
        for i in range(0, len(regex)):
            var = regex[i][2]
            type_t = regex[i][1]
            var_total.append(var)
            vars_type.append(type_t)
            vars_loca.append(regex[i][0])
            if(self.Check_Pascal(var) == False):
                line.append(self.Check_Line_Number(regex[i][0]))
                check *= False
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Var_002:\nNG: {self.dataJson["Variable_Name"][2]["message"]}')
        # # else:
        # #     print('OKE2')

        #Name_Var_003
        # var_total
        # print(var_total)
        line = []
        check = True
        for i in range(len(var_total)):
            if(Dict_US.check(var_total[i]) == True):
                check *= False
                line.append(self.Check_Line_Number(vars_loca[i]))
                # print(var_total[i])
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Var_003:\nNG: {self.dataJson["Variable_Name"][3]["message"]}')
        # else:
        #     print('OKE3')
        
        # #Name_Var_004


        #Name_Var_005
        check = True
        line = []
        var_t = [] # ['strong', 'hello', 'Config', 'Comment']
        # vars_type = ['string', 'int', 'List<AdcConfigSet>', 'int']
        for i in range(len(var_total)):
            var = var_total[i]
            if('const' not in vars_loca[i]):
                if('_' in var):
                    if(var.isupper() == False):
                        check *= False
                        line.append(self.Check_Line_Number(vars_loca[i]))
            #get first name of variable
            k = 0
            i = len(var)
            while(i > k):
                name_t = var[k:i+1]
                if(Dict_US.check(name_t) == True):
                    if (len(name_t) > 1):
                        var_t.append(name_t)
                        break
                    else:
                        i -= 1
                else:
                    i -= 1
        for i in range(0, len(var_t)):
            if (var_t[i].lower() == vars_type[i].split('<')[0].lower()):
                print(var_t[i])
                check *= False
                line.append(self.Check_Line_Number(vars_loca[i]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Var_005:\nNG: {self.dataJson["Variable_Name"][5]["message"]}')
        # # else:
        # #     print('OKE5')

    #2.3 METHOD NAMING
    def Check_Method_Name(self):
        #Name_Method_001 
        line = []
        pattern = r'((public|protected).+\()'
        regex_1 = (re.findall(pattern, self.content))   #[('protected AdcU2xIntermediate() : this(', 'protected'), 
        #('public AdcU2xIntermediate(', 'public')]
        # print(regex_1)
        methods = [] #['protected', 'AdcU2xIntermediate()', ':', 'this(']
        methods_total = []
        check = True
        for i in range(0, len(regex_1)):
            methods = regex_1[i][0].split()
            # print(methods)
            if(':' in methods):
                tempt = methods[len(methods)-3] #pick method
                method = tempt[:len(tempt)-2] #remove ()
                methods_total.append(method)
            else:
                tempt = methods[len(methods)-1]
                method = tempt[:len(tempt)-1] #remove (
                methods_total.append(method)
            # print(method) #AdcU2xIntermediate
            if(self.Check_Pascal(method) == False):
                check *= False
                line.append(self.Check_Line_Number(method))

        pattern = r'(private.+\()'
        regex_1 = re.findall(pattern, self.content)
        # print(regex_1) #['private AdcU2xIntermediate() : this(', 'private AdcU2xManager(']
        methods = []
        check = True
        for i in range(0, len(regex_1)):
            methods = regex_1[i].split()
            # print(methods) #['private', 'AdcU2xIntermediate()', ':', 'this(']
            if(':' in methods):
                tempt = methods[len(methods)-3] #pick method
                method = tempt[:len(tempt)-2] #remove ()
                methods_total.append(method)
            else:
                tempt = methods[len(methods)-1]
                method = tempt[:len(tempt)-1] #remove (
                methods_total.append(method)
            # print(method) #AdcU2xIntermediate
            if(self.Check_Camel(method) == False):
                check *= False
                line.append(self.Check_Line_Number(method))
        # print(methods_total) #['AdcU2xHunt', 'adcU2xIntermediate', 'adcU2xManager']
        for method in methods_total:
            if ('_' in method):
                check *= False
                line.append(self.Check_Line_Number(method))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Method_001 :\nNG: {self.dataJson["Method_Name"][1]["message"]}')
        # else:
        #     print('OKE1')

    #2.4 TYPE NAMING
    def Check_Type_Name(self):
        #Name_Type_003
        line = []
        pattern = r'.*\n.* enum .*'
        regex_1 = (re.findall(pattern, self.content))
        enum = ''
        enums_total = []
        check = True
        #check pascal
        for i in range(0, len(regex_1)):
            enums = regex_1[i].split()
            # print(enums)
            tempt = enums[len(enums)-1] #pick method
            if ('{' in tempt):
                enum = tempt[:len(tempt)-1] #remove ()
            else:
                enum = tempt
            if(self.Check_Pascal(enum) == False):
                check *= False
                line.append(self.Check_Line_Number(enum))
            #check plural for flag
            if('[Flags]' in enums):
                # print(enum[:len(enum)-1])
                # check *= Dict_US.check(enum[:len(enum)-1])
                if(enum[len(enum)-1] == 's'):
                    if (Dict_US.check(enum[:len(enum)-1]) == True):
                        # print (enum[:len(enum)-1])
                        check *= True
                    else:
                        # print (enum[:len(enum)-1])
                        check *= False
                        line.append(self.Check_Line_Number(enum[:len(enum)-1]))
                else:
                    check *= False
                    line.append(self.Check_Line_Number(enum[:len(enum)-1]))

            #check singular
            else:
                # print (enum[len(enum)-1])
                if(enum[len(enum)-1] == 's'):
                    if (Dict_US.check(enum[:len(enum)-1]) == False):
                        # print (enum[:len(enum)-1])
                        check *= True
                    else:
                        # print (enum[:len(enum)-1])
                        line.append(self.Check_Line_Number(enum[:len(enum)-1]))
                        check *= False
                else:
                    check *= True

            #Check "Enum" and "Flag" suffix or prefix
            if('Enum' in enum):
                check *= False
                line.append(self.Check_Line_Number(enum))
            if('Flag' in enum):
                check *= False
                line.append(self.Check_Line_Number(enum))

        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Type_003 :\nNG: {self.dataJson["Type_Name"][3]["message"]}')
        # else:
        #     print('OKE3')

    #2.6 PARAMETER NAMING
    def Check_Param_Name(self):
        #Name_Param_001
        line = []
        pattern = r'param name=\".+\"'
        regex = (re.findall(pattern, self.content))
        # print(regex)
        param = ''
        params = []
        check = True
        #check pascal
        for i in range(0, len(regex)):
            params = regex[i].split('"')
            param = params[len(params)-2]
            #Check_camel
            if(self.Check_Camel(param) == False):
                check *= False
                line.append(self.Check_Line_Number(param))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Param_001 :\nNG: \n{self.dataJson["Param_Name"][1]["message"]}')
        # else:
        #     print('OKE1')

    #2.11 CLASS NAMING
    def Check_Class_Name(self):
        #Name_Class_001
        line = []
        pattern = r'class (.*) ?\n?:?.*?\n?\{'
        regex = re.findall(pattern, self.content)
        check = True
        # print(regex)
        for i in range(0, len(regex)):
            class_n = regex[i].split(':')[0].strip(' ')
            check *= self.Check_Pascal(class_n)
            if('_' in class_n):
                check *= False
                line.append(self.Check_Line_Number(class_n))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Class_001 :\nNG: {self.dataJson["Class_Name"][1]["message"]}')
        # else:
        #     print('OKE1')

    #2.12 EVENT NAMING
    def Check_Event_Name(self):
        pattern = r'delegate void (.*)\((.*), (.*)\);'
        regex = re.findall(pattern, self.content)
        check = True
        line = []
        # print(regex)
        for i in range(0, len(regex)):
            event = regex[i]
            if('EventHandler' not in event[0]):
                check *= False
                line.append(self.Check_Line_Number(event[0]))
            if('sender' not in event[1]):
                check *= False
                line.append(self.Check_Line_Number(event[1]))
            if('e' not in event[2]):
                check *= False
                line.append(self.Check_Line_Number(event[2]))
            if('EventArgs' not in event[2]):
                check *= False
                line.append(self.Check_Line_Number(event[2]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Event_001 :\nNG: {self.dataJson["Event_Name"][1]["message"]}')
        # else:
        #     print('OKE1')

    #2.13 FIELD NAMING
    def Check_Field_Name(self):
        check = True
        line = []
        pattern = r'((protected|public) static .* ([a-zA-Z0-0_]*));'
        regex = re.findall(pattern, self.content)
        # print(regex)
        for i in range(0, len(regex)):
            field = regex[i][2]
            if(';' not in regex[i][0]):
                if(self.Check_Pascal(field) == False):
                    check *= False
                    line.append(self.Check_Line_Number(regex[i][0]))
        
        pattern = r'(private static .* ([a-zA-Z0-0_]*));'
        regex = re.findall(pattern, self.content)
        for i in range(0, len(regex)):
            field = regex[i][1]
            if(';' not in regex[i][0]):
                if(self.Check_Camel(field) == False):
                    check *= False
                    line.append(self.Check_Line_Number(regex[i][0]))
        # print(regex)
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line}\nName_Event_001 :\nNG: {self.dataJson["Field_Name"][1]["message"]}')
        # else:
        #     print('OKE1')

    #3.1 FORMAT
    def Check_Format(self):
        #Style_Format_005
        check = True
        line = []
        with open(self.pathFile, 'r', errors = "ignore") as inputFile:
            for line_i, line_t in enumerate(inputFile, 1):
                if (len(line_t.strip()) > 120):
                    check *= False
                    line.append(line_i)
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_005\nNG: {self.dataJson["Format"][5]["message"]}')
        # else:
        #     print('OKE5')

        #Style_Format_007 
        pattern = r' *(else if|if|while|for|switch)( *\()'
        regex = re.findall(pattern, self.content)
        check = True
        line = []
        for i in range(0, len(regex)):
            if (' ' not in regex[i][1]):
                var = regex[i][0] +regex[i][1]
                line.append(self.Check_Line_Number(var))
                check *= False
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_007\nNG: {self.dataJson["Format"][7]["message"]}')
        # else:
        #     print('OKE7')

        #Style_Format_008
        pattern = r' *(.*(\+\+|--|~|!));'
        regex = re.findall(pattern, self.content)
        check = True
        line = []
        for i in range(0, len(regex)):
            if (' ' in regex[i][0]):
                # print(regex[i][0].strip())
                var = regex[i][0]
                line.append(self.Check_Line_Number(var))
                check *= False
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_008\nNG: {self.dataJson["Format"][8]["message"]}')
        # else:
        #     print('OKE8')

        #Style_Format_009
        pattern = r' *([a-zA-Z0-9_]+ ?= ?[a-zA-Z0-9_]+( ?(\+|-|\*|/) ?[a-zA-Z0-9_]+)*);'
        regex = re.findall(pattern, self.content)
        check = True
        line = []
        # print(regex)
        for i in range(0, len(regex)):
            var = regex[i][0]
            if (' = ' not in var):
                line.append(self.Check_Line_Number(var))
                check *= False
            if ('+' in var):
                if(' + ' not in var):
                    line.append(self.Check_Line_Number(var))
                    check *= False
            if ('-' in var):
                if(' - ' not in var):
                    line.append(self.Check_Line_Number(var))
                    check *= False
            if ('*' in var):
                if(' * ' not in var):
                    line.append(self.Check_Line_Number(var))
                    check *= False
            if ('/' in var):
                if(' / ' not in var):
                    line.append(self.Check_Line_Number(var))
                    check *= False
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_009\nNG: {self.dataJson["Format"][9]["message"]}')
        # else:
        #     print('OKE9')

        # Style_Format_010
        pattern = r'(\(|\{)([a-zA-Z0-9_\"\']+,(,* *[a-zA-Z0-9_\"\']?)+)(\}|\))'
        regex = re.findall(pattern, self.content)
        check = True
        line = []
        for i in range(0, len(regex)):
            var = regex[i][1]
            length = len(var)
            tempt = regex[i][1].split(',')
            length = len(tempt)
            # print(tempt)
            for j in range(1, length):
                if(tempt[j][0] != ' '):
                    check *= False
                    line.append(self.Check_Line_Number(var))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_010\nNG: {self.dataJson["Format"][10]["message"]}')
        # else:
        #     print('OKE10')

        #Style_Format_011
        pattern = r'(([a-zA-Z0-9_]+ ?= ?[a-zA-Z0-9_]+( ?(\+|-|\*|/) ?[a-zA-Z0-9_]+)*); *([a-zA-Z0-9_]+ ?= ?[a-zA-Z0-9_]+( ?(\+|-|\*|/) ?[a-zA-Z0-9_]+)*);)'
        regex = re.findall(pattern, self.content)
        check = True
        line = []
        for i in range(0, len(regex)):
            var = regex[i][0]
            line.append(self.Check_Line_Number(var))
            check *= False
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_011\nNG: {self.dataJson["Format"][11]["message"]}')
        # else:
        #     print('OKE11')

        #Style_Format_013
        pattern = r'( *)({)\n( *)(#if|#else|#endif)(.*)'
        regex = re.findall(pattern, self.content)
        check = True
        line = []
        tempt = ''
        var_t = ''
        # print(regex)
        for i in range(0, len(regex)):
            var = regex[i]
            if('{' in var and '#if' in var):
                tempt = var[0]
                if (regex[i][2] != (tempt + '  ')):
                    line.append(self.Check_Line_Number(var[3] + var[4]))
                    check *= False
                var_t = var[3] + var[4]
            else:
                if (regex[i][2] != (tempt + ('  '))):
                    check *= False
                    line.append(self.Check_Line_Number(var_t))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_013\nNG: {self.dataJson["Format"][13]["message"]}')
        # else:
        #     print('OKE13')

        #Style_Format_014
        check = True
        line_t = []
        with open(self.pathFile, 'r', errors = "ignore") as inputFile:
            for line_i, line in enumerate(inputFile, 1):
                if (len(line.strip()) != 0):
                    if(line[len(line)-2] == ' '  ):
                        if(line[len(line)-3] != '='):
                            check *= False
                            line_t.append(line_i)
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line_t} \nStyle_Format_014\nNG: {self.dataJson["Format"][14]["message"]}')
        # else:
        #     print('OKE14')

        #Style_Format_015
        check = True
        line = []
        var_const = []
        pattern = r'(static readonly|const) .+ (.+) = .*;'
        regex = re.findall(pattern, self.content)
        for i in range(0, len(regex)):
            var_const.append(regex[i][1])
            pattern_t = f"(.* == {regex[i][1]})"
            if (re.search(pattern_t, self.content) is not None):
                var = '== ' + regex[i][1]
                line.append(self.Check_Line_Number(var))
                check *= False
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_015\nNG: {self.dataJson["Format"][15]["message"]}')
        # else:
        #     print('OKE15')

        #Style_Format_016
        check = True
        line = []
        pattern = r'\((([A-Za-z0-9_]*) (==|<|>|<=|>=) ([A-Za-z0-9_]*))\)'
        regex = re.findall(pattern, self.content)
        # print(regex)
        for i in range(len(regex)):
            RHS = regex[i][1]
            LHS = regex[i][3]
            if(RHS != 'true' and LHS != 'true' and RHS != 'false' and LHS != 'false' and RHS != '1' 
            and LHS != '1' and RHS != '0' and LHS != '0' and RHS != 'null' and LHS != 'null'):
                re_RHS = re.findall(f'(\w*) {RHS}[^\w][ =0-9.a-zA-Z+\-\*/]*;', self.content)
                re_LHS = re.findall(f'(\w*) {LHS}[^\w][ =0-9.a-zA-Z+\-\*/]*;', self.content)
                if(re_RHS != [] and re_LHS != []):
                    if (re_LHS[0] != re_RHS[0]):
                        check *= False
                        line.append(self.Check_Line_Number(regex[i][0]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Format_016\nNG: {self.dataJson["Format"][16]["message"]}')
        # else:
        #     print('OKE16')

    #3.2 FILE STRUCTURE
    def Check_File_Structure(self):
        #Style_File_003 
        check = True
        line = []
        end = ''
        before = ''
        with open(self.pathFile, 'r', errors = "ignore") as inputFile:
            for line_i, line_t in enumerate(inputFile, 1):
                    end = line_t
                    line = line_i 
            for line_i, line_t in enumerate(inputFile, 1):
                if(line_i == (line -1)):
                    before = line_t
                    break
            if ("\n" not in end):
                check *= False
            if(before.strip() == '' and end.strip() == ''):
                check *= False
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_File_003 \nNG: {self.dataJson["File_Structure"][3]["message"]}')
        # else:
        #     print('OKE3')

    #3.3 COMMENTS
    def Check_Comment(self):
        #Style_Comment_004 + Style_Comment_005
        check = True
        pattern = r'((if|else|#if|for|while|do|switch) *.*\n){*\n(([a-zA-Z0-9_:;\"\' (){}><=+\-]*\n){10,})}*[#endif]* *(.*)'
        regex = re.findall(pattern, self.content)
        # print(regex)
        line = []
        for i in range(len(regex)):
            if('//' not in regex[i][4]):
                check *= False
                line.append(self.Check_Line_Number(regex[i][0]))
                print(regex[i][4])
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Comment_004\nNG: {self.dataJson["Comment"][4]["message"]}')
        # else:
        #     print('OKE4 and OKE5')
        
        #Style_Comment_006
        count = ''
        check = True
        line = []
        pattern = r'(//.* (//.*)\n)'
        regex = re.findall(pattern, self.content)
        # print(regex)
        if (regex != []):
            check *= False
            line.append(self.Check_Line_Number(regex[0][0]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nStyle_Comment_006\nNG: {self.dataJson["Comment"][6]["message"]}')
        # else:
        #     print('OKE6')

    #4.1 CONFORMANCE TO EXTERNAL RULES
    def Check_External(self):
        #Rules_Ext_003
        check = True
        line = []
        pattern = r'(byte|ushort|uint|ulong) (.*)'
        regex = re.findall(pattern, self.content)
        if (regex != []):
            check *= False
            print(regex)
            for i in range(len(regex)):
                line.append(self.Check_Line_Number(regex[i][0] + ' ' + regex[i][1]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Ext_003 \nNG: {self.dataJson["External"][3]["message"]}')
        # else:
        #     print('OKE3')

    #4.3. COMMENTS/DOCUMENTATION
    def Check_Rule_Comment(self):
        #Rules_Comment_001
        check = True
        string = []
        line = []
        pattern = r'/// <summary>\n */// *(.*)\n( *///.*\n)* */// </summary>'
        pattern2 = r'/\* (.*)() \*/'
        pattern3 = r'.*[^/]// (.*)()'
        regex1 = re.findall(pattern, self.content)
        regex2 = re.findall(pattern2, self.content)
        regex3 = re.findall(pattern3, self.content)
        regex = regex1 + regex2 + regex3
        for i in range(len(regex)):
            for k in range(len(regex[i])):
                string = regex[i][k].split(' ')
                for j in range(len(string)):
                    string_t = string[j].strip('.').strip(',').strip(':').strip(';').strip('!').strip('(').strip(')')
                    if(string_t != ''):
                        check_string = Dict_US.check(string_t)   
                    if(check_string == False):    
                        if(string_t.isupper() == False):
                            if (string_t.isalpha()):
                                # print(string_t)
                                if(self.Check_Spell(string_t) == False):
                                    check *= False
                                    line.append(self.Check_Line_Number(string_t))
                                    print (string_t)
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Comment_001 \nNG: {self.dataJson["Rule_Comment"][1]["message"]}')
        # else:
        #     print('OKE1')
            
        #Rules_Comment_007
        # check = True
        # string = []
        # line = []
        # pattern = r'(.*)\n( *[^/]// *.*)\n(.*[^/]// .*\n)+(.*)'
        # regex = re.findall(pattern, self.content)
        # print(regex)
        # for i in range(len(regex)):
    
    #4.5 TYPES
    def Check_Types(self):
        #Rules_Types_002
        check = True
        line = []
        pattern = r'.*enum.*\n *{\n(( *[a-zA-Z0-9_, =]*\n)+) *};*'
        regex = re.findall(pattern, self.content)
        # print(regex)
        for i in range(len(regex)):
            enumvar = regex[i][0].split(',')
            # print(regex_t)
            for j in range(len(enumvar)):
                var = enumvar[j].strip().split(' ')
                if(var[0] != ''):
                    var_enum = var[0]
                # print(var_enum)
                pattern_t = f'({var_enum} *[+\-*/] *[a-zA-Z_0-9]*)'
                regex_t = re.findall(pattern_t, self.content)
                if (regex_t != []):
                    for k in range(len(regex_t)):
                        check *= False
                        line.append(self.Check_Line_Number(regex_t[k]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Types_002 \nNG: {self.dataJson["Types"][2]["message"]}')
        # else:
        #     print('OKE2')
        
        #Rules_Types_004
        check = True
        line = []
        pattern = r'(for|while) \((.*([a-zA-Z]).*)\)'
        regex = re.findall(pattern, self.content)
        # print(regex)
        for i in range(len(regex)):
            pattern_t = f'(([a-z]+) {regex[i][2]} *=* *[0-9]*;)'
            regex_t = re.findall(pattern_t, self.content)
            for j in range(len(regex_t)):
                if(regex_t[j][1] != 'int'):
                    check *= False
                    line.append(self.Check_Line_Number(regex_t[j][0]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Types_002 \nNG: {self.dataJson["Types"][4]["message"]}')
        # else:
        #     print('OKE4')
            
    #4.6 CONSTANTS
    def Check_Constant(self):
        #Rules_Const_001 
        check = True
        line = []
        pattern = r'0x([0-=a-fA-F]*)u*l*'
        regex = re.findall(pattern, self.content)
        # print(regex)
        for i in range(len(regex)):
            regex_t = regex[i].strip('<').strip(';')
            if(regex_t != ''):
                if(regex_t.isnumeric() == False):
                    if(regex_t.isupper() == False):
                        check *= False
                        line.append(self.Check_Line_Number('0x' + regex_t))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Const_001 \nNG: {self.dataJson["Constant"][1]["message"]}')
        # else:
        #     print('OKE1')

        #Rules_Const_004
        check = True
        line = []
        pattern = r'(const.* ([a-zA-Z_]+)) *=* *.*;'
        regex = re.findall(pattern, self.content)
        # print(regex)
        for i in range(len(regex)):
            if(regex[i][1].isupper() == False):
                check *= False
                line.append(self.Check_Line_Number(regex[i][0]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Const_004 \nNG: {self.dataJson["Constant"][4]["message"]}')
        # else:
        #     print('OKE4')

    #4.7 DECLARATIONS AND DEFINITIONS
    def Check_Declaration(self):
        #Rules_Defn_Decl_004
        check = True
        line = []
        pattern = r'([a-zA-Z<>]+ [a-zA-Z_]* *=* *[a-zA-Z0-9_]*(, [a-zA-Z_0-9]* *=* *[a-zA-Z0-9_]*)+;)'
        regex = re.findall(pattern, self.content)
        # print(regex)
        if (regex != []):
            for i in range(len(regex)):
                check *= False
                line.append(self.Check_Line_Number(regex[i][0]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Defn_Decl_004 \nNG: {self.dataJson["Declaration"][4]["message"]}')
        # else:
        #     print('OKE4')

        #Rules_Defn_Decl_012
        check = True
        line = []
        pattern = r'[a-zA-Z<>]+ ([a-zA-Z_]*)( = [a-zA-Z0-9_]*)*;'
        regex = re.findall(pattern, self.content)
        # print(regex)
        for i in range(len(regex)):
            regex_t = re.findall(regex[i][0], self.content)
            if(len(regex_t) < 2):
                check *= False
                line.append(self.Check_Line_Number(regex[i][0]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Defn_Decl_012 \nNG: {self.dataJson["Declaration"][12]["message"]}')
        # else:
        #     print('OKE12')

        #Rules_Defn_Decl_013
        check = True
        line = []
        pattern = r'param name=\"(.*)\"'
        regex = re.findall(pattern, self.content)
        for i in range(len(regex)):
            regex_t = re.findall(regex[i], self.content)
            if(len(regex_t) < 2):
                check *= False
                line.append(self.Check_Line_Number(regex[i]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Defn_Decl_013 \nNG: {self.dataJson["Declaration"][13]["message"]}')
        # else:
        #     print('OKE13')

        #Rules_Defn_Decl_027
        check = True
        line = []
        pattern = r'(.*)\n *([a-z]+ [a-zA-Z0-9_]+ = [0-9]*;)\n([a-z]+ [a-zA-Z0-9_]+ = [0-9]*;\n)*'
        regex = re.findall(pattern, self.content)
        # print(regex)
        for i in range(len(regex)):
            if('{' not in regex[i][0]):
                check *= False
                line.append(self.Check_Line_Number(regex[i][1]))
        if(check == 0):
            print(f'{self.location}\{self.nameFile}\nIn line: {line} \nRules_Defn_Decl_027 \nNG: {self.dataJson["Declaration"][27]["message"]}')
        # else:
        #     print('OKE27')


if (__name__ == '__main__'):
    for i in range(len(path_total)):
        for j in range(len(path_total[i])):
            if('.' not in path_total[i][j]):
                os.chdir(path_total[i][j])
                pathFile = glob.glob("*.cs") #list all file in folder
                if(pathFile != []):
                    for k in range(len(pathFile)):
                        ob = CodingRule(pathFile[k], path_total[i][j])
                        ob.Check_Declaration()
                        ob.Check_Constant()
                        ob.Check_Types()
                        ob.Check_Rule_Comment()
                        ob.Check_External()
                        ob.Check_Comment()
                        ob.Check_File_Structure()
                        ob.Check_Format()
                        ob.Check_Field_Name()
                        ob.Check_File_Name()
                        ob.Check_Variable_Name()
                        ob.Check_Method_Name()
                        ob.Check_Type_Name()
                        ob.Check_Param_Name()
                        ob.Check_Class_Name()
                        ob.Check_Event_Name()