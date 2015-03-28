from __future__ import division, unicode_literals, print_function
def print_metadata(f):
    def r(*args,**kwargs):
        print (f.__name__ , 'function ')
        print ('Arguments: ', args, kwargs)
        if not f.__doc__ is None:
            print ('Documentation: ', f.__doc__) 
        return f(*args, **kwargs) 
    return r 

@print_metadata
def print_two(A,b):
    """
    Print  A and b 
    """
    print (A, b)

print_two("Hello", "Python")

def mygen():
    """Yield 5 until something else is passed back via send()"""
    a = 5
    while True:
        f = (yield a) #yield a and possibly get f in return
        if f is not None: 
            a = f  

pattern = """
^                   # beginning of string
M{0,4}              # thousands - 0 to 4 M's
(CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                    #            or 500-800 (D, followed by 0 to 3 C's)
(XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                    #        or 50-80 (L, followed by 0 to 3 X's)
(IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                    #        or 5-8 (V, followed by 0 to 3 I's)
$                   # end of string
"""
class kelvin_to_celsius(object):
    def __init__(self, temp):
        self.temperature = temp 
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        if value>=0:
            self._temperature = value
        else:
            raise ValueError("Temperature in Kelvin cannot be below 0")

obj = kelvin_to_celsius(-1)