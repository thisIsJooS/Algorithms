# 미로탐색 - 백트래킹 

def isSafe(maze, x, y, mark):
  W, H = len(maze[0]), len(maze)

  if x >= 0 and x < W and y >= 0 and y < H:  # 미로 맵 내부 확인
    if maze[y][x] != 0 and mark[y][x] == 0:  # 벽이 아니고, 방문 않음
      return True

  return False


def solve_maze(maze, x, y):
  W, H = len(maze[0]), len(maze)
  
  sol = [[0 for _ in range(W)] for _ in range(H)]  # 해 경로 맵
  mark = [[0 for _ in range(W)] for _ in range(H)]  # 방문 맵

  if DFS_maze(maze, x, y, sol, mark) == False:
    print("출구를 찾을 수 없음")
  else:
    for i in sol : print(i)


def DFS_maze(maze, x, y, sol, mark): 
  if not isSafe(maze, x, y, mark):
    return False  # 백트래킹
  
  mark[y][x] = 1
  sol[y][x] = 1
  if maze[y][x] == 2:
    return True  # 탐색 종료
  
  if DFS_maze(maze, x+1, y, sol, mark) == True : return True
  if DFS_maze(maze, x-1, y, sol, mark) == True : return True
  if DFS_maze(maze, x, y+1, sol, mark) == True : return True
  if DFS_maze(maze, x, y-1, sol, mark) == True : return True
  
  sol[y][x] = 0  # (x,y)는 이제 부분해가 아님 -> sol에서 제거 
  
  return False


maze = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

solve_maze(maze, 3, 0)  # 미로 입구 좌표는 (3, 0)




##########################################
# 결과
#
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0]
# [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0]
# [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
# [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1]
# [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
##########################################