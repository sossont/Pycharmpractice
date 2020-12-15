def solve(a,b,c):
    return (-b + ((b**2 - 4  * a * c) ** 0.5)) / (2*a)

def solution(brown, yellow):
    total = brown + yellow
    M,N = 0,0   # M : 가로, N : 세로
    M = solve(2,-(4+brown),2*total)
    N = total / M
    answer = [int(M),int(N)]
    return answer

solution(10,2)