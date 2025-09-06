from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    counts = sorted(counter.values(), reverse=True)

    total = 0
    for i, c in enumerate(counts):
        total += c
        if total >= k:
            return i + 1