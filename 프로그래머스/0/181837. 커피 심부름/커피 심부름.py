def solution(order):
    answer = 0
    for i in range(len(order)):
        if 'americano' in order[i] or order[i] == 'anything':
            answer+=4500
        else:
            answer+=5000
    return answer