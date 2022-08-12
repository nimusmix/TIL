word = list(input())

def palindrome(x):
    check = 0

    for i in range(len(word) // 2):
        if word[i] == word[-i-1]:
            check += 1

    if check == len(word) // 2:
        return 'true'
    else:
        return 'false'

print(palindrome(word))