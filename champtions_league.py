def count_wins(winners_list, country):
    count = 0
    for winners in winners_list:
        value_country = winners.get('country')
        if value_country == country:
            count += 1
    return count