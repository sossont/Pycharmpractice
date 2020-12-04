"""
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다. => clothes[1] 은 의상의 종류다. 고로 의상의 종류별로 정렬하자.
같은 이름의 의상은 존재하지 않기 때문에 의상의 이름은 중요하지 않다.

스파이가 가진 의상의 수는 1개 이사 30개 이하. 즉, 의상 종류도 최대 30개 짜리라는것.
일단 수학적으로, 경우의 수를 어떻게 계산할까 생각해보자.

만약 3종류의 의상이 3,4,3개가 있다고 하면
1개씩 입을때 3+4+3
2개씩은 3*4 + 3*3 + 4*3
3개씩은 3*4*3
인덱스로 생각해보자
종류가 5개면 [1][2][3][4][5] 니까
[1] + [2] + [3] + [4] + [5] + [1]*[2] + [1]*[3] + ... + [4]*[5] + [1]*[2]*[3] + .... 이런식?

*******

구글링했지만 옷 종류 별로 옷의 개수 + 1 씩 다 곱하고 마지막에 -1
왜냐하면 안입는 거 까지 생각해야해서 +1이고 다 안입는 경우의 수를 하나 뺴주는거다.

"""
def solution(clothes):
    cnum = len(clothes) # 옷의 개수
    ckinds = []
    for i in range(0,cnum):
        ckinds.append(clothes[i][1])    # 옷 종류 추가하는거염
    cset = set(ckinds)
    ckinds = list(cset) # 순서가 상관 없기 때문에 집합으로 중복 제거해주기

    clotheslist = [0] * len(ckinds) # 옷 종류에 따른 옷의 개수 구할건데, 그러기 위해선 배열을 0으로 초기화 시켜줘야

    for i in range(0,cnum):
        clotheslist[ckinds.index(clothes[i][1])] += 1   # 옷 종류별로 옷의 개수 구함.

    answer = 1
    for i in range(0,len(clotheslist)):         # 와.. 수학적 지식... 반성하
        answer *= (clotheslist[i] + 1)

    answer -= 1
    return answer