def real_numbers(n):
    divisible_by_2 = n // 2
    divisible_by_3 = n // 3
    divisible_by_5 = n // 5

    divisible_by_2_and_3 = n // (2 * 3)
    divisible_by_2_and_5 = n // (2 * 5)
    divisible_by_3_and_5 = n // (3 * 5)

    divisible_by_2_and_3_and_5 = n // (2 * 3 * 5)

    count = n - (divisible_by_2 + divisible_by_3 + divisible_by_5) + \
            (divisible_by_2_and_3 + divisible_by_2_and_5 + divisible_by_3_and_5) - \
            divisible_by_2_and_3_and_5

    return count