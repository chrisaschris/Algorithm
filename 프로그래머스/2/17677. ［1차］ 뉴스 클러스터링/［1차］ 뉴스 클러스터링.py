from collections import Counter

def solution(str1, str2):
    answer = 1
    str1_2 = []
    str2_2 = []
    for i in range(0, len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_2.append(str1[i:i+2].upper())
    for i in range(0, len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_2.append(str2[i:i+2].upper())
    # print(str1_2, str2_2)
    s1 = Counter(str1_2)
    s2 = Counter(str2_2)
    inter = sum((s1 & s2).values())
    union = sum((s1 | s2).values())
    if union == 0:
        answer = 65536
    else :
        answer = int(inter/union * 65536)
    return answer