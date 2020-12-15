import math

isused = []
nlist = []
usednum = []
answer = 0

def isPrime(x): # 제곱근까지만 보고 소수를 판별하는 함수
    global answer
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x))+1): # 2부터 제곱근까지의 모든 수를 확인
        if x % i == 0:  # 소수가 아님
            return False
    answer += 1


def P(numbers, nlen, size):
    global isused
    global nlist
    global usednum
    for i in range(nlen):
        if size <= nlen:  # size = 자리 수. 아직 자리수를 채우지 못했으면 추가해야징
            if not isused[i]:   # i번째 숫자가 사용 되었는지 확인한다. 중복되면 안되니까?
                nlist.append(numbers[i])
                isused[i] = True
                P(numbers, nlen, size + 1)
                isused[i] = False

    if len(nlist) >= 1:
        new_number = "".join(nlist)
        new_number = int(new_number)
        if not new_number in usednum:
            usednum.append(new_number)
            isPrime(int(new_number)) # 소수인지 판별
        nlist.pop()  # 자리수가 꽉 찼으면 소수인지 판별하고 팝 해야지요.


def solution(numbers):
    global isused
    global answer
    nlen = len(numbers) # 종이 조각의 개수.
    isused = [False] * nlen
    P(numbers,nlen,1)
    return answer