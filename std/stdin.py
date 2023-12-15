def InputLineNext(*prompt):
    a = '\n'
    for i in prompt:
        a += i
    return input(a)


def InputLine(*prompt):
    a = ''
    for i in prompt:
        a += i
    return input(a)
