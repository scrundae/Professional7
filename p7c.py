import STD
import sys
import shlex

class interpreter:
    def __init__(self):
        variables = {}
    def execute_script(filename):
        f = open(filename, 'r')
        ftext = f.read()
        for line in ftext.split('\n'):
            flex = shlex.split(line)
            if flex[0] == "Print":
                STD.PrintCom(flex[1])
            elif flex[0] == "Input":
                STD.InputCom(flex[1])
        

fn = sys.argv[1]
interpreter.execute_script(fn)