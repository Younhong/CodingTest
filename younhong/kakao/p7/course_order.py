from itertools import product, combinations

def solution(orders, course):
  combo_list = []
  answerList = []
  answer = []
  course_map = {}
  
  for k in course:
    for order in orders:
      order = sorted(order)
      if len(order) >= k:
        temp = list(combinations(order, k))
        
        for t in temp:
          # 조합을 하나의 문자열로 합쳐줌
          temp = ''
          for e in t:
            temp += e
          
          if temp in course_map:
            course_map[temp] += 1
          else:
            course_map[temp] = 1
  
  # print(course_map)
  for n in course:
    max_key = []
    max_value = 0
    for c in course_map:
      if len(c) == n and course_map[c] >= 2:
        if course_map[c] > max_value:
          max_key = [c]
          max_value = course_map[c]
        elif course_map[c] == max_value:
          max_key.append(c)
    
    for key in max_key:
      answer.append(key)

  # 결과 정렬
  answer = sorted(answer)

  return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))