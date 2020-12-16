def solution(N, number):
    s = []
    answer = 0
    k = 0
    for i in range(9):
        if i >= 1:
            k = k*10 + N
        s.append([k])

    if N == number:
        answer = 1
        return answer
    s[0] = [0]
    s[1] = [N]  # N을 한번만 이용해서 만들 수 있는 수는 N밖에 없음.

    for i in range(2,9):
        j = 1
        while j<i:
            for x1 in s[j]:
                for x2 in s[i-j]:
                    s[i].append(x1 + x2)
                    s[i].append(x1 - x2)
                    s[i].append(x1 * x2)
                    if x2 != 0:
                        s[i].append((x1 / x2) - (x1 / x2) % 1)
            j = j+1
        if number in s[i]:
            answer = i
            return answer
        s[i] = set(s[i])

    answer = -1
    return answer
