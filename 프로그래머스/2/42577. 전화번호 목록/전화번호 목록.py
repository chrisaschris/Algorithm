def solution(phone_book):
    answer = True
    phone_book_set = set(phone_book)
    for num in phone_book:
        for i in range(1, len(num)):
            # if num[:i+1].isin(phone_book_set):
            if num[:i] in (phone_book_set):
                answer = False
                break
    return answer