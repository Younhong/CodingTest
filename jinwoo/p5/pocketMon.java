/*
https://programmers.co.kr/learn/courses/30/lessons/1845?language=java
프로그래머스 폰켓몬 
*/
import java.util.Arrays;
public class pocketMon {
    public static void main(String[] args) {

		int[] monsters = { 
				3,1,2,3
		};

		int result = solution(monsters );
		
		System.out.println(Arrays.toString(result));

	}//main

    public int solution(int[] nums) {
        int answer = 0;
        
        int len = nums.length;
        int prev = 0;
  
        Arrays.sort(nums);
        
        for(int i=0; i<len; i++){
            if(answer==len/2){
                break;
            }
            if(nums[i]!=prev){
                answer++;
                prev = nums[i];
            }
        }
        return answer;
    }
}