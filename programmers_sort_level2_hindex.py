"""
H-지수 구하는 방법

나의 h는 어떻게 구할 수 있을까? 우측의 표와 같이 자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후,
피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다.

출처: [BRIC Bio통신원] [연구논문을 위한 핵심 10단계] H-지수(H-Index) 란 무엇인가? ( https://www.ibric.org/myboard/read.php?Board=news&id=270333 )
"""


def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)  # clen = 과학자가 발표한 논문 수. n편.
    answer = 0
    for i in range(0, n):
        if i >= citations[i]:
            answer = i
            break
        answer = i + 1      # break문으로 안끝날떄. [2,2]와 같은 반례.

    return answer
