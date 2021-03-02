"""
예제 입력.
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""

import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
n = int(input())    # 도시의 개수.
m = int(input())    # 버스의 개수.
costs = [INF] * (n+1)
busgraph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())    # a : 출발 도시 번호. b : 도착 도시 번호. c: 버스 비용
    busgraph[a].append((b,c))
start, end = map(int, input().split())

def dijkstra(s):
    q = []
    heapq.heappush(q,(0,start)) # (비용, 도시 번호) 쌍.
    while q:
        cost, now = heapq.heappop(q)
        if costs[now] < cost:
            continue

        for i in busgraph[now]:
            # i[0] : 출발점에서 갈 수 있는 지점. i[1] : 그 도시까지의 비용.
            x = cost + i[1]
            if x < costs[i[0]]:
                costs[i[0]] = x
                heapq.heappush(q,(x,i[0]))

dijkstra(start)
print(costs[end])