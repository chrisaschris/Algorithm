def sums(length, elements, stack):
    for i in range(0, len(elements)):
        total = 0
        # print("i+length", i+length, "length", length)
        if i+length<=len(elements):
            total = sum(elements[i:(i+length)])
        else :
            total = sum(elements)-sum(elements[(i+length)%len(elements):i])
        # for j in range(i, i+length):
        #     total = total + elements[j%len(elements)]
        # print("total", total)
        stack.append(total)
    return stack
def solution(elements):
    answer = 0
    stack = []
    length = len(elements)+1
    for i in range(1, length):
        sums(i, elements, stack)
    answer = len(list(set(stack)))
    return answer