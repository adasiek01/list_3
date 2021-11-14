def ordinary_polynomial_value_calc(coeff, arg):
    value = 0
    count_mult = 0
    count_add = 0
    expo = 1
    for a in coeff[1:]:
        value += a*(arg**expo)
        count_add  += 1
        count_mult += expo
        expo += 1
    value += coeff[0]
    count_add += 1
    return value, count_mult, count_add

if __name__ == "__main__":
    print(ordinary_polynomial_value_calc([1,2,1,6,0,4,-40], -1))
