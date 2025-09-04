def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        answer = answer + word.capitalize()+ ' '
    answer = answer[:-1]
    return answer