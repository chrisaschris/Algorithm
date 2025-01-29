def solution(s):
    answer = []
    dic = {}
    s=s.replace('{','').replace('}','')
    s=s.split(',')
    # print(s)
    for num in s :
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    # print(dic)
    answer = sorted(dic, key=lambda x : dic[x], reverse=True)
    # print(answer)
    # answer = map(int, answer)
    answer = [int (i) for i in answer]
    return answer