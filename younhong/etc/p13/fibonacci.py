input_num = int(input())

if input_num > 90 or input_num <= 0:
  print('invalid input')
else:
  fibo_list = [0 for i in range(input_num + 1)]

  fibo_list[0] = 0
  fibo_list[1] = 1

  for i in range(2, input_num + 1):
    fibo_list[i] = fibo_list[i - 1] +fibo_list[i - 2]

  print(fibo_list[input_num])