# 백트래킹을 이용한 순열 생성

def all_permutations(data):
    selected = [False] * len(data)  # 필요한 자료 초기화
    DFS_permutation(data, [], 0, selected)  # 순환 호출 시작


def DFS_permutation(data, sol, level, selected):
    if level == len(data):  # 함수가 끝나는 조건 (탐색이 끝나는 조건)
        print(sol)
        return

    for i in range(len(data)):
        if not selected[i]:  # 아직 사용되지 않았어야 가능한 부분해
            sol.append(data[i])
            selected[i] = True
            DFS_permutation(data, sol, level+1, selected)  # 자식 노드 탐색
            sol.pop()  # 복구 : 부분해에서 꺼냄 / 여기까지 왔다는 건 탐색에 실패했다는 뜻이므로 복구를 하는 것
            selected[i] = False  # 복구 : 이 원소는 사용하지 않음 


all_permutations(['A', 'B', 'C'])


####################
#결과
#
# ['A', 'B', 'C']
# ['A', 'C', 'B']
# ['B', 'A', 'C']
# ['B', 'C', 'A']
# ['C', 'A', 'B']
# ['C', 'B', 'A']
####################



# 파이썬에서는 itertools 모듈에서 순열 생성을 위한 permutations  함수를 제공한다.

# from itertools import permutations
# print(list(permutations(['A','B','C'])))   #순열을 리스트로 만들어 출력