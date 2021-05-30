#include <iostream>
#include <string>
#include <stack>
// 짝을 지어서 제거하기 때문에 2의 배수가 아니면 지울수가 없다.
// if(s.length() % 2 == 1) return 0;
// st.top() 은 스택이 비어있으면 nullpoint exception을 띄운다.
// 스택도 배열과 비슷하다고 해야하나. 암튼 그렇다.

using namespace std;

int solution(string s)
{
    int answer = -1;
    stack<char> st;
    
    //cout << st.top();
    for(int i=0; i<s.length(); i++){
        if(st.size()>0 && st.top() == s[i]) st.pop();
        else{
            st.push(s[i]);
        }
    }
    if(st.empty())
        answer = 1;
    else answer = 0;
    return answer;
}

int main(){
    int ans = solution("aabbaa");
    cout << ans <<endl;
    return 0;
}
