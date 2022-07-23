# 내가 푼 코드
a = input()
new = []

for i in a:
    if i.isupper() == True:
        i = i.lower()
        new.append(i)
    else:
        i = i.upper()
        new.append(i)
        
new = ''.join(new)
print(new)

# 좋은 코드
print(input().swapcase())