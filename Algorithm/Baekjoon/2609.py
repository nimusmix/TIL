a, b = map(int, input().split())

def divisor(x):
    i = 2
    x_li = []
    while i <= x:
        if x % i == 0:
            x_li.append(i)
            x //= i
            continue
        else:
            i += 1
            pass
    return x_li

a_li = divisor(a)
b_li = divisor(b)

div = 1

for i in a_li:
    if i in b_li:
        div *= i
        b_li.remove(i)

mul = div * (a/div) * (b/div)

print(div, int(mul), sep='\n')