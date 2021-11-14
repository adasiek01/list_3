def smart_polynomial_value_calc(coeff, arg):
    count_mult = 0
    count_add = 0
    if len(coeff) == 1:
        value = coeff[0]
    else:
        coeff.reverse()
        value = coeff[0]*arg+coeff[1]
        expo = 2
        count_mult += 1
        count_add += 1
        for i in coeff[2:]:
            value = value*arg+coeff[expo]
            expo += 1
            count_mult += 1
            count_add += 1
    return value, count_mult, count_add

if __name__ == "__main__":
    print(smart_polynomial_value_calc([1,0,-4,3,1],2))