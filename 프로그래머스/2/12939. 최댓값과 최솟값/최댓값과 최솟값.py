# def solution(s):
#     answer = ''
#     num = s.split(' ')
#     # print(num)
#     num_int = [int(x) for x in num]
#     num_int.sort()
#     # print(num_int)
#     answer = f"{num_int[0]} {num_int[-1]}"
#     return answer


def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))