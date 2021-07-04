from itertools import product, combinations

N, target = map(int, input().split())
n_list = list(map(int, input().split()))

if len(n_list) != N:
  print('Invalid')
else:
  answer = 0

  for i in range(1, len(n_list) + 1):
    temp = list(combinations(n_list, i))
    for j in range(len(temp)):
      if sum(temp[j]) == target:
        answer += 1

  print(answer)