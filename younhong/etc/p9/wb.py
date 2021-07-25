row, col = map(int, input().split())

n_list = []

# not solved
terminate = False
for i in range(col):
  inputData = input()

  # 길이에 맞지 않을 경우 바로 break
  if len(inputData) == row:
    temp = []
    for j in range(len(inputData)):
      if (inputData[j].lower() != 'w' and inputData[j].lower() != 'b'):
        terminate = True
      else:
        temp.append(inputData[j].upper())
    if terminate:
      print('Only Include W and B')
      break
    n_list.append(temp)
  else:
    print('Wrong Input Length')
    break

comb_list = []
for i in range(col):
  for j in range(row):
    if i == 0 and j == 0:
      comb_list.append([[i, j]])
    elif i != 0 and j == 0:
      if n_list[i][j] == n_list[i-1][j]:
        for k in range(len(comb_list)):
          if [i-1, j] in comb_list[k]:
            comb_list[k].append([i, j])
      else:
        comb_list.append([[i, j]])
    elif i == 0 and j != 0:
      if n_list[i][j] == n_list[i][j-1]:
        for k in range(len(comb_list)):
          if [i, j-1] in comb_list[k]:
            comb_list[k].append([i, j])
      else:
        comb_list.append([[i, j]])
    else:
      # 위와 같을 경우

print(comb_list)

# wbw 
# wbw
# www

# 5 5
# WBWWW
# WWWWW
# BBBBB
# BBBWW
# WWWWW