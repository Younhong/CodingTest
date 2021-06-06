def solution(info_list, query_list):
  answer = []

  for query in query_list:
    first, _, second, _, third, _, fourth, fifth = query.split(" ")
        
    # print("=======")
    # print("QUERY POSITION")
    # print(first)
    # print(second)
    # print(third)
    # print(fourth)
    # print(fifth)
    # print("=======")

    ans = 0

    for info in info_list:
      lang, pos, exp, food, score = info.split(" ")

      # print("=======")
      # print("INFO")
      # print(lang)
      # print(pos)
      # print(exp)
      # print(food)
      # print(score)
      # print("=======")

      if (first == "-" or first == lang) and (second == "-" or second == pos) and (third == "-" or third == exp) and (fourth == "-" or fourth == food) and (fifth == "-" or int(fifth) <= int(score)):
        ans = ans + 1
    
    answer.append(ans)
  
  return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))