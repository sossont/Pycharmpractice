T = int(input())
zero = [0 for _ in range(41)]
one = [0 for _ in range(41)]
one[0] = 0
zero[0] = 1
one[1] = 1
zero[1] = 0

inputnum = []
for i in range(2,41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

for _ in range(T):
    inputnum.append(int(input()))

for i in range(T):
    print(zero[inputnum[i]], end=" ")
    print(one[inputnum[i]])
