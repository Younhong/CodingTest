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
    # print("===")
    # print(i)
    if i == 2:
      newList = [1, N * 2, N + N * 10, N * N]
      for n in newList:
        if n == number:
          return i
        elif n not in comboList and n > 0:
          comboList.append(n)
          countNList.append(i)
    else:
      for j in range(len(countNList)):
        for k in range(len(countNList)):
          # print(comboList)
          if j != k and countNList[j] + countNList[k] == i:
            temp1 = comboList[j]
            temp2 = comboList[k]
            if temp1 > temp2:
              newList = [temp1 + temp2, temp1 // temp2, temp1 - temp2, temp1 * temp2]
            else:
              newList = [temp1 + temp2, temp1 - temp2, temp1 * temp2]
            for n in newList:
              if n == number:
                return i
              elif n not in comboList and n > 0:
                comboList.append(n)
                countNList.append(i)
  
  if answer == 0:
    return -1
  return answer

# print(solution(5, 31168))
print(solution(5, 12))
print(solution(2, 11))