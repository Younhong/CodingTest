def solution(N, number):
  answer = 0
  comboList = [N]
  countNList = [1]
  found = False

  if N < 1 or N > 9 or number < 1 or number > 32000:
    return -1

  # check if number only consists of N
  if str(number).count(str(N)) == len(str(number)):
    return len(str(number))

  for i in range(2, 9):
    if i == 2:
      newList = [1, N + N, N + N * 10, N * N]
      for n in newList:
        if n == number:
          return i
        elif n not in comboList and n > 0:
          comboList.append(n)
          countNList.append(i)
    else:
      comboList.append(int(str(N) * i))
      countNList.append(i)

      for j in range(0, len(countNList)):
        for k in range(0, len(countNList)):
          if j != k and countNList[j] + countNList[k] == i:
            temp1 = comboList[j]
            temp2 = comboList[k]
            
            newList = [temp1 + temp2, temp1 // temp2, temp1 - temp2, temp1 * temp2]

            for n in newList:
              if n == number:
                return i
              elif n not in comboList and n > 0:
                comboList.append(n)
                countNList.append(i)
  
  return -1

# print(solution(5, 31168))
print(solution(5, 2))
# print(solution(2, 11))