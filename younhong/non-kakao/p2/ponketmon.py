def solution(nums):
  loopNum = len(nums) // 2
  
  answer = 0
  uniqueNumList = []

  for i in nums:
    if i not in uniqueNumList:
      uniqueNumList.append(i)

  if len(uniqueNumList) >= loopNum:
    answer = loopNum
  else:
    answer = len(uniqueNumList)
  
  return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))