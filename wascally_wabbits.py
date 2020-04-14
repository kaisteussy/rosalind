# A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive
# two months prior.

# This program uses a modified fibonacci sequence to calculate the total number of rabbit pairs in a given period of
# months (months) if each rabbit produces the specified number of pairs in each litter (pairs_in_litter)


def calculate_wabbits(months, pairs_in_litter):
    # total_rabbit_pairs_list assumes starting at month 1 with only 1 pair.
    total_rabbit_pairs_list = [1, 1, pairs_in_litter + 1]
    months = list(range(1, months))
    for month in months:
        if month == 1 or month == 2:
            pass
        else:
            # Modified fibonacci sequence, taking the pairs of rabbits two months ago, multiplied by pairs_in_litter
            total_rabbit_pairs = total_rabbit_pairs_list[month - 1] + (total_rabbit_pairs_list[month - 2] * pairs_in_litter)
            total_rabbit_pairs_list.append(total_rabbit_pairs)
    return total_rabbit_pairs_list[months[-1]]


print(calculate_wabbits(5, 3))
