def solution(N, stages):
    answer = []
    percentList = []

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

    print(percentList)

    # sorting
    answer = sorted(range(len(percentList)), key=lambda k: percentList[k], reverse = True)

    for i in range(len(answer)):
      answer[i] += 1

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))