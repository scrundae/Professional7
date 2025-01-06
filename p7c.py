import re
import sys

KEYWORDS = {
    'Sub': 'void',  
    'Integer': 'int',
    'Character': 'char',
    'While': 'while',
    'Do': 'do',
    'Match': 'match',
    'Case': 'case',
    'Default': 'default',
    'Proceed': 'continue',
    'Start': '{',
    'End': '}',
    'If': 'if',
    'Else': 'else',
    'Return': 'return',
    'For': 'for',
    'Public': 'public',
    'Private': 'private',
    'Protected': 'protected',
    'Bucket': 'class',

}

def convert_to_c(pseudo_code, keywords):
    # Split the input pseudo-code into lines for easier processing
    lines = pseudo_code.splitlines()
    c_code = []

    # Replace each keyword in the line with its corresponding C equivalent
    for line in lines:
        for key, value in keywords.items():
            line = line.replace(key, value)
        c_code.append(line)

    # Combine the converted lines back into a single string
    return "\n".join(c_code)

fl = open(sys.argv[1], 'r')
out = open(sys.argv[2], 'w')

pseudo_code = fl.read()

converted_c_code = convert_to_c(pseudo_code, KEYWORDS)
out.write(converted_c_code)
