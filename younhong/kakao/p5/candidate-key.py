from itertools import product, combinations

def solution(relations):
  # 분리된 unique한 리스트
  uniqueList = []
  # 전체 분리된 리스트
  totalList = []
  # unique한 리스트의 index
  indexList = []

  totalIndexList = [i for i in range(len(relations[0]))]

  for i in range(len(relations)):
    if len(uniqueList) == 0:
      for relation in relations[i]:
        uniqueList.append([relation])
        totalList.append([relation])
    else:
      for j in range(len(relations[i])):
        totalList[j].append(relations[i][j])
        if relations[i][j] not in uniqueList[j]:
          uniqueList[j].append(relations[i][j])

  answer = 0

  for i in range(len(uniqueList)):
    if len(uniqueList[i]) == len(relations):
      indexList.append([i])

  for k in range(2, len(relations[0])):
    combo_list = list(combinations(totalIndexList, k))
    new_combo = []
    for combo in combo_list:
      for index in indexList:
        if (len(index) == 1):
          if index[0] not in combo:
            new_combo.append(combo)
    
    for i in range(len(new_combo)):
      combo = new_combo[i]

      # 전체 분리된 리스트
      uniqueList = []

      for j in range(len(totalList[0])):
        temp = [totalList[i][j] for i in combo]
        if len(uniqueList) == 0:
          uniqueList.append(temp)
        else:
          if temp in uniqueList:
            break
          else: 
            uniqueList.append(temp)

      if (len(uniqueList) == len(relations)):
        contains = False
        for index in indexList:
          if set(index).issubset(set(combo)) is True:
            contains = True
            break
      
        if contains is False:
          indexList.append(list(combo))

  return len(indexList)

print(solution([["100","ryan","music","2"],["200","apeachlll","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))