def stage1(new_id):
  capitalList = []
  for l in new_id:
    if l.isupper():
      capitalList.append(l)

  before = ""
  after = ""
  if len(capitalList) == 0:
    print("1단계 변화 없습니다")
  else:
    for i in range(len(capitalList)):
      # 마지막 항목은 이/가, 으로/로
      if i == len(capitalList) - 1:
        if capitalList[i] == 'M' or capitalList[i] == 'N':
          before = before + capitalList[i] + "이"
          after = after + capitalList[i].lower() + "으로"

        elif capitalList[i] == 'L' or capitalList[i] == 'R':
          before = before + capitalList[i] + "이"
          after = after + capitalList[i].lower() + "로"
        else:
          before = before + capitalList[i] + "가"
          after = after + capitalList[i].lower() + "로"
      # 와/과
      else:
        if capitalList[i] == 'L' or capitalList[i] == 'M' or capitalList[i] == 'N' or capitalList[i] == 'R':
          before = before + capitalList[i] + "과 "
          after = after + capitalList[i].lower() + "과 "
        else:
          before = before + capitalList[i] + "와 "
          after = after + capitalList[i].lower() + "와 "

    print("1단계 대문자 ", end="")
    print(before, end="")
    print(" ", end="")
    print(after, end="")
    print(" 바뀌었습니다.")

  return new_id.lower()

def solution(new_id):
  # stage 1
  print("Enter stage 1")
  new_id = stage1(new_id);

  print(new_id)
  # stage 2
  # stage 3
  # stage 4
  # stage 5
  # stage 6
  # stage 7

  answer = ''
  return answer

solution("...!@BaT#*..y.abcdefghijklm")

# solution("z-+.^.")
# solution("=.=")
# solution("123_.def")
# solution("abcdefghijklmn.p")