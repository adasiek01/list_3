def probability(n, k, p):
    def newton(a, b):
        score = 1
        for i in range(1, b + 1):
            score = score * (a - i + 1) / i
        return score
    return sum(i * newton(n, k) * p**i * (1-p)**(n-i) for i in range(0, k))

