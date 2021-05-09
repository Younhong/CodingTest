def solution(relations):
  totalList = len(relations)
  answerList = []

  for i in range(len(relations)):
    if len(answerList) == 0:
      for relation in relations[i]:
        answerList.append([relation])
    else:
      for j in range(len(relations[i])):
        if relations[i][j] not in answerList[j]:
          answerList[j].append(relations[i][j])

  answer = 0
  temp = 0

  for ans in answerList:
    if len(ans) == len(relations):
      temp = temp + 1

  for i in range(1, answer+1):
    print(i)

  return answer * 2

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))