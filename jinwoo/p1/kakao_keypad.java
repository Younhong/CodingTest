public class kakao_keypad {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] numbers = new int[] { 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5 };
		String result = kakao_keypad.findSolution(numbers, "right");

		System.out.println(result);
	}

	public static String findSolution(int[] numbers, String hand) {
		String answer = "";
		int lastXLeftHandPos = 3;
		int lastYLeftHandPos = 0;
		int lastXRightHandPos = 3;
		int lastYRightHandPos = 2;
		
		for(int num : numbers) { 
			if((num==1) || (num==4) ||(num==7)) {
				answer += "L";
				lastYLeftHandPos = 0;
				lastXLeftHandPos = num/3;
			}
			else if((num==3) || (num==6) ||(num==9)) {
				answer += "R";
				lastYRightHandPos = 2;
				lastXRightHandPos = num/3 - 1;
			}
			else {
				int newXPos;
				int newYPos=1;
				if((num == 0)) {
					newXPos=3;
				}
				else{
					newXPos=num/3;
				}
				int leftDistance;
				int rightDistance;
				
				leftDistance = Math.abs(lastYLeftHandPos - newYPos) + Math.abs(lastXLeftHandPos - newXPos);
				rightDistance = Math.abs(lastYRightHandPos - newYPos) + Math.abs(lastXRightHandPos - newXPos);
				System.out.println("l =: "+ leftDistance);
				System.out.println("r =: "+ rightDistance);
				
				if(leftDistance < rightDistance) {
					answer += "L";
					lastYLeftHandPos = newYPos;
					lastXLeftHandPos = newXPos;
				}
				else if(leftDistance > rightDistance) {
					answer += "R";
					lastYRightHandPos = newYPos;
					lastXRightHandPos = newXPos;
				}
				else {
					if(hand.equals("left")) {
						answer += "L";
						lastYLeftHandPos = newYPos;
						lastXLeftHandPos = newXPos;
					}
					else {
						answer += "R";
						lastYRightHandPos = newYPos;
						lastXRightHandPos = newXPos;
					}
				}
			}
		}
		return answer;
	}
}
