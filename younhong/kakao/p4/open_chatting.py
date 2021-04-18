def solution(records):
  answers = []
  userList = []
  actionList = []
  nameMap = {}
  
  for record in records:
    if len(record.split(" ")) >  2:
      action, id, name = record.split(" ")
    else:
      action, id = record.split(" ")
  
    if len(name) >= 1 and len(name) <= 10:
      if action == "Enter" or action == "Change":
        actionList.append(action)
        userList.append(id)
        nameMap[id] = name
      else:
        actionList.append(action)
        userList.append(id) 

  for i in range(len(userList)):
    if actionList[i] == "Enter":
      answers.append(nameMap[userList[i]] + "님이 들어왔습니다.")
    elif actionList[i] == "Leave":
      answers.append(nameMap[userList[i]] + "님이 나갔습니다.")
  return answers

print(solution(["Enter uid123 Muzi", "Enter uid123 Prodo", "Enter uid124 Con", "Enter uid000 Ryan"]))