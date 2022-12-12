'''def add(*number):
    l = [*number]
    total = l[0]
    l.pop(0)
    for i in l:
        total = total + i
    return total'''

def add(*number):
    from functools import reduce
    return reduce(lambda a,b:a+b, [*number])

'''def difference(*number):
    l = [*number]
    diff = l[0]
    l.pop(0)
    for i in l:
        diff = diff - i
    return diff'''

def difference(*number):
    from functools import reduce
    return reduce(lambda a,b:a-b, [*number])

'''def multiply(*number):
    l = [*number]
    mul = l[0]
    l.pop(0)
    for i in l:
        mul = mul * i
    return mul'''

def multiply(*number):
    from functools import reduce
    return reduce(lambda a,b:a*b, [*number])

print(add(1,2,3,4,5))
print(difference(1,2,3,4,5))
print(multiply(1,2,3,4,5))

def division(numerator,denominator):
    if denominator == 0:
        raise ValueError('Divivsion with zero is not possible')
    else:
        return numerator/denominator

def square(number):
    return number**2

def cube(number):
    return number**3

def exponent(base, power):
    return base**power

def sqroot(number):
    return number**0.5

def nthroot(number, n):
    return number**(1/n)

pi = 3.1415926535897932384626433832792

e = 2.71828182845904523536028747135266

def exp(x):
    val = 0
    for n in range(51):
        temp = (x**n)/factorial(n)
        val += temp
    return val

def factorial(number):
    if number < 0:
        raise ValueError("Sorry, factorial does not exist for negative numbers")
    elif number == 0:
        return 1
    else:
        return number*factorial(number-1)

def hcf(*number):
    l = [*number]
    n1 = l[0]
    n2 = l[1]
    while n2:
        n1,n2 = n2,n1%n2
    hcf1 = n1
    for i in range(2,len(l)):
        hcf1 = hcf(hcf1, l[i])
    return hcf1

def lcm(*number):
    l = [*number]
    n1 = l[0]
    n2 = l[1]
    lcm_initial = int(int(n1 * n2)/int(hcf(n1,n2)))
    for i in range(2, len(l)):
    	lcm_initial = lcm(lcm_initial, l[i])
    return lcm_initial

def sin(x):
    val = 0
    for n in range(51):
       odd = (2*n) + 1
       temp = (((-1)**n)*(x**odd))/factorial(odd)
       val += temp
    return val

def cos(x):
    val = 0
    for n in range(51):
       even = (2*n)
       temp = (((-1)**n)*(x**even))/factorial(even)
       val += temp
    return val

def tan(x):
    return sin(x)/cos(x)

def cot(x):
    return cos(x)/sin(x)

def cosec(x):
    return 1/sin(x)

def sec(x):
    return 1/cos(x)

def sinh(x):
    val = (exp(x) - exp(-x))/2
    return val
'''def sinh(x):
    val = 0
    for n in range(51):
        odd = (2*n)+1
        temp = (x**odd)/factorial(odd)
        val += temp
    return val'''

def cosh(x):
    val = (exp(x) + exp(-x))/2
    return val
'''def cosh(x):
    val = 0
    for n in range(51):
        even = (2*n)
        temp = (x**even)/factorial(even)
        val += temp
    return val'''

def tanh(x):
    return sinh(x)/cosh(x)

def cosech(x):
    return 1/sinh(x)

def sech(x):
    return 1/cosh(x)

def coth(x):
    return cosh(x)/sinh(x)

def ln(x):                  #Improve effeciency
    n=100000000
    val = n * ((nthroot(x,n))-1)
    return round(val,8)

def nPr(n,r):
    if n>=r:
        return int(factorial(n)/factorial(n-r))
    else:
        raise ValueError('r cannot be less than n')

def nCr(n,r):
    if n>=r:
        return int(factorial(n)/((factorial(n-r))*(factorial(r))))
    else:
        raise ValueError('r cannot be less than n')

