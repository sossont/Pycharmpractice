N, M = map(int,input().split())
tree_height = list(map(int,input().split()))
tree_height.sort()
start = 0
end = max(tree_height)    # 최대 높이는 이 수를 넘길 수 없음
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for height in tree_height:
        if mid < height:
            total += height - mid

    if total < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)

# 나무 자르기 문제. 11~13번 줄에서 모든 나무가 mid 보다 큰지 검사하지 않는 방법을 생각해보자.