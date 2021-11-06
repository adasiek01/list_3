def p(n, k, i):
    def newton(a, b):
        score = 1
        for i in range(1, b + 1):
            score = score * (a - i + 1) / i
        return score
    p = 1/2
    return sum(i for i in range(0, k)) * newton(n, k) * p**i * (1-p)**(n-i)

