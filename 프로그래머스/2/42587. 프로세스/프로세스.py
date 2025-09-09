def solution(priorities, location):
    answer = 0
    loc = [0]*len(priorities)
    loc[location]=1
    # print(loc)
    count=0
    # print("first",priorities)
    while(len(priorities)):
        if priorities[0]==max(priorities):
            priorities.pop(0)
            count+=1
            if(loc[0]==1):
                break
            else:
                loc.pop(0)
            # print(priorities)
            # print(loc)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
            # print("changed priorities",priorities)
            # print("changed loc",loc)
    answer = count
    return answer