import std.stdvar as s


def AddVar(a, b):
    return s.GetVar(a)[0] + s.GetVar(b)[0]


def SubVar(a, b):
    return s.GetVar(a)[0] - s.GetVar(b)[0]
