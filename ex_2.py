def horner(polynomial, n, x):
    score = polynomial[0]
    for i in range(1, n):
        score = score * x + polynomial[i]

    return score


if __name__ == "__main__":
    print(horner((2, -6, 2, -1), 4, 1))
