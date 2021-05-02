def solution(new_id):
  answer = ""
  
  # stage 1
  answer = new_id.lower()
  
  # stage 2
  temp = ""
  for l in answer:
    if l.isdigit() or l.isalpha() or l == "-" or l == "." or l == "_":
      temp += l

  answer = temp
  
  # stage 3
  if len(answer) > 0:
    temp = answer[0]
  for i in range(1, len(answer)):
    if answer[i] != "." or answer[i-1] != ".":
      temp += answer[i]

  answer = temp

  # stage 4
  if len(answer) > 0:
    if answer[0] == ".":
      answer = answer[1: len(answer)]
      
  if len(answer) > 0:
    if answer[len(answer) - 1] == ".":
      answer = answer[0: len(answer) - 1]

  # stage 5
  if len(answer) == 0:
    answer = "a"
  
  # stage 6
  if len(answer) >= 16:
    answer = answer[0: 15]
    if answer[len(answer) - 1] == ".":
      answer = answer[0: len(answer) - 1]

  # stage 7
  if len(answer) == 1:
    answer = answer + answer[0] * 2
  elif len(answer) == 2:
    answer = answer + answer[1]

  return answer

print(solution(".1."))
# print(solution("~!@#$%&*()=+[{]}:?,<>/"))
# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))