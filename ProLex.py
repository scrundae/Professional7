import re

def lexicate(input_string):
    pattern = r"""
        "([^"\\]*(?:\\.[^"\\]*)*)" |    # Double-quoted strings
        '([^'\\]*(?:\\.[^'\\]*)*)' |    # Single-quoted strings
        (\S+)                           # Other words (not whitespace)
    """
    
    matches = re.finditer(pattern, input_string, re.VERBOSE)
    tokens = []

    for match in matches:
        if match.group(1):
            tokens.append(match.group(1))
        elif match.group(2):
            tokens.append(match.group(2))
        elif match.group(3):
            tokens.append(match.group(3))
    
    return tokens