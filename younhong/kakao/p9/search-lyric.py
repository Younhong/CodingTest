# not solved
def solution(words, queries):
  answer = []

  for q in queries:
    ans = 0
    
    # ?가 앞에서 시작할 때
    if q.find("?") == 0:
      index = q.rfind("?")
      first, second = q[:index+1], q[index+1:]
    # ?가 뒤에서 시작할 때
    else:
      index = q.find("?")
      first, second = q[:index], q[index:]
    
    for w in words:
      if len(w) == len(q):
        if '?' in first:
          if second == w[index+1:]:
            ans += 1
        elif '?' in second:
          if first == w[:index]:
            ans += 1
    answer.append(ans)

  return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))