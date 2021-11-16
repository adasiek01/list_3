def ordinary_polynomial_value_calc(coeff, arg):
    """
    Function that counts how many multiplications we do to calculate the value of a polynomial of degree n
    :param coeff: list of coefficients of a polynomial (from the smallest to the biggest)
    :param arg: argument of the faction
    :return: value of the polynomial, amount of multiplications, amount of additions
    """
    value = 0
    count_mult = 0
    count_add = 0
    expo = 1
    for a in coeff[1:]:
        value += a*(arg**expo)
        count_add += 1
        count_mult += expo
        expo += 1
    value += coeff[0]
    count_add += 1
    return value, count_mult, count_add


if __name__ == "__main__":
    print(ordinary_polynomial_value_calc([1, 2, 1, 6, 0, 4, -40], -1))
