def solution(n, words):
    answer = [0,0]
    used_words = []
    used_words.append(words[0])
    for i in range(1,len(words)):
        if words[i] not in used_words and used_words[i-1][-1]==words[i][0]:
            # print(used_words[i-1][-1])
            # print(words[i][0])
            # print(words[i], used_words)
            used_words.append(words[i])
        else:
            answer[0]=i%n+1
            answer[1]=i//n+1
            break
    return answer


# def solution(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#     else:
#         return [0,0]