import math

def solution(numbers, hand):
    answer = ''
    # 11 -> '*', 12 -> '#'
    lastXLeftHandPos = 3
    lastYLeftHandPos = 0
    lastXRightHandPos = 3
    lastYRightHandPos = 2

    for number in numbers:
      if (number==1 or number==4 or number==7):
        answer += 'L'
        lastXLeftHandPos = int(number / 3)
        lastYLeftHandPos = 0

      elif (number==3 or number==6 or number==9):
        answer += 'R'
        lastXRightHandPos = int(number / 3 - 1)
        lastYRightHandPos = 2
           
      else:
        if (number==0):
          newXPos = 3
        else:
          newXPos = int(number / 3)
        newYPos = 1

        leftDistance = math.pow(newXPos - lastXLeftHandPos, 2) + math.pow(newYPos - lastYLeftHandPos, 2)
        rightDistance = math.pow(newXPos - lastXRightHandPos, 2) + math.pow(newYPos - lastYRightHandPos, 2)

        if (leftDistance < rightDistance):
          answer += 'L'
          lastXLeftHandPos = newXPos
          lastYLeftHandPos = 1
        elif (leftDistance > rightDistance):
          answer += 'R'
          lastXRightHandPos = newXPos
          lastYRightHandPos = 1
        else:
          if (hand == 'left'):
            answer += 'L'
            lastXLeftHandPos = newXPos
            lastYLeftHandPos = 1
          else:
            answer += 'R'
            lastXRightHandPos = newXPos
            lastYRightHandPos = 1

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print("----")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print("----")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))