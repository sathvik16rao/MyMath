class MathError(Exception):
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return self.string

def add(*number):
    check = [*number]
    if type(check[0])==list:
        l = check[0]
    else:
        l = [*number]
    total = l[0]
    l.pop(0)
    for i in l:
        total = total + i
    return total

def difference(*number):
    check = [*number]
    if type(check[0])==list:
        l = check[0]
    else:
        l = [*number]
    diff = l[0]
    l.pop(0)
    for i in l:
        diff = diff - i
    return diff

def multiply(*number):
    check = [*number]
    if type(check[0])==list:
        l = check[0]
    else:
        l = [*number]
    mul = l[0]
    l.pop(0)
    for i in l:
        mul = mul * i
    return mul

def division(numerator,denominator):
    if denominator == 0:
        raise MathError('Divivsion with zero is not possible.')
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

def factorial(number):
    if number < 0:
        raise MathError("Sorry, factorial does not exist for negative numbers.")
    elif number == 0:
        return 1
    else:
        val = 1
        for i in range(2,number+1):
            val = val * i
        return val

def hcf(*number):
    check = [*number]
    if type(check[0])==list:
        l = check[0]
    else:
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
    check = [*number]
    if type(check[0])==list:
        l = check[0]
    else:
        l = [*number]
    n1 = l[0]
    n2 = l[1]
    lcm_initial = int(int(n1 * n2)/int(hcf(n1,n2)))
    for i in range(2, len(l)):
        lcm_initial = lcm(lcm_initial, l[i])
    return lcm_initial

def sin(x):                                         #x is in radians
    val = 0
    for n in range(51):
       odd = (2*n) + 1
       temp = (((-1)**n)*(x**odd))/factorial(odd)
       val += temp
    return val

def cos(x):                                         #x is in radians
    val = 0
    for n in range(51):
       even = (2*n)
       temp = (((-1)**n)*(x**even))/factorial(even)
       val += temp
    return val

def tan(x):                                         #x is in radians
    return sin(x)/cos(x)

def cot(x):                                         #x is in radians
    return cos(x)/sin(x)

def cosec(x):                                       #x is in radians
    return 1/sin(x)

def sec(x):                                         #x is in radians
    return 1/cos(x)

def sinh(x):                                         #x is in radians
    val = (exp(x) - exp(-x))/2
    return val

def cosh(x):                                         #x is in radians
    val = (exp(x) + exp(-x))/2
    return val

def tanh(x):                                         #x is in radians
    return sinh(x)/cosh(x)

def cosech(x):                                       #x is in radians
    if x != 0:
        return 1/sinh(x)
    else:
        raise MathError('Domain of cosech is R-{0}.')

def sech(x):                                         #x is in radians
    return 1/cosh(x)

def coth(x):                                         #x is in radians
    if x != 0:
        return cosh(x)/sinh(x)
    else:
        raise MathError('Domain of coth is R-{0}.')

def nPr(n,r):
    if n>=r:
        return int(factorial(n)/factorial(n-r))
    else:
        raise MathError('r cannot be greater than n.')

def nCr(n,r):
    if n>=r:
        return int(factorial(n)/((factorial(n-r))*(factorial(r))))
    else:
        raise MathError('r cannot be greater than n.')

def agm(a,b):
    tolerance = 1e-14
    an, bn = a, b
    while abs(an - bn) > tolerance:
        an, bn = (an + bn) / 2, sqroot(an * bn)
    return an

def ln(x):
    if x>0:
        m = 35
        s = x*(2**m)
        val = (pi/(2*(agm(1,4/s))))-(m*0.6931471805599453)
        return val
    else:
        raise MathError('Logarithms of negative number is not defined.')

def log(x):
    if x>0:
        return ln(x)/ln(10)
    else:
        raise MathError('Logarithms of negative number is not defined.')

def logn(x,base):
    if x>0:
        return ln(x)/ln(base)
    else:
        raise MathError('Logarithms of negative number is not defined.')

def antilog(x, base):
    return base**x

def sin_inv(x):                                         #x is in radians
    if x>=-1 or x<=1:
        val = 0
        for n in range(51):
            odd = (2*n)+1
            even = 2*n
            temp = ((factorial(even))/((4**n)*((factorial(n))**2)*odd))*(x**odd)
            val += temp
        return val
    else:
        raise MathError('x cannot be outside the range [-1,1].')

def cos_inv(x):                                         #x is in radians
    if x>=-1 or x<=1:
        return (pi/2) - sin_inv(x)
    else:
        raise MathError('x cannot be outside the range [-1,1].')

def tan_inv(x):                                         #x is in radians
    val = 0
    for n in range(51):
        odd = (2*n)+1
        temp = (((-1)**n)/odd)*(x**odd)
        val += temp
    return val

def cosec_inv(x):                                       #x is in radians
    if x>=1 or x<=-1:
        return sin_inv(1/x)
    else:
        raise MathError('x cannot be in the range (-1,1).')

def sec_inv(x):                                         #x is in radians
    if x>=1 or x<=-1:
        return cos_inv(1/x)
    else:
        raise MathError('x cannot be in the range (-1,1).')

def cot_inv(x):                                         #x is in radians
    if x>0:
        return tan_inv(1/x)
    elif x<0:
        return pi + tan_inv(x)
    else:
        return pi/2

def rand():
    import random
    return random.random()

def ranint(a,b):
    import random
    return random.randint(a,b)

def sinh_inv(x):                                         #x is in radians
    temp = sqroot((x**2)+1)
    val = ln(x + temp)
    return val

def cosh_inv(x):                                         #x is in radians
    if x>=1:
        temp = sqroot((x**2)-1)
        val = ln(x + temp)
        return val
    else:
        raise MathError('Domain of cosh\u207B\u00B9 is [1,∞).')

def tanh_inv(x):                                         #x is in radians
    if -1<x<1:
        temp = (1+x)/(1-x)
        val = (1/2)*ln(temp)
        return val
    else: 
        raise MathError('Domain of tanh\u207B\u00B9 is (-1,1).')

def cosech_inv(x):                                       #x is in radians
    if x!=0:
        temp = sqroot((1/(x**2))+1)
        val = ln((1/x)+temp)
        return val
    else:
        raise MathError('Domain of cosech\u207B\u00B9 is R-{0}.')

def sech_inv(x):                                         #x is in radians
    if 0 < x <= 1:
        temp = sqroot((1/(x**2))-1)
        val = ln((1/x)+temp)
        return val
    else:
        raise MathError('Domain of sech\u207B\u00B9 is (0,1].')

def coth_inv(x):                                         #x is in radians
    if x<-1 or x>1:
        temp = (x+1)/(x-1)
        val = (1/2)*(ln(temp))
        return val
    else:
        raise MathError('Domain of coth\u207B\u00B9 is (-∞,-1)u(1,+∞).')

def radians(x):
    val = pi/180
    return x*val
    
def degrees(x):
    val = 180/pi
    return x*val

def factors(n):
    l=[]
    for i in range(1,n+1):
        if i in l:
            break
        else:
            if n%i==0:
                l.append(i)
                if n/i not in l:
                    l.append(int(n/i))
    return sorted(l)

def summation(function, lower, upper):                  #input a functin only (eg: lambda x: x*2)
    val = 0
    for i in range(lower, upper+1):
        val += function(i)
    return val

def rep_product(function,lower,upper):
    val = []
    val.append(function(lower))
    for i in range(lower+1, upper+1):
        val[0] *= function(i)
    return val[0]

def primefactors(n):
    temp=[]
    while n % 2 == 0:
        temp.append(2)
        n = n / 2
    for i in range(3,int(MyMath.sqroot(n)+1),2):
        while n%i==0:
            temp.append(i)
            n = n / i
    if n > 2:
        temp.append(n)
    return temp

class AP:
    def __init__(self, a, n, d, b, a_n):
        self.a=a
        self.n=n
        self.d=d
        self.b=b
        self.a_n=a_n
    def sum(a, d, n):
        return (n/2)*((2*a)+((n-1)*d))
    def suml(a, n, a_n):
        return (n/2)*(a+a_n)
    def nthterm(a, d, n):
        return a+((n-1)*d)
    def termsnum(a, a_n, d):
        return int(((a_n-a)/d)+1)
    def am(a,b):
        return (a+b)/2

class GP:
    def __init__(self, a, n, r, b, a_n):
        self.a=a
        self.n=n
        self.r=r
        self.b=b
        self.a_n=a_n
    def sum(a, r, n):
        if r != 1 and r<1:
            return (a*(1-(r**(n))))/(1-r)
        elif r!=1 and r>1:
            return (a*((r**(n))-1))/(r-1)
        elif r==1:
            return n*a
    def sum_inf(a,r):
        return a/(1-r)
    def suml(a, r, a_n):
        no = int(ln((a_n/a)-r))
        return (a*(1-(r**(no))))/(1-r)
    def nthterm(a, r, n):
        return a*r**(n-1)
    def gm(a, b):
        return (a*b)**0.5

class Series:
    def __init__(self, n):
        self.n=n
    def sum_n(n):
        if n>0:
            return (n*(n+1))/2
    def sum_n2(n):
        if n>0:
            return (n*(n+1)*(2*n+1))/2
    def sum_n3(n):
        if n>0:
            return ((n*(n+1))/2)**2

class HP:
    def __init__(self, a, n, b, d):
        self.a=a
        self.n=n
        self.b=b
        self.d=d
    def nthtermh(a,d,n):
        return 1/(a + (n-1)*d)
    
    def sumh(a,d,n):
        return (1/d)*(ln((2*a)+ (n-1)*d))

    def hm(a,b):
        return ((2*a*b)/(a + b))

class AGP:
    def __init__(self, a, n, r, d):
        self.a=a
        self.n=n
        self.r=r
        self.d=d
    def nthterm(a,d,r,n):
        if r == 1:
            return n/2*((2*a)+((n-1)*d))
        else:
            return a/(1-r) + ((d*r)(1-(r(n-1)))/(1-r)) - ((a + ((n-1)*d)*(r*n))/(1-r))

    def sum_inf(a,d,r):
        return a/(1-r) + ((d*r)/(1-r)**2)

