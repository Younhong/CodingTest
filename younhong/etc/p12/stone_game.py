import random

stone_num = int(input())

stone_option = [1, 3, 4]
5, 3, 2
4,2,1 0,0,0 1,0,0

turn = 0
if stone_num < 1 or stone_num > 1000000:
  print('invalid input')
else:
  while stone_num >= 0:
    turn = turn + 1
    rand = random.randrange(0,3)

    print('result: ', stone_option[rand])

    if stone_num - stone_option[rand] <= 0:
      break
    else:
      stone_num = stone_num - stone_option[rand]

print(stone_num)
if stone_num >= 1:
  turn = turn + 1

if turn % 2 == 0:
  print('SK')
else:
  print('CY')