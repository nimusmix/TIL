from string import ascii_uppercase

w = input().upper()
a_list = list(ascii_uppercase)
mx_list = []

for i in a_list:
    mx_list.append(w.count(i))
if mx_list.count(max(mx_list)) > 1:
    print('?')
else:
    print(a_list[mx_list.index(max(mx_list))])