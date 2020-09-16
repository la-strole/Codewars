def valid_parentheses(string):
    return string.find('(') < string.find(')') and string.count('(') == string.count(')')

print(valid_parentheses(")("))