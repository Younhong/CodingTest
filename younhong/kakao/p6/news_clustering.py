def solution(str1, str2):  
  # 편의를 위해 소문자로 변경
  str1 = str1.lower()
  str2 = str2.lower()

  first_combo = []
  second_combo = []
  total_combo = []
  duplicate_combo = []

  for i in range(len(str1) - 1):
    if str1[i].isalpha() and str1[i+1].isalpha():
      first_combo.append([str1[i], str1[i+1]])

  for i in range(len(str2) - 1):
    if str2[i].isalpha() and str2[i+1].isalpha():
      second_combo.append([str2[i], str2[i+1]])

  for combo in first_combo:
    total_combo.append(combo)
  
  for combo in second_combo:
    if combo in first_combo:
      first_combo.remove(combo)
      duplicate_combo.append(combo)
    else:
      total_combo.append(combo)

  # print(first_combo)
  # print(second_combo)
  # print(total_combo)
  # print(duplicate_combo)

  if len(total_combo) == 0:
    answer = 1
  else:
    answer = len(duplicate_combo) / len(total_combo)
  
  # print(answer)

  return int(answer * 65536)

print(solution('E=M*C^2', 'e=m*c^2'))
print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2	', 'AAAA12'))