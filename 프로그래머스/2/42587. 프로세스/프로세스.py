def solution(priorities, location):
    answer = 0
    loc = [0]*len(priorities)
    loc[location]=1
    while(len(priorities)):
        if priorities[0]==max(priorities):
            priorities.pop(0)
            answer+=1
            if(loc[0]==1):
                break
            else:
                loc.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
    return answer