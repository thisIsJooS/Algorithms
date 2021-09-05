# N-Queen : NxN의 체스보드에 N개의 퀸을 놓는다. 어떤 퀸도 다른 퀸을 공격할 수 없다.

def isSafe(board, x, y):  # 유효성 검사
  N = len(board)
  
  for i in range(y):  # 세로 방향 검사
    if board[i][x] == 1: return False
  
  for i, j in zip(range(y-1, -1, -1), range(x-1, -1 ,-1)):  # \ 방향 검사
    if board[i][j] == 1: return False
    
  for i, j in zip(range(y-1, -1, -1), range(x+1, N)):  # / 방향 검사
    if board[i][j] == 1: return False
    
  return True

def solve_N_Queen(board, y):
  N = len(board)
  
  if y == N:
    printBoard(board)
    return
  
  for x in range(N):  #0열부터 N-1열 까지
    if isSafe(board, x, y):
      board[y][x] = 1
      solve_N_Queen(board, y+1)  # 상태공간 트리 탐색
      board[y][x] = 0
      
def printBoard(board):
  print("-----")
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == 1:
        print("Q", end='')
      else:
        print(".", end='')
    print()
  print("-----")
  
N = 4
board = [[0 for _ in range(N)] for _ in range(N)]
solve_N_Queen(board, 0)



##########
# 결과
#
# -----
# .Q..
# ...Q
# Q...
# ..Q.
# -----
# -----
# ..Q.
# Q...
# ...Q
# .Q..
# -----
##########