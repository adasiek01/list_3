import math


def newton(n, k):
    """
    Function that finds binomial theorem
    :param n: first value
    :param k: second value
    :return: binomial theorem without multiplications
    """
    if k == 0 or k == n:
        return 1
    else:
        return newton(n - 1, k - 1) + newton(n - 1, k)


def expotentation_by_squaring(x, y):
    """
    Function that counts "base to exponent"
    :param x: base
    :param y: exponent
    :return: base to exponent
    """
    if y == 0:
        return 1
    if y % 2 == 0:
        return pow(expotentation_by_squaring(x, y/2), 2)
    else:
        return x*expotentation_by_squaring(x, y-1)


def probability(n, k, p):
    """
    Function that counts probability and number of multiplications
    :param n: amount of trials
    :param k: maximum amount of successes
    :param p: probability of success
    :return: probability and number of multiplications
    """
    prob = 0
    power = expotentation_by_squaring((1-p), n)
    count_mult = math.log(n, 2)
    p_fraction = p/(1-p)
    count_mult += 1
    for i in range(0, k+1):
        element = newton(n, i)*power
        prob += element
        power *= p_fraction
        count_mult += 2
    return prob, count_mult
    
    
if __name__ == "__main__":
    print(newton(7, 3))
    print(probability(8, 5, 0.2))
