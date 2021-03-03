# 마을 사이에 M개의 단방향 도로, i번째 길을 지나는데 T[i]의 시간을 소비한다.
"""
예제 입력 1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
"""
import sys
import heapq

n, m, x = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
# 1번부터 n번 학생까지.

distance = []
for _ in range(n+1):
    distance.append([INF] * (n+1))

for _ in range(m):
    s,e,ti = map(int,input().split())
    graph[s].append((e,ti))

def dikjstra(start):

    distance[start][start] = 0
    q = []
    heapq.heappush(q,(0,start))    # (거리, 도착점) 쌍

    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[start][i[0]] > cost:
                distance[start][i[0]] = cost

                heapq.heappush(q,(cost,i[0]))

for i in range(1,n+1):
    dikjstra(i)

longtime = 0
for i in range(1,n+1):
    if longtime < distance[i][x] + distance[x][i]:
        longtime = distance[i][x] + distance[x][i]

print(longtime)