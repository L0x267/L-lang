import importlib
import os


def bdjwo3y57r9vge749gsg7393hwgd9gebe937shs0fusbm0acnroo(name, t):
    module = importlib.import_module('std.lib.'+name+'.'+name)
    if t:
        withoutArgs = ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__',
                        '__builtins__']
        keyList = list(module.__dict__.keys())
        for k in keyList:
            if k not in withoutArgs:
                globals()[k] = module.__dict__.get(k)
    else:
        globals()[name] = importlib.import_module('std.lib.'+name+'.'+name)
    return 0


def h1v2k4jv2n3ktbyn4irje4n68j6j3n3og9hu43h49t7fgd37384bey9wb3(c, *args):
    return globals()[c](*args)


def ListLib():
    List = os.listdir('std/lib/')
    print(List)
    return List
