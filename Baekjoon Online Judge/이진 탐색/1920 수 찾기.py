N = int(input())
a = list(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))

a.sort()    # a를 정렬해서 이분 탐색 할거임!


def binary_search(array,target,start,end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] > target:
        return binary_search(array,target,start,mid-1)
    elif array[mid]== target:
        return mid
    else:
        return binary_search(array,target,mid+1,end)

for x in b:
    if binary_search(a,x,0,N-1) is None:
        print('0', end='\n')
    else:
        print('1',end='\n')
