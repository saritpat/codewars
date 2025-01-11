def remove_parentheses(st):
    ans = ''
    count = 0
    for i in st:
        if i == '(':
            count += 1
        
        if i == ')' and count > 0:
            count -= 1
        
        if count == 0 and i != '(' and i != ')':
            ans += i
        
    return ans


print(remove_parentheses('example(unwanted thing)example'))
print(remove_parentheses('example (unwanted thing) example'))
print(remove_parentheses('a (bc d)e'))
print(remove_parentheses('a(b(c))'))
print(remove_parentheses('hello example (words(more words) here) something'))
print(remove_parentheses('(first group) (second group) (third group)'))
