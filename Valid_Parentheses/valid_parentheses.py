def valid_parentheses(string):
    result = 0
    for i in string:
        if i == '(':
            result += 1
        elif i == ')':
            result -= 1
        if result < 0:
            return False
    return not result

print(valid_parentheses("(())"))