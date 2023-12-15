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
