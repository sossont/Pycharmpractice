import sys
import heapq

dx = [1,0,-1,0]
dy = [0,1,0,-1]
INF = int(1e9)
input = sys.stdin.readline
M, N = map(int,input().split())
# (0,0) 부터 (N-1,M-1) 까지로 하자.

maze = []
for _ in range(N):
    a = list(map(int,input().rstrip()))
    maze.append(a)  # 이차원 배열 maze 생성.

dist = [[INF] * M for _ in range(N)]

q = []
dist[0][0] = 0
heapq.heappush(q,(dist[0][0],0,0))
while q:
    dd, y, x = heapq.heappop(q)
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= nx < M and 0<= ny < N:
            if dist[ny][nx] == INF:
                if maze[ny][nx] == 1:  # 벽이 있으면
                    dist[ny][nx] = dist[y][x] + 1
                    heapq.heappush(q,(dist[ny][nx],ny,nx))
                else:
                    dist[ny][nx] = dist[y][x]
                    heapq.heappush(q,(dist[ny][nx],ny,nx))

print(dist[N-1][M-1])