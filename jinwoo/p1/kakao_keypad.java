public class kakao_keypad {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] numbers = new int[] { 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5 };
		String result = kakao_keypad.findSolution(numbers, "right");

		System.out.println(result);
	}

	public static String findSolution(int[] numbers, String hand) {
		StringBuilder answer = new StringBuilder();

		int len = numbers.length;
		int[][] array = new int[12][12];

		int k = 1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 3; j++) {
				array[i][j] = k++;
			}
		}
		array[3][1] = 0;
//        array[3][0]=10; // *
//        array[3][1]=11; // 0
//        array[3][1]=12; // #

		int n = 0;
//        int x,y;
		int lx = 3, ly = 0, rx = 3, ry = 2;
		int ldist = 0, rdist = 0;

		while (0 < len) {
			len--;
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 3; j++) {
					if (array[i][j] == numbers[n]) {
						if ((array[i][j] == 1) || (array[i][j] == 4) || (array[i][j] == 7)) {

							answer.append("L");
							lx = i;
							ly = j;
						} else if ((array[i][j] == 3) || (array[i][j] == 6) || (array[i][j] == 9)) {
							answer.append("R");
							rx = i;
							ry = j;
						} else {// if(array[i][j]==numbers[n]) {
								// x=i;
								// y=j;
//                        	System.out.println(i);
//                        	System.out.println(j);
							ldist = Math.abs(lx - i) + Math.abs(ly - j);
							rdist = Math.abs(rx - i) + Math.abs(ry - j);
//                        	System.out.println(ldist);
//                        	System.out.println(rdist);
							if (ldist < rdist) {
								answer.append("L");
								lx = i;
								ly = j;
							} else if (ldist > rdist) {
								answer.append("R");
								rx = i;
								ry = j;
							} else {
								if (hand.equals("right")) {
									answer.append("R");
									rx = i;
									ry = j;
								} else {
									answer.append("L");
									lx = i;
									ly = j;
								}
							}
						}
					}
				}
			}

			n++;
		}

		String result = answer.toString();
		return result;
	}
}
