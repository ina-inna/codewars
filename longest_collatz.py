def longest_collatz(arr):
    counts = []
    
    for i in arr:
        count = 0
        while i != 1:
            if i % 2 == 0:
                i = i/2
            else: 
                i = 3 * i + 1
            count += 1
        counts.append(count)
    max_value = max(counts)
    max_index = counts.index(max_value)   
    return arr[max_index]