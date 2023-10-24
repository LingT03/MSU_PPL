from functools import reduce
from functools import partial

def f(x): 
    return x*x

def g(x):
    return 2*x

def h(x):
    return x+1

def compose(f1, f2):
    return lambda v: f1(f2(v))

def double(x):
    return 2*x

def inc(x): 
    return x+1

def dec(x):
    return x-1

def compose1(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def area(r,p):
    return r*r*p

circle = partial(area, 3.14)

hgf = compose(h, compose(g, f))
inc_and_double = compose(double, inc)
inc_and_double_and_dec = compose(dec, compose(double, inc))

print(hgf(2))
print(inc_and_double(10))
print(inc_and_double_and_dec(10))
print (circle(r = 1))