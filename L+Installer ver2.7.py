import sys
# 将打包为.py文件
open(sys.argv[1]+'.py', 'w', encoding='utf-8').write('''def InputLineNext(*prompt):
    a = '\n'
    for i in prompt:
        a += i
    return input(a)


def AddVar(a, b):
    return GetVar(a)[0] + GetVar(b)[0]


def SubVar(a, b):
    return GetVar(a)[0] - GetVar(b)[0]


def PrintTextLineNext(*text):
    a = '\n'
    for i in text:
        a += str(i) + ' '
    print(a, end='')
    return a


def PrintTextLine(*text):
    a = ''
    for i in text:
        a += str(i) + ' '
    print(a, end='')
    return a


def TypeOfVar(obj: list):
    return type(obj[0])


def ToInt(obj: list):
    return [int(obj[0]), obj[1]]


def ToString(obj: list):
    return [str(obj[0]), obj[1]]


def ToBool(obj: list):
    return [bool(obj[0]), obj[1]]


def ToFloat(obj: list):
    return [float(obj[0]), obj[1]]


GlobalVar = []


def NewVar(value, name):
    global GlobalVar
    GlobalVar.append([value, name])
    return [value, name]


def GetVar(name):
    global GlobalVar
    for i in range(len(GlobalVar)):
        if GlobalVar[i][1] == name:
            return GlobalVar[i]
    return []


def SetVar(value, name):
    global GlobalVar
    for i in range(len(GlobalVar)):
        if GlobalVar[i][1] == name:
            GlobalVar[i][0] = value
            return GlobalVar[i]
    NewVar(value, name)


def DelVar(name):
    global GlobalVar
    for i in range(len(GlobalVar)):
        if GlobalVar[i][1] == name:
            a = GlobalVar[i]
            del GlobalVar[i]
            return a
    return []


def InputLine(*prompt):
    a = ''
    for i in prompt:
        a += i
    return input(a)


def Run(codes, bf=''):
    # format
    codes = codes.split('\n')
    for i in codes:
        try:
            for j in GlobalVar:
                i = i.replace('$' + str(j[1]), str(j[0]))
            i = i.split(' ')
            x = []
            for j in i:
                x.append(j.replace('%n', ' ').replace('%b', str(bf)).replace('%l', '\n'))

            # run
            # stdin
            if x[0] == 'InputLN':
                bf = InputLineNext(*x[1:])
            elif x[0] == 'InputL':
                bf = InputLine(*x[1:])
            # stdout
            elif x[0] == 'PrintLN':
                bf = PrintTextLineNext(*x[1:])
            elif x[0] == 'PrintL':
                bf = PrintTextLine(*x[1:])
            # stdtype
            elif x[0] == 'Type':
                bf = TypeOfVar(GetVar(x[1]))
            elif x[0] == 'ToInt':
                bf = SetVar(*ToInt(GetVar(x[1])))
            elif x[0] == 'ToFloat':
                bf = SetVar(*ToFloat(GetVar(x[1])))
            elif x[0] == 'ToString':
                bf = SetVar(*ToString(GetVar(x[1])))
            elif x[0] == 'ToBool':
                bf = SetVar(*ToBool(GetVar(x[1])))
            # stdvar
            elif x[0] == 'Let':
                bf = NewVar(*x[1:])
            elif x[0] == 'Del':
                bf = DelVar(x[1])
            elif x[0] == 'Set':
                bf = SetVar(*x[1:])
            # color egg
            elif x[0] in ['Fuck', 'fuck', 'FUCK']:
                print('YOU TOO')
            elif x[0] in ['Shit', 'shit', 'SHIT']:
                print('YOU TOO')
            elif x[0] == '<SYSTEM-FORMAT-CODES>':
                print('PLS DONT RUN LX.PY')
            # num
            elif x[0] == 'Add':
                bf = AddVar(x[1], x[2])
            elif x[0] == 'Sub':
                bf = SubVar(x[1], x[2])
            # get help
            elif x[0] == 'Ver':
                print(open('version.txt', 'r', encoding='utf-8').read())
            elif x[0] in ['Help', 'help', 'HELP']:
                print(open('help/HowToUseL+.txt', 'r', encoding='utf-8').read())
            # exit
            elif x[0] in ['Exit', 'exit', 'EXIT']:
                global rtn
                rtn = 1
                break
        except Exception as e:
            global typ
            if typ == 'File':
                print(e)
                rtn = -1
                break
            else:
                print(e)
    return bf


rtn = 0
Return = ''
typ = 'File'
Run("""<SYSTEM-FORMAT-CODE>""")
input(f'\n\nRETURN CODE: {rtn} | PRESS [ENTER] TO EXIT')
'''.replace('<SYSTEM-FORMAT-CODE>', open(sys.argv[1], 'r', encoding='utf-8').read()))