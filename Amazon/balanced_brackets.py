def isBalanced(the_string):
    paren_map = {')': '(', '}': '{', ']': '[', '>': '<'}
    open_parens = paren_map.values()
    stack = []
    for char in the_string:
        if not(char in open_parens or char in paren_map):
            continue
        elif char in paren_map:
            top = stack.pop() if stack else '#'
            if top != paren_map[char]:
                return False
        else:
            stack.append(char)
    return not stack


string1 = '(h[e{l<l>o}!]~)()()()('
string2 = 'k<>ol{i()}'
string3 = '<>'
string4 = '({}([][]))[]()'
string5 = '[{]}'
string6 = '{[(])}'
print(isBalanced(string1))
print(isBalanced(string2))
print(isBalanced(string3))
print(isBalanced(string4))
print(isBalanced(string5))
print(isBalanced(string6))
