# Professional7.1: Python Interpreter

import sys
import ProLex
import ProSaladIB as salad


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
                if flex[1][0] == "$":
                    self.execute_code(self.variables[flex[1]])
                else:
                    self.execute_code(flex[1])
            elif flex[0] == "ExecScript":
                if flex[1][0] == "$":
                    self.execute_script(self.variables[flex[1]])
                else:
                    self.execute_script(flex[1])


            elif flex[0] == "PyExec":
                exec(flex[1])
            elif flex[0] == "NewLine":
                print("")

            elif flex[0] == "SaladServer":
                self.variables[flex[1]] = salad.StartSaladServer()
            elif flex[0] == "SaladClient":
                self.variables[flex[1]] = salad.SaladInvade(self.variables[flex[2]])
            elif flex[0] == "SaladSend":
                salad.SaladSend(self.variables[flex[1]], flex[2])
            
            elif flex[0] == "Integer":
                self.variables[flex[1]] = 0
            elif flex[0] == "String":
                self.variables[flex[1]] = ""

            elif flex[0][0] == "*":
                repflex = flex[0].replace('*', '$')
                self.execute_script(self.variables[repflex])

            elif flex[1] != None:
                if flex[1] == "is":
                    self.variables[flex[0]] = flex[2]
            elif flex[0] == '':
                pass


fn = sys.argv[1]
interpreter().execute_script(fn)
