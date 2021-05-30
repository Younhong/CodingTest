def solution(s):
  s = list(s)
  if len(s) % 2 == 1:
    return 0

  temp = []
  for i in range(len(s)):
    if len(temp) == 0:
      temp.append(s[i])
    else:
      if temp[len(temp) - 1] == s[i]:
        temp.pop()
      else:
        temp.append(s[i])

  if len(temp) == 0:
    answer = 1
  else:
    answer = 0

  return answer

print(solution('bb'))
print(solution('bbbc'))
print(solution('bbcc'))
print(solution('cbfbccbbcf'))