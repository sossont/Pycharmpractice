def solution(phone_book):   #phone_book은 1000000이하 길이의 배열
    lst = sorted(phone_book,key=len)
    pblen = phone_book.__len__()
    for i in range(0,pblen-1):
        for j in range(i+1,pblen):
            if lst[j].startswith(lst[i]):
                answer = False
                return answer
    answer = True
    return answer
