# A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive
# two months prior.

# This program uses a modified fibonacci sequence to calculate the total number of rabbit paris if each rabbit
# produces the specified number of pairs in each litter (litters_in_pairs)


def calculate_wabbits(months, litters_in_pairs):
    # total_rabbit_pairs_list assumes starting at month 1 with only 1 pair.
    total_rabbit_pairs_list = [1, 1, litters_in_pairs + 1]
    months = list(range(1, months))
    for month in months:
        if month == 1 or month == 2:
            pass
        else:
            # Modified fibonacci sequence, taking the pairs of rabbits two months ago, multiplied by litters_in_pairs
            total_rabbit_pairs = total_rabbit_pairs_list[month - 1] + (total_rabbit_pairs_list[month - 2] * litters_in_pairs)
            total_rabbit_pairs_list.append(total_rabbit_pairs)
            print(total_rabbit_pairs_list)
    return total_rabbit_pairs_list[months[-1]]


print(calculate_wabbits(5, 5))
