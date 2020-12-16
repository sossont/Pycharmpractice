def solution(n, computers):
    isvisited = [False] * n # 0부터 n-1번 컴퓨터를 방문했는지 여부. 네트워크 수를 결정할 때 중요하다.
    answer = 0
    for num in range(n):
        answer += DFS(n,computers,isvisited,num)

    return answer

def DFS(n, computers, isvisited, k):
    if not isvisited[k]:    # 노드(컴퓨터)를 방문한 적이 없다면
        isvisited[k] = True
        for i in range(n):  # 인접해있는지 확인.
            if computers[k][i] == 1 and not isvisited[i]:   # 인접해있고 방문한 적이 없다면
                DFS(n,computers,isvisited,i)    # 방문하자!

        return 1

    return 0