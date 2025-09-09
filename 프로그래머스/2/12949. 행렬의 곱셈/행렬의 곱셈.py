def solution(arr1, arr2):
    answer = [[]]
    ans = []
    for i in range(len(arr1)):
        tmp=[]
        for x in range(len(arr2[0])):
            sums = 0
            for j in range(len(arr1[0])):
                sums += arr1[i][j]*arr2[j][x]
                # print(arr1[i][j], arr2[j][x], sums)
            tmp.append(sums)
            # print(tmp)
        ans.append(tmp)
        # print(ans)
    answer = ans
    return answer