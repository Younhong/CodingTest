//https://programmers.co.kr/learn/courses/30/lessons/42888

import java.util.Arrays;
import java.util.HashMap;

public class Phone {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] numbers = { "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
				"Change uid4567 Ryan" };
		String[] result = Phone.solution(numbers);

		System.out.println(Arrays.toString(result));
	}

	public static String[] solution(String[] record) {
		
		String[] answer = {};
		HashMap <String, String> map = new HashMap<String, String>();
		
		int size=0;
	
		for(String order: record) {
			String[] tokens = order.split(" ");
			
			if(tokens[0].equals("Enter") || tokens[0].equals("Change")) {
				map.put(tokens[1], tokens[2]);
			}
			// Enter, Leave의 경우에만 정답으로 넣고 싶기 떄문에 size를 이때에만 증가시킨다. 
			if (tokens[0].equals("Enter") || tokens[0].equals("Leave")) {
                size++;
            }
		}
		
		answer = new String[size];
		int i=0;
		for(String order: record) {
			String[] tokens = order.split(" ");
			if(tokens[0].equals("Enter")) {
				answer[i++] = map.get(tokens[1])+"님이 들어왔습니다.";
			}
			if(tokens[0].equals("Leave")) {
				answer[i++] = map.get(tokens[1])+"님이 나갔습니다.";
			}
		}		
		
		return answer;
	}

}
