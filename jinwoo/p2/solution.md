Hashmap 을 사용하여 푸는 문제이다.
key, value 값이 보이면 Hashmap문제라고 생각하면 된다.

1) map에서 같은 key값이 들어오면 기존에 있던 key는 대체되고 새로운 key-value pair가 들어가게 된다. (Enter, Change 경우에 새로운 userid-username을 넣으면 기존에 있던 userid에 해당하는 username이 수정이 되는 형식이다.)
2) split을 사용하여 String을 공백기준으로 나눈다. 
3) Enter, Leave의 경우에만 정답으로 넣고 싶기 떄문에 size를 이때에만 증가시킨다. 