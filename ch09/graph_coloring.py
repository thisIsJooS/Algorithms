# Graph Coloring

def isSafe(graph, vtx, clr, color):   # 유효성 검사
  for i in range(len(graph)):
    if graph[vtx][i] == 1 and color[i] == clr:  # 점 i가 vtx에 인접하고, 색이 같으면
      return False
  return True


def graphColouring(graph, num, states):
  color = [0] * len(graph)
  ret = DFS_graph_coloring(graph, num, 0, color)
  
  if ret:
    for i in range(len(graph)):
      print("%3s = " % states[i], color_name[color[i]])
  else:
    print("그래프를 색칠할 수 없음 ! ")

    
def DFS_graph_coloring(graph, num, vtx, color):
  if vtx == len(graph):  # 색칠 성공
    return True
  
  for c in range(1, num+1):  # 모든 색상에 대해
    if isSafe(graph, vtx, c, color):
      color[vtx] = c
      if DFS_graph_coloring(graph, num, vtx+1, color):
        return True
      color[vtx] = 0
  
  return False  # 정점 색칠 실패

# 알고리즘 테스트
states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
graph = [
  [0, 1, 1, 1, 0, 0],
  [1, 0, 0, 1, 0, 0],
  [1, 0, 0, 1, 1, 0],
  [1, 1, 1, 0, 1, 1],
  [0, 0, 1, 1, 0, 1],
  [0, 0, 0, 1, 1, 0]
]
color_name = ["None", "Red", "Green", "Blue", "Yellow", "Purple"]


print("색상 3개 : ")
graphColouring(graph, 3, states)
print("----------")
print("색상 2개 : ")
graphColouring(graph, 2, states)

######################
# 결과
#
# 색상 3개 :
#  NT =  Red
#  WA =  Green
#   Q =  Green
#  SA =  Blue
# NSW =  Red
#   V =  Green
# ----------
# 색상 2개 :
# 그래프를 색칠할 수 없음 !
######################