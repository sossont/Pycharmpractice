"""
1. int형 list를 map을 사용하여 string으로 바꿔주고, 리스트로 변환한다.

2. sort가 핵심임.

3. lambda x:x*3은 num인자 각각의 문자열을 3번 반복한다는 것. x*3을 하는 이유? num의 인수값이 1000이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 것.

4. 이건 두고두고 생각좀해봐야겠다...

"""

def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse=True)
    return str(int(''.join(num)))

