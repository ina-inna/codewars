from itertools import combinations

def choose_best_sum(t, k, ls):
    result = list(combinations(ls, k))
    if not result:
        print(None)
    else:
        result.sort(key=sum, reverse=True)
        filtered_list = [x for x in result if sum(x) <= t]
        if not filtered_list:
            print(None)
        else:
            return sum(filtered_list[0])
