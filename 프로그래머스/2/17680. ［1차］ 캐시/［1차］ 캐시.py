def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        answer = 5 * len(cities)
    else :
        cache=list()
        for i in cities:
            city=i.upper()
            if city in cache :
                cache.remove(city)
                cache.append(city)
                answer=answer-4
            else :
                if len(cache)<cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
            # print(cache)
            answer=answer+5
    return answer