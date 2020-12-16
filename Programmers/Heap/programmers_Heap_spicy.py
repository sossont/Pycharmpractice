"""
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

1번째 시

def solution(scoville, K):
    nlist = sorted(scoville)
    answer = 0

    if nlist[1] == 0:  #모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우 : 가장 맵지 않은 음식과 두 번째로 맵지 않은 음식의 스코빌 지수가 0일떄.
        answer = -1
        return answer

    while(nlist[0] <= K):
        nlist[1] = nlist[0] + 2 * nlist[1]
        del nlist[0]    # 가장 맵지 않은 음식과 두 번째로 맵지 않은 음식을 섞고, 1번째 인덱스에 저장한다음, 0번째 인덱스를 삭제해준다.
        nlist = sorted(nlist)
        answer += 1

    return answer

코드자체는 에러가 없으나 런타임 에러, 시간 초과가 뜬다. => 에러가 있으니 런타임 에러가 뜨지;
아마도 정렬하고 합치고 다시 정렬하고 하는게 굉장히 비효율적인듯.
원소의 길이가 1,000,000 이하니까, 백만개의 원소를 받으면 엄청난 메모리 소모가 있을 것 같긴 하다.

"""

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)     #scoville 리스트를 힙으로 만든다.


    while 1:

        first = heapq.heappop(scoville) # 가장 맵지 않은 음식.
        if first >= K:  # 모든 음식의 스코빌 지수가 K이상임.
            break

        if len(scoville) <= 0:  # 원소가 하나만 주어졌는데 그게 K보다 낮을 때.
            answer = -1
            return answer

        second = heapq.heappop(scoville)   # 두 번째로 맵지 않은 음식.
        new = first + 2 * second

        if new == 0:    # new가 0이면 스코빌 지수를 K로 절대 못 만든다.
            answer = -1
            return answer

        heapq.heappush(scoville, new)
        answer += 1

    return answer