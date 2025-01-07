# Professional7.1: Python Interpreter

import STD
import sys
import ProLex

class interpreter:
    def __init__(self):
        self.variables = {}
    def execute_script(self, filename):
        f = open(filename, 'r')
        ftext = f.read()
        self.execute_code(ftext)
    def execute_code(self, code):
        for line in code.split('\n'):
            flex = ProLex.lexicate(line)
            print(flex)
            if flex[0] == "Print":
                if flex[1][0] == "$":
                    print(self.variables[flex[1]], end='')
                else:
                    print(flex[1], end='')
            elif flex[0] == "Input":
                input(flex[1])
            elif flex[0] == "Exec":
                self.execute_code(flex[1])
            elif flex[0] == "ExecScript":
                self.execute_script(flex[1])
            elif flex[0] == "PyExec":
                exec(flex[1])
            elif flex[0] == "NewLine":
                print("")
            
            elif flex[0] == "Integer":
                self.variables[flex[1]] = 0
            elif flex[0] == "String":
                self.variables[flex[1]] = ""

            elif flex[1] != None:
                if flex[1] == "is":
                    self.variables[flex[0]] = flex[2]
            
            else:
                if flex[0] == None:
                    print("skipping line")
                

        

fn = sys.argv[1]
interpreter().execute_script(fn)