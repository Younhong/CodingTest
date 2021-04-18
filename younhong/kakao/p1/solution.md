solution이라는 함수로 넘기는 파라미터는 두 가지: 숫자 리스트와 왼손잡이인지 오른손잡이인지(hand)를 나타내는 변수

우선 초기 왼손과 오른손의 X, Y 좌표를 지정해준다. 둘 모두 Y 좌표는 3으로 시작하며 왼손 X 좌표는 0, 오른손 X 좌표는 2로 지정을 한다.

우선 1, 4, 7의 경우는 hand의 값에 무관하게 L을 출력하며 3,6,9의 경우에도 hand와는 무관하게 R을 출력한다.
이 경우는 값을 출력하는 동시에 각각의 왼손의 좌표와 오른손의 좌표만 계속 기록을 하도록 한다. Y 좌표는 왼손, 오른손 각각 0, 2로 지정해주고 X 좌표는 각각 3으로 나눈 몫과 3으로 나눈 몫 - 1의 값으로 지정을 해준다.

문제는 2,5,8,0의 경우인데 이 경우에는 두 손의 현재 위치와 새로운 숫자의 위치 사이의 거리를 비교해야 한다.
우선 새로운 값의 좌표를 받아야한다. Y좌표 는 자동으로 1(중앙이니까)이 되고, X 좌표는
숫자를 3으로 나눈 몫이 된다. 단 0의 경우에는 예외적으로 3으로 기록을 한다.

그런 다음 위에서 기록한 왼손과 오른손에 대하여 각각 현재 좌표와 새로운 값의 좌표의 차의 절대값을 더해 왼쪽과의 거리가 더 짧으면 L을, 오른쪽이 짧으면 R을 더해준다. 

이 경우에 또 문제가 생기는건 두 거리가 같을 경우이다. 이럴 때에는 앞에서 파라미터로 넘긴 hand의 값에 따라 Left일 경우 L을 Right일 경우 R을 더해주도록 한다. 이 경우에도 반드시 현재 왼손과 오른손의 좌표를 업데이트해주어야 한다.