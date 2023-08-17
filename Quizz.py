def discount_calc(price, is_member):
    if is_member == True:
        discount = 0.10 * price
        discounted_amount = price - discount
        return discounted_amount
    else:
        return 0

#*******************************************************************************


def difference(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    difference = max_num - min_num
    return difference
