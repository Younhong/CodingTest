def solution(N, stages):
    percentList = []
    indexList = []

    if N < 1 or N > 500 or len(stages) < 1 or len(stages) > 200000:
      return "Invalid"

    for i in range(1, N+1):
      totalNumber = 0
      totalFail = 0
      percent = 0

      for stage in stages:
        if stage == i:
          totalNumber += 1
          totalFail += 1
        elif stage > i:
          totalNumber += 1
        
      if (totalNumber == 0):
        percent = 0
      else:
        percent = totalFail / totalNumber

      percentList.append(percent)
      indexList.append(i)

    for i in range(len(percentList)):
      for j in range(len(percentList)):
        if percentList[i] > percentList[j]:
          temp = percentList[i]
          percentList[i] = percentList[j]
          percentList[j] = temp

          temp = indexList[i]
          indexList[i] = indexList[j]
          indexList[j] = temp
        elif percentList[i] == percentList[j]:
          if indexList[i] < indexList[j]:
            temp = indexList[i]
            indexList[i] = indexList[j]
            indexList[j] = temp

    return indexList

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

print(solution(	4, [4, 4, 4, 4, 4]))