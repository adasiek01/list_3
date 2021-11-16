import math

def newton(a,b):
    newton_symbol = factorial(a)/(factorial(b)*factorial(a-b))
    count_mult = 2*a +1  #a+b+a-b + 1
    return newton_symbol, count_mult



def factorial(a):
    number = 1
    for i in range (2,a+1):
        number *= i
    return number

def expotentation_by_squaring(x,y):
    if y == 0:
        return 1
    if y%2 == 0:
        return pow(expotentation_by_squaring(x,y/2),2)
    else:
        return x*expotentation_by_squaring(x,y-1)

def probability(n,k,p):
    prob = 0
    power = expotentation_by_squaring((1-p),(n-1))
    count_mult = math.log(n,2)
    for i in range (0,k+1):
        element = newton(n,i)[0]*(p**i)
        prob += element
        count_mult += element
    prob *= power
    count_mult += 1
    return prob, count_mult
    
    
if __name__ == "__main__":
    print(factorial(3))
    print(newton(7,3))
    print(probability(10,5,0.2))