N = int(input())

words = []

for _ in range(N):
    word = input()  
    words.append(word)

set_words = set(words)
words = list(set_words)

words.sort()
words.sort(key = len)

for i in words:
    print(i)