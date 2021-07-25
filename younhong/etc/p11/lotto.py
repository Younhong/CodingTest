from itertools import product, combinations

input_list = []

while(True):
  temp = list(map(int, input().split()))
  if (temp[0] == 0):
    break
  else:
    input_list.append(temp)

for i in range(len(input_list)):
  current_input_list = input_list[i]
  list_len = current_input_list[0]

  # has invalid list length
  if list_len + 1 != len(current_input_list):
    print('invalid length')
    break

  if list_len <= 6 and list_len >= 13:
    print('invalid length input')

  new_list = sorted(current_input_list[1:])

  combi_list = list(combinations(new_list, 6))
  
  for combi in combi_list:
    temp_str = ''
    for e in range(len(combi)):
      if e == 0:
        temp_str = str(combi[e])
      else:
        temp_str = temp_str + ' ' + str(combi[e])
    print(temp_str)

  if i != len(input_list) - 1:
    print('')

# 7 1 2 3 4 5 6 7
# 8 1 2 3 5 8 13 21 34
# 0