n = int(input())

def ctoi(char): # char to int
    if char == '.':
        return 0
    return ord(char) - ord("A") + 1

def itoc(integer):  # int to char
    return chr(integer + 64)

tree = [[0,0] for _ in range(n+1)]

for _ in range(n):
    a, b, c = input().split()
    a = ctoi(a)
    b = ctoi(b)
    c = ctoi(c)
    tree[a][0], tree[a][1] = b, c   # tree[a][0] : a의 왼쪽 노드. 1은 오른쪽 노드.

answer1 = ''
answer2 = ''
answer3 = ''
def leftree(tree, root):
    global answer1
    alphabet = itoc(root)
    answer1 = answer1 + alphabet
    if tree[root][0] != 0 :    # 왼쪽 노드가 비어있지 않으면
        leftree(tree, tree[root][0])

    if tree[root][1] != 0 :   # 오른쪽 노드가 비어있지 않으면
        leftree(tree, tree[root][1])

def midtree(tree, root):
    global answer2
    if tree[root][0] != 0 :    # 왼쪽 노드가 비어있지 않으면
        midtree(tree, tree[root][0])
    alphabet = itoc(root)
    answer2 = answer2 + alphabet
    if tree[root][1] != 0 :   # 오른쪽 노드가 비어있지 않으면
        midtree(tree, tree[root][1])

def rightree(tree, root):
    global answer3
    if tree[root][0] != 0 :    # 왼쪽 노드가 비어있지 않으면
        rightree(tree, tree[root][0])
    if tree[root][1] != 0 :   # 오른쪽 노드가 비어있지 않으면
        rightree(tree, tree[root][1])
    alphabet = itoc(root)
    answer3 = answer3 + alphabet

leftree(tree,1)
midtree(tree,1)
rightree(tree,1)

print(answer1, end= '\n')
print(answer2, end= '\n')
print(answer3)