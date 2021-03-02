""" 예제 입력 1
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
V, E = map(int,input().split())
K = int(input())
graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)


for i in range(E):
    # (u,v,w) : u에서 v로 가는 간선 w가 존재한다.
    u,v,w = map(int,input().split())
    graph[u].append([v,w])


def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))    # heapq에 집어 넣는 것 : (거리, 노드) 쌍.
    distance[start] = 0

    while q:
        # 우선순위 큐에서 가장 거리가 짧은 노드의 (거리,노드) 쌍을 받아온다.
        dist, now = heapq.heappop(q)

        # 그 거리가 테이블표에 있는 거리보다 크면, 즉 갱신이 되지 않는 경우.
        if distance[now] < dist:
            continue

        # i[0] : 도착점 정점. i[1] : 현재 노드에서 그정점까지의 거리.
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(K)
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])