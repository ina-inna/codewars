import pandas as pd


def duplicate_count(text):
    text = text.lower()
    counts = {}
    n = 0
    for i in text:
        counts[i] = counts.get(i, 0) + 1
    counts_data = pd.DataFrame(list(counts.items()), columns=['Character', 'Count'])
    
    letters_greater_than_1 = counts_data[counts_data['Count'] > 1].shape[0]
    
    return letters_greater_than_1
    