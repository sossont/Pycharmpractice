"""
A B C D E F G H I J K  L  M  N  O  P  Q  R S T U V W X Y Z    알파벳 26개
0 1 2 3 4 5 6 7 8 9 10 11 12 13 12 11 10 9 8 7 6 5 4 3 2 1

"""

def cal(alphabet):
    return min(ord(alphabet) - ord("A"), ord("Z") - ord(alphabet) + 1)  # A에서 그문자까지 가는데에 걸리는 횟수.

def solution(name):
    answer = 0
    if len(name) == 1:
        answer = cal(name[0])
        return answer

    if name[1] == "A":
        for chr in name:
            answer += cal(chr)

        answer += len(name) - 2
    else:
        for chr in name:
            answer += cal(chr)
        answer += len(name) -1
    return answer