def solution(a, b):
    answer = ''
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    tmp=3
    i=1
    j=1
    while 1:
        answer = days[(j+tmp)%7]
        if a==i and b==j:
            break
        # print(f'{i}month {j}days {answer}days')
        if (i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12) and j == 31:
            i=i+1
            tmp=(j+tmp)%7
            j=1
        elif (i==2 and j==29):
            i=i+1
            tmp=(j+tmp)%7
            j=1
        elif (i==2 or i==4 or i==6 or i==9 or i==11) and j==30:
            i=i+1
            tmp=(j+tmp)%7
            j=1
        else:
            j=j+1
    return answer

