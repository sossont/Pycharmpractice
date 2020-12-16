"""
단어는 알파벳 소문자로만 이루어져 있다.

단어의 길이는 3이상 10이하. 모든 단어의 길이는 같다.

words 에는 3개 이상 50개 이하의 단어가 있다!

begin != target

변환할수 없는 경우는 0을 리턴.
"""
minn = 100
def BFS(target,words,isvisited,adj,k,ans):
    global minn
    isvisited[k] = True
    if target == words[k]:  #찾았다!
        if minn > ans:
            minn = ans

    for i in range(len(words)):
        if adj[k][i] and not isvisited[i]:   # 인접하면.
            BFS(target,words,isvisited,adj,i,ans+1)
            isvisited[i] = False

def solution(begin, target, words):
    global minn
    if target not in words: # target이 words에 없으면 변환할 수 없다.
        answer = 0
        return answer
    words.insert(0,begin)   # words에 첫번째에 begin 을 넣는다. 인접한거 판단하게.

    alen = len(begin)   # 단어의 길이
    wlen = len(words)
    adj = []
    for i in range(len(words)):
        adj.append([])  # 인접한지를 판단하게 해주는 이차원 배열 생성.

    for i in range(wlen):
        for j in range(wlen):
            same = 0
            for k in range(alen):
                if words[i][k] != words[j][k]:
                    same += 1
            if same > 1:    # 1번 이상 일치하지 않는다 => 두 글자 이상 다르다.
                adj[i].append(0)
            else:
                adj[i].append(1)
    # 인접한 것 까지 다 완성. 이제 begin에서 시작해서 따라가서 단어가 만들어지는지만 확인하면 된다.
    isvisited = [False] * wlen
    BFS(target,words,isvisited,adj,0,0)
    return minn