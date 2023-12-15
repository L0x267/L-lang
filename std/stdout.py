def PrintTextLineNext(*text):
    a = '\n'
    for i in text:
        a += str(i)+' '
    print(a, end='')
    return a


def PrintTextLine(*text):
    a = ''
    for i in text:
        a += str(i)+' '
    print(a, end='')
    return a
