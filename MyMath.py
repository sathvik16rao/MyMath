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
    for i in range(3,int(sqroot(n)+1),2):
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
    
    def nthterm(a,d,n):
        return 1/(a + (n-1)*d)
    
    def sum(a,d,n):
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

class Constants:
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
    m_e = 9.1093837015e-31                  #electron mass (in kg)
    M_e = 5.4857990888e-7                   #electron molar mass (kg mol)
    g_d = 0.8574382338                      #deuteron g factor
    mu_g = 4.330735094e-27                  #deuteron magnetic moment (in J/T)
    m_d =  3.3435837724e-27                 #deuteron mass (in kg)
    m_d_u =  2.013553212745                 #deuteron mass (in u)
    M_d = 2.01355321205e-3                  #deuteron molar mass (in kg/mol)
    g_e = -2.00231930436256                 #electron g factor
    gamma_e = 1.76085963023e11              #electron gyromagnetic ratio (in /sT)
    mu_e = -9.2847647043e-24                #electron magnetic moment (in J/T)
    Fcc = 1.1663787e-5                      #Fermi coupling constant (in GeV^-2)
    alpha = 7.2973525693e-3                 #fine-structure constant
    E_h = 4.3597447222071e-18               #Hartree energy (in J)
    alpha_inv = 137.035999084               #inverse fine-structure constant
    g_mu = -2.0023318418                    #muon g factor 
    mu_mu = -4.49044830e-26                 #muon magnetic moment (in J/T)
    m_mu = 1.883531627e-28                  #muon mass (in kg)
    M_mu = 1.134289259e-4                   #muon molar mass (in kg/mol)
    g_n = -3.82608545                       #neutron g factor
    gamma_n = 1.83247171e8                  #neutron gyromagnetic ratio (in /sT)
    mu_n = -9.6623651e-27                   #neutron magnetic moment (in J/T)
    m_n = 1.67492749804e-27                 #neutron mass (in kg)
    M_n = 1.00866491560e-3                  #neutron molar mass (in kg/mol)
    g_p = 5.5856946893                      #proton g factor
    gamma_p = 2.6752218744e8                #proton gyromagnetic ratio (in /sT)
    mu_p = 1.41060679736e-26                #proton magnetic moment (in J/T)
    m_p = 1.67262192369e-27                 #proton mass (in kg)
    M_p = 1.00727646627e-3                  #proton molar mass (in kg/mol)
    qoc = 3.6369475516e-4                   #quantum of circulation (m^2/s)
    R_inf = 10973731.568160                 #Rydberg constant (in meter per cycle)
    m_tau = 3.16754e-27                     #tau mass (in kg)
    M_tau = 1.90754e-3                      #tau molar mass (in kg/mol)
    sigma_e = 6.6524587321e-29              #Thomson cross section (in m^2)

    #Physico-chemical constants
    m_u = 1.66053906660e-27                 #atomic mass constant (in kg)
    N_A = 6.02214076e23                     #Avogadro constant (in mol^-1)
    k_B = 1.380649e-23                      #Boltzmann constant
    F = 96485.33212                         #Faraday constant
    R = 8.314462618                         #molar gas constant
    sigma = 5.670374419e-8                  #Stefan–Boltzmann constant
    b = 2.897771955e-3                      #Wien wavelength displacement law constant
    b_ = 5.878925757e10                     #Wien frequency displacement law constant
    bentropy = 3.002916077e-3               #Wien entropy displacement law constant
    c1 = 3.741771852e-16                    #First radiation constant
    c1L = 1.1910429723971884140794892e-16   #First radiation constant for spectral radiance
    c2 = 1.438776877e-2                     #Second radiation constant

    #Other constants
    kappa = 2.076647442844e-43              #Einstein gravitational constant
    k_e = 8.9875517923e9                    #Coulomb constant