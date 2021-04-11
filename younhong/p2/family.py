def solution(familyNumber, target, relationNumber, relationList):
  relationMap = [[0 for i in range(familyNumber)] for i in range(familyNumber)]

  targetFrom = target[0]
  targetTo = target[1]
  
  for relation in relationList:
    x = relation[0]-1
    y = relation[1]-1
    relationMap[x][y] = 1
    relationMap[y][x] = -1

  parent = []
  child = []
  searchedNumber = []

  result = search(targetFrom, relationMap, familyNumber, targetFrom, targetTo, searchedNumber, 0) 
  
  return result

def search(i, relationMap, familyNumber, targetFrom, targetTo, searchedNumber, result):
  parent = []
  child = []
  searchedNumber.append(i)
  
  # 연결된 지점을 모두 찾음
  for x in range(familyNumber):
    if relationMap[i-1][x] == -1:
      parent.append(x+1)
    elif relationMap[i-1][x] == 1:
      child.append(x+1)

  # print("===")
  # print(searchedNumber)
  # print(parent)
  # print(child)
  # print(result)
  # print("===")

  # 연결 없을 때
  if (len(parent) == 0 and len(child) == 0):
    return 0
  else:
    if len(parent) > 0:
      # 각 상위 연결 지점에 대해서
      for x in parent:
        if x == targetTo:
          return 1
        elif x not in searchedNumber:
          result = search(x, relationMap, familyNumber, targetFrom, targetTo, searchedNumber, 0)
    elif len(child) > 0:
      for x in child:
        if x == targetTo:
          return 1
        elif x not in searchedNumber:
          result = search(x, relationMap, familyNumber, targetFrom, targetTo, searchedNumber, 0)

  if result > 0:
    return result + 1
  else:
    return 0

print(solution(9, [7,3], 7, [[1,2], [1,3], [2,7], [2,8], [2,9], [4,5], [4,6]]))
print(solution(9, [7,2], 3, [[1,2], [1,3], [3,7]]))
print(solution(9, [7,3], 2, [[1,2], [1,3]]))
print(solution(9, [7,3], 3, [[1,2], [1,3], [5,7]]))