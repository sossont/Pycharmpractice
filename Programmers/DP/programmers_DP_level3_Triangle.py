def solution(triangle):
    tlen = len(triangle) #  삼각형 세로 길이. 주석의 i라고 할 수 있다. 0~tlen-1 까지.
    for i in range(1,tlen):
        if i == 1:
            triangle[1][0] += triangle[0][0]
            triangle[1][1] += triangle[0][0]
        else:
            for j in range(0,i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    answer = max(triangle[tlen-1])
    return answer