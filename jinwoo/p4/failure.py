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
          totalNumber += 1 # 현 스테이지에 도달한 사람들
          totalFail += 1 # 현 스테이지에 실패한 사람들
        elif stage > i:
          totalNumber += 1 # 현 스테이지를 통과한 사람들 더하기
      # totalNumber = 결국 이 for문은 현 스테이지를 도달했거나 통과한 사람들 중에서 통과하지 못하고 머무른 사람들 수 
      if (totalNumber == 0):
        percent = 0
      else:
        percent = totalFail / totalNumber
      
      #각 stage번호 1~N 순으로 실패율 저장 + indexList에 i 저장
      percentList.append(percent)
      indexList.append(i)

    # 이중 
    for i in range(len(percentList)):
      for j in range(len(percentList)):
        if percentList[i] > percentList[j]:
          percentList[i], percentList[j] = swap(percentList[i], percentList[j])

          indexList[i], indexList[j] = swap(indexList[i], indexList[j])
        elif percentList[i] == percentList[j]:
          if indexList[i] < indexList[j]:
            indexList[i], indexList[j] = swap(indexList[i], indexList[j])

    return indexList

def swap(a, b):
  temp = a
  a = b
  b = temp

  return a, b

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(	4, [4, 4, 4, 4, 4]))