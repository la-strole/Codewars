def valid_parentheses(string):
    return string.index('(') < string.index(')') and string.count('(') == string.count(')')

print(valid_parentheses(")("))