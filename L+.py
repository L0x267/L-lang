import std.stdin as std_in
import std.stdout as std_out
import std.stdtype as std_type
import std.stdvar as std_var
import std.stdlib as std_lib
import std.stdnum as std_num
import sys


def Run(codes, bf=''):
    # format
    codes = codes.split('\n')
    for i in codes:
        try:
            for j in std_var.GlobalVar:
                i = i.replace('$' + str(j[1]), str(j[0]))
            i = i.split(' ')
            x = []
            for j in i:
                x.append(j.replace('%n', ' ').replace('%b', str(bf)).replace('%l', '\n'))

            # run
            # stdin
            if x[0] == 'InputLN':
                bf = std_in.InputLineNext(*x[1:])
            elif x[0] == 'InputL':
                bf = std_in.InputLine(*x[1:])
            # stdout
            elif x[0] == 'PrintLN':
                bf = std_out.PrintTextLineNext(*x[1:])
            elif x[0] == 'PrintL':
                bf = std_out.PrintTextLine(*x[1:])
            # stdtype
            elif x[0] == 'Type':
                bf = std_type.TypeOfVar(std_var.GetVar(x[1]))
            elif x[0] == 'ToInt':
                bf = std_var.SetVar(*std_type.ToInt(std_var.GetVar(x[1])))
            elif x[0] == 'ToFloat':
                bf = std_var.SetVar(*std_type.ToFloat(std_var.GetVar(x[1])))
            elif x[0] == 'ToString':
                bf = std_var.SetVar(*std_type.ToString(std_var.GetVar(x[1])))
            elif x[0] == 'ToBool':
                bf = std_var.SetVar(*std_type.ToBool(std_var.GetVar(x[1])))
            # stdvar
            elif x[0] == 'Let':
                bf = std_var.NewVar(*x[1:])
            elif x[0] == 'Del':
                bf = std_var.DelVar(x[1])
            elif x[0] == 'Set':
                bf = std_var.SetVar(*x[1:])
            # include
            elif x[0] == 'IncludeNL':
                bf = std_lib.bdjwo3y57r9vge749gsg7393hwgd9gebe937shs0fusbm0acnroo(x[1], False)
            elif x[0] == 'Include':
                bf = std_lib.bdjwo3y57r9vge749gsg7393hwgd9gebe937shs0fusbm0acnroo(x[1], True)
            elif x[0] == 'ListLib':
                bf = std_lib.ListLib()
            # color egg
            elif x[0] in ['Fuck', 'fuck', 'FUCK']:
                print('YOU TOO')
            elif x[0] in ['Shit', 'shit', 'SHIT']:
                print('YOU TOO')
            elif x[0] == '<SYSTEM-FORMAT-CODES>':
                print('PLS DONT RUN LX.PY')
            elif x[0] in ['#', '//', 'REM']:
                pass
            # num
            elif x[0] == 'Add':
                bf = std_num.AddVar(x[1], x[2])
            elif x[0] == 'Sub':
                bf = std_num.SubVar(x[1], x[2])
            elif x[0] == 'If':
                if len(x) == 5:
                    if int(x[1]) != 0: 
                        bf = Run(x[2], bf)
                    else:
                        if x[4] == '-else':
                            bf = Run(x[4], bf)
                else:
                    if int(x[1]) != 0:
                        bf = Run(x[2], bf)
            # get helpL 
            elif x[0] == 'Ver': 
                print('L+ ver2.8\nby _0x-') 
            elif x[0] in ['Help', 'help', 'HELP']: 
                print('-') 
            # exit
            elif x[0] in ['Exit', 'exit', 'EXIT']:
                global rtn
                rtn = 1
                break
            # user lib
            else:
                bf = std_lib.h1v2k4jv2n3ktbyn4irje4n68j6j3n3og9hu43h49t7fgd37384bey9wb3(x[0], *x[1:])
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
if len(sys.argv) == 2:
    f = open(sys.argv[1], 'r').read() if sys.argv[1].split('.')[-1] in ['l+', 'L+'] else (
                'PrintLN PLEASE %nUSE %n.L+ %nFILE\n'
                * 100 + '.l+')
    Run(f)
else:
    typ = 'Console'
    print('L+ CONSOLE VER2.8')
    print('TYPE "HELP" GET HELP') 
    while not rtn:
        Return = Run(input('# '), Return)
input(f'\n\nRETURN CODE: {rtn} | PRESS [ENTER] TO EXIT')
