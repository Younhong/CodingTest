def solution(n, lost, reserve):
  hasUniform = n - len(lost)
  
  lost = sorted(lost)
  reserve = sorted(reserve)

  temp = []
  for r in lost:
    if r in reserve:
      reserve.remove(r)
      temp.append(r)
      hasUniform += 1

  for t in temp:
    lost.remove(t)

  for r in lost:
    if r-1 in reserve:
      reserve.remove(r-1)
      hasUniform += 1
    elif r+1 in reserve:
      reserve.remove(r+1)
      hasUniform += 1
      
  return hasUniform

print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5, [2, 4], [3]))
# print(solution(3, [3], [1]))