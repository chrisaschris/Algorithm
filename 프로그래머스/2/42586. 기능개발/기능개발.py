def solution(progresses, speeds):
    answer = []
    index = 0
    count = 0
    while(index<len(progresses)):
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
        # print(progresses)
        while(index<len(progresses) and progresses[index]>=100):
            index+=1
            count+=1
        if count>0:
            answer.append(count)
            count=0
        # if progresses[0]==100:
        #     break
    return answer