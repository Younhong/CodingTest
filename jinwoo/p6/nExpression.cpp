#include <iostream>
#include <string>
#include <vector>

using namespace std;

int answer = 9;
 
void dfs(int N, int number, int count, int currentNumber){
    if(count >=9)
        return;
    if(number == currentNumber){
        answer = min(count, answer);
        return;
    }
    int tempNumber = 0;
    for(int i=1; i+ count < 9; i++){
        tempNumber = tempNumber * 10 + N;
        dfs(N, number, count+i, currentNumber + tempNumber);
        dfs(N, number, count+i, currentNumber - tempNumber);
        dfs(N, number, count+i, currentNumber * tempNumber);
        dfs(N, number, count+i, currentNumber / tempNumber);
    }
}

int solution(int N, int number) {
    dfs(N, number, 0, 0);
    if(answer == 9)
        return -1;
    return answer;
}

int main(){
//    int answer = solution(2, 22);
//    cout << answer << endl;
    int answer1 = solution(5, 12);
    cout << answer1 << endl;
//    int answer2 = solution(2, 11);
//    cout << answer2 << endl;
//    int answer3 = solution(5, 31168);
//    cout << answer3 << endl;
    return 0;
}
