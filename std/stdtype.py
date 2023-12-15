def TypeOfVar(obj: list):
    return type(obj[0])


def ToInt(obj: list):
    return [int(obj[0]), obj[1]]


def ToString(obj: list):
    return [str(obj[0]), obj[1]]


def ToBool(obj: list):
    return [bool(obj[0]),  obj[1]]


def ToFloat(obj: list):
    return [float(obj[0]),  obj[1]]
