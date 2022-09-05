rank = {'(': (0, 3),
        '+': (1, 1),
        '-': (1, 1),
        '*': (2, 2),
        '/': (2, 2)}

words = input()
stack = []
postfix = []
tmp = ''

try:
    for i in words:
        if i.isdigit():
            postfix.append(i)
        elif i == ')':
            while tmp != '(':
                tmp = stack.pop()
                if tmp != '(':
                    postfix.append(tmp)
                tmp = ''
        else:
            if stack == [] or rank[i][1] > rank[stack[-1]][0]:
                stack.append(i)
            else:
                while stack != [] and rank[i][1] <= rank[stack[-1]][0]:
                    tmp = stack.pop()
                    postfix.append(tmp)
                stack.append(i)

    while stack:
        tmp = stack.pop()
        postfix.append(tmp)

    postfix = ''.join(postfix)

    stack = []
    for j in postfix:
        if j.isdigit():
            stack.append(j)
        else:
            tmp1 = int(stack.pop())
            tmp2 = int(stack.pop())
            if j == '+': tmp = tmp2 + tmp1
            elif j == '-': tmp = tmp2 - tmp1
            elif j == '*': tmp = tmp2 * tmp1
            elif j == '/': tmp = tmp2 // tmp1
            stack.append(tmp)

    if len(stack) == 1: print(stack.pop())
    else: print('ROCK')
except:
    print('ROCK')