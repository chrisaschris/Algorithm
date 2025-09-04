def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers) - 1, -1, -1):
        # print(stack)
        while stack and numbers[stack[-1]] <= numbers[i]:
            stack.pop()
        if stack:
            answer[i] = numbers[stack[-1]]
        stack.append(i)
    return answer