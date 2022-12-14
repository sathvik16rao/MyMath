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

def inv(number):
    return number**-1

def abs(number):
    if number>=0:
        return number
    else:
        return number*-1

pi = 3.1415926535897932384626433832795

e = 2.71828182845904523536028747135266

def exp(x):
    val = 0
    for n in range(51):
        temp = (x**n)/factorial(n)
        val += temp
    return val

'''def factorial(number):
    if number < 0:
        raise ValueError("Sorry, factorial does not exist for negative numbers")
    elif number == 0:
        return 1
    else:
        return number*factorial(number-1)'''
def factorial(number):
    if number < 0:
        raise ValueError("Sorry, factorial does not exist for negative numbers")
    elif number == 0:
        return 1
    else:
        val = 1
        for i in range(2,number+1):
            val = val * i
        return val

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

def agm(a,b):
    tolerance = 1e-14
    an, bn = a, b
    while abs(an - bn) > tolerance:
        an, bn = (an + bn) / 2, sqroot(an * bn)
    return an

def ln(x):
    m = 35
    s = x*(2**m)
    val = (pi/(2*(agm(1,4/s))))-(m*0.6931471805599453)
    return val
'''def ln(x):                  #Improve effeciency
    n=100000000
    val = n * ((nthroot(x,n))-1)
    return round(val,8)'''

def log(x):
    return ln(x)/ln(10)

def logn(x,base):
    return ln(x)/ln(base)

def antilog(x, base):
    return base**x

def sin_inv(x):
    if x>=-1 or x<=1:
        val = 0
        for n in range(51):
            odd = (2*n)+1
            even = 2*n
            temp = ((factorial(even))/((4**n)*((factorial(n))**2)*odd))*(x**odd)
            val += temp
        return val
    else:
        raise ValueError('x cannot be outside the range [-1,1]')

def cos_inv(x):
    return (pi/2) - sin_inv(x)

def tan_inv(x):
    val = 0
    for n in range(51):
        odd = (2*n)+1
        temp = (((-1)**n)/odd)*(x**odd)
        val += temp
    return val

def cosec_inv(x):
    if x>=1 or x<=-1:
        return sin_inv(1/x)
    else:
        raise ValueError('x cannot be in the range (-1,1)')

def sec_inv(x):
    if x>=1 or x<=-1:
        return cos_inv(1/x)
    else:
        raise ValueError('x cannot be in the range (-1,1)')

def cot_inv(x):
    if x>0:
        return tan_inv(1/x)
    elif x<0:
        return pi + tan_inv(x)
    else:
        return pi/2

def rand():
    import random
    return random.random()

def rani(a,b):
    import random
    return random.randint(a,b)

def sinh_inv(x):
    temp = sqroot((x**2)+1)
    val = ln(x + temp)
    return val

def cosh_inv(x):
    if x>=1:
        temp = sqroot((x**2)-1)
        val = ln(x + temp)
        return val
    else:
        raise ValueError('Domain of cosh_inv is [1,∞)')

def tanh_inv(x):
    if -1<x<1:
        temp = (1+x)/(1-x)
        val = (1/2)*ln(temp)
        return val
    else: 
        raise ValueError('Domain of cosh_inv is (-1,1)')

def cosech_inv(x):
    if x!=0:
        temp = sqroot((1/(x**2))+1)
        val = ln((1/x)+temp)
        return val
    else:
        raise ValueError('Domain of cosech_inv is R-{0}')

def sech_inv(x):
    if 0 < x <= 1:
        temp = sqroot((1/(x**2))-1)
        val = ln((1/x)+temp)
        return val
    else:
        raise ValueError('Domain of sech_inv is (0,1]')

def coth_inv(x):
    if x<-1 or x>1:
        temp = (x+1)/(x-1)
        val = (1/2)*(ln(temp))
        return val
    else:
        return ValueError('Domain of coth_inv is (-∞,-1)u(1,+∞)')
 