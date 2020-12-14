"""
A B C D E F G H I J K  L  M  N  O  P  Q  R S T U V W X Y Z    알파벳 26개
0 1 2 3 4 5 6 7 8 9 10 11 12 13 12 11 10 9 8 7 6 5 4 3 2 1

알파벳 넘기는 것은 판단하기 굉장히 쉬우나, 조이스틱을 왼쪽 오른쪽 조작하는 경우의 수를 어떻게 판단할 것인지. 이게 핵심이다.

JABAAAAAB
"""


def cal(alphabet):
    return min(ord(alphabet) - ord("A"), ord("Z") - ord(alphabet) + 1)  # A에서 그문자까지 가는데에 걸리는 횟수.

def solution(name):
    answer = 0
    name_len = len(name)
    isA = []
    if name_len == 1:  # name의 길이가 1인 경우.
        answer = cal(name[0])
        return answer

    for a in name:
        if a == "A":
            isA.append(0)
        else:
            isA.append(1)
        answer += cal(a)        # 위아래 움직이는 횟수 먼저 더하자.
    idx = 0

    while 1:
        left, right = 0, 0

        if sum(isA) == 0:
            break
        while isA[idx - left] == 0:
            left += 1
        while isA[idx + right] == 0:
            right += 1

        answer += right if left > right else left
        idx += -left if left < right else right
        isA[idx] = 0
    return answer
