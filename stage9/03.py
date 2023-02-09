#write a function check if given string is balanced with brackets or not
#Input : '(()[()]{()})' #Output : True
#Input : '((){[})' #Output : False

def check(string):
    stack = []
    bal = True
    i = 0
    while i < len(string) and bal:      #loopruns till the given string length
        bracket = string[i]
        if bracket == '(' or bracket=='[' or bracket=='{':
            stack.append(bal)             #push into stack
        else:
            if not stack:
                bal = False
            else:
                stack.pop()                  #pop from stack
        i += 1

    if bal and not stack:
        return True
    else:
        return False

print(check('(()[()]{()})'))             #paranthesis are balanced here return True
print(check('((){[})'))                #paranthesis are not abalance here returns False