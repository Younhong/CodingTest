import itertools

# not solved
N, M = map(int, input().split())

lamp = []
for i in range(N):
  input_temp = str(input())
  lamp.append(input_temp)

clickN = int(input())

rows = [[] for i in range(N)]

for i in range(N):
  for j in range(M):
    rows[j].append(int(lamp[i][j]))

combo_idx = [p for p in itertools.product([i for i in range(M)], repeat=clickN)]

maxList = []
for i in range(len(combo_idx)):
  changeIdx = combo_idx[i]
  for j in range(len(changeIdx)):

    # change idx of changeIdx[j]

  # checkMax
  
  # add to max list


# print(temp)