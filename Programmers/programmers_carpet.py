"""
갈색격자수는 8 이상 5000이하

노란색 격자수는 1 이상 2,000,000 이하

카펫의 가로 길이 >= 세로 길이

M(가로) * N(세로) 의 카펫일때,

total = M * N = brown + yellow
N = total / M
2(M+total/M-2)=brown
2M + 2 * total / M - (4+brown) = 0
2M^2 - (4+borwn) * M + 2 *total = 0

2(M+N-2) = brown


(4-yellow + root ((yellow-4)^2 - 4 * 2 * total)) / 4
"""

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