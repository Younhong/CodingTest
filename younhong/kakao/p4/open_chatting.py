def solution(records):
  answers = []
  userList = []
  nameList = []
  actionList = []
  statusList = []
  
  for record in records:
    if len(record.split(" ")) >  2:
      action, id, name = record.split(" ")
    else:
      action, id = record.split(" ")
  
    if len(name) >= 1 and len(name) <=9:
      # id에 대해 메시지가 처음일때
      if id not in userList:
        if action == "Enter":
          nameList.append(name)
          actionList.append(action)
          userList.append(id)
          statusList.append("In")
        # 첫 입장시 enter가 아니면 아무런 액션 없음
      # 이미 입장했거나 나갔다 들어왔을 때
      else:
        actionList.append(action)
        userList.append(id)

        if action == "Change":
          for i in range(len(userList)-1):
            if id == userList[i]:
              nameList[i] = name
          statusList.append("In")
          nameList.append(name)

        elif action == "Leave":
          for i in range(len(userList)-1):
            if id == userList[i]:
              nameList.append(nameList[i])
              break
          statusList.append("Out")

        # 나갔다 들어온 경우
        else:
          nameList.append(name)
          for i in range(len(userList)):
            if id == userList[i]:
              nameList[i] = name
          statusList.append("In")

  for i in range(len(userList)):
    if actionList[i] == "Enter":
      answers.append(nameList[i] + "님이 들어왔습니다.")
    elif actionList[i] == "Leave":
      answers.append(nameList[i] + "님이 나갔습니다.")
  return answers

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan", "Leave uid1234", "Enter uid1234 Con", "Change uid1234 dddd", "Change uid1234 yyy", "Leave uid1234"]))