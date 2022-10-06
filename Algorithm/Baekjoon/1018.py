N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
minC = 9999
# reverse = {'W': 'B', 'B':'W'}
ans1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
ans2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

# for i in range(N-8+1):
#     new_board = board[i:i+8]
#     for j in range(M-8+1):
#         cnt = 0
#         for c in range(8):
#             if b[c] == b[c-1]:
#                 b[c] = reverse[b[c]]
#                 cnt += 1
#             if
#         if cnt < minC:
#             minC = cnt
# print(cnt)