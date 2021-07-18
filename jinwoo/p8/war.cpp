// BOJ #1303 전쟁-전투 
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int m, n;
char graph[101][101];

int visited[101][101];

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int bfs(int row, int col){
  //if(graph[s][e] == 'X') return 0;
  int count;
  queue <pair<int, int>> q;
  q.push({row,col});
  count = 1;
  char a = graph[row][col];
  //graph[row][col] = 'X';
  visited[row][col] = 1;

  while(!q.empty()){
    int x = q.front().first;
    int y = q.front().second;

    q.pop();

    for(int i=0; i<4; i++){
      int nx = x + dx[i];
      int ny = y + dy[i];

      if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
      if(visited[nx][ny] || graph[nx][ny] != a) continue;

      if(!visited[nx][ny]){
        q.push({nx, ny});
//        graph[nx][ny] = 'X';
          visited[nx][ny] = 1;
        count++;
      }
    }
  }
  return count*count;
}

int main() {

  cin >> m >> n;
//  getchar();
//  for(int i=0; i<m; i++){
//    for(int j=0; j<n; j++){
//        scanf("%1c", &graph[i][j]);
//    }
//      getchar();
//  }
    for(int i=0; i<n; i++){
        cin >> graph[i];
    }
    
  int white=0, black=0;
  for(int i=0; i< n; i++){
      for(int j=0; j<m; j++){
//          if(graph[i][j] == 'X') continue;
          if(visited[i][j] == 1) continue;
          if(graph[i][j] == 'W') {
              white += bfs(i,j);
          }
          if(graph[i][j] == 'B'){
              black += bfs(i,j);
          }
      }
    }
    cout << white <<" "<< black << endl;

}
