우선 solution으로 넘기는 파라미터는 패밀리 구성원수, 촌수 관계를 계산하고 싶은 번호(from, to), 직접 연결되는 관계의 수(1촌), 관계가 정리된 이차원 배열 이렇게 넘겨진다.

다음으로 패밀리 구성원수를 n이라 할때 n * n개의 2차원 배열을 만든 뒤 0으로 값을 초기화해준다.
그 다음, 1촌 관계에 있을 때 [부모][자식]의 배열은 -1로 [자식][부모]의 배열은 1로 업데이트한다.

그런 다음 기준점으로부터 recursion 함수를 실행한다. 값이 존재하지 않으면 -1을 리턴하고, 존재한다면 그 안에서 다시 재귀함수를 실행한다. 대신 목표 값이 나오면 바로 1을 리턴해준다. 그 뒤 재귀함수에서 빠져나오면서 리턴된 값이 1이라면 +1을 해주고 아니면 그냥 -1을 리턴한다.