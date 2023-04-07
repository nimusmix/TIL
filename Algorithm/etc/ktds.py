from itertools import permutations

def sol(cards_1, cards_2, k):
    all_cards = cards_1[:]
    all_cards.extend(cards_2)
    
    ans = 1e9
    for pr in permutations(all_cards, len(all_cards)):
        cnt = 0
        prev=''
        for i in range(len(all_cards)-1):
            if pr[i] > pr[i+1] and pr[i] - pr[i+1] != k:
                break
            
            if pr[i] in cards_1 and prev != 'c1':
                cnt += 1
                prev = 'c1'
            elif pr[i] in cards_2 and prev != 'c2':
                cnt += 1
                prev = 'c2'
        else:
            ans = min(ans, cnt)
    
    return ans
    
print(sol([2, 5, 6, 8], [1, 3, 4], 0))
print(sol([2, 4, 6, 8], [1, 3, 5, 7], 6))