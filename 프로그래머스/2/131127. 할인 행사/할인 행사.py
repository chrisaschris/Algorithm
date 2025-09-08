from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_counter = Counter(dict(zip(want, number)))
    # print(want_counter)
    for i in range(0, len(discount)-9):
        wantdis_counter = Counter(discount[i:i+10])
        # print(want_counter, wantdis_counter)
        if want_counter == wantdis_counter:
            answer = answer + 1
    return answer