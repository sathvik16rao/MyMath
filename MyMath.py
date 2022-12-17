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

def ranint(a,b):
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
        raise ValueError('Domain of coth_inv is (-∞,-1)u(1,+∞)')

#Universal constants
Z0 = 376.730313668                      #Characteristic impedance of vacuum
G = 6.67430e-11                         #Newtonian constant of gravitation
h = 6.62607015e-34                      #Planck constant
h_eV = 4.135667696e-15                  #Planck constant in eV/Hz
lP = 1.616255e-35                       #Planck length
mP = 2.176434e-8                        #Planck mass
TP = 1.416784e32                        #Planck temperature
tP = 5.391247e-44                       #Planck time
h_bar = 1.054571817e-34                 #reduced Planck constant
c = 299792458                           #Speed of light in vacuum
epsilon0 = 8.8541878128e-12             #Vacuum electric permittivity
mu0 = 1.25663706212e-6                  #Vacuum magnetic permeability

#Electromagnetic constants
muB = 9.2740100783e-24                  #Bohr magneton
muB_eV = 5.7883818060e-5                #Bohr magneton in eV/T
G0 = 7.748091729e-5                     #Conductance quantum
eC = 1.602176634e-19                    #Elementary charge
G0_1 = 12906.40372                      #Inverse of conductance quantum
KJ = 483597.8484e9                      #Josephson constant
phi0 = 2.067833848e-15                  #Magnetic flux quantum
muN = 5.0507837461e-27                  #Nuclear magneton
muN_eV = 3.15245125844e-8               #Nuclear magneton in eV/T
RK = 25812.80745                        #von Klitzing constant

#Atomic and nuclear constants
m_alpha = 6.6446573357e-27              #alpha particle mass (in kg)
M_alpha = 4.0015061777e-3               #alpha particle molar mass (kg/mol)
a0 = 5.29177210903e-11                  #Bohr radius (in m)
re = 2.8179403262e-15                   #classical electron radius (in m)
lambda_c = 2.42631023867e-12            #Compton wavelength (in meter per cycle)




kappa = 2.076647442844e-43              #Einstein gravitational constant
ke = 8.9875517923e9                     #Coulomb constant
kB = 1.380649e23                        #Boltzmann constant
sigma = 5.670374419e-8                  #Stefan–Boltzmann constant
c1 = 3.741771852e-16                    #First radiation constant
c1L = 1.1910429723971884140794892e-16   #First radiation constant for spectral radiance
c2 = 1.438776877e-2                     #Second radiation constant
b = 2.897771955e-3                      #Wien wavelength displacement law constant
b_ = 5.878925757e10                     #Wien frequency displacement law constant
bentropy = 3.002916077e-3               #Wien entropy displacement law constant


