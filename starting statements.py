Python 3.2.3 (default, Apr 11 2012, 07:15:24) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 24*7
168
>>> 5+9
14
>>> 22-6
16
>>> 12*14
168
>>> 22/7
3.142857142857143
>>> 2**4
16
>>> 25%7
4
>>> 1+2*3
7
>>> (1+2)*3
9
>>> 8.8**-5.4
7.939507629591553e-06
>>> 2.3e02
230.0
>>> 3.
3.0
>>> 1j
1j
>>> 1j*1j
(-1+0j)
>>> import math
>>> math.sqrt(5)
2.23606797749979
>>> sqrt(5)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    sqrt(5)
NameError: name 'sqrt' is not defined
>>> math.sqrt(5)
2.23606797749979
>>> from math import *
>>> sqrt(5)
2.23606797749979
>>> log(25+5)
3.4011973816621555
>>> 'http'
'http'
>>> "http"
'http'
>>> """http"""
'http'
>>> """
me and my monkey
have something to hide
"""
'\nme and my monkey\nhave something to hide\n'
>>> len('pear')
4
>>> len("")
0
>>> len(" ")
1
>>> 5 + len('cat') * len('dog')
14
>>> 'hot' + 'dog'
'hotdog'
>>> 10 * 'ha'
'hahahahahahahahahaha'
>>> len(12* 'pizza pie
    
SyntaxError: EOL while scanning string literal
len(12* 'pizza pie
>>> 1en(12 * 'pizza pie!')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    en(12 * 'pizza pie!')
NameError: name 'en' is not defined
>>> len(12 * 'pizza pie!')
120
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the hyperbolic arc cosine (measured in radians) of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the hyperbolic arc sine (measured in radians) of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the hyperbolic arc tangent (measured in radians) of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as an int.
        This is the smallest integral value >= x.
    
    copysign(...)
        copysign(x, y)
        
        Return x with the sign of y.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -> Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as an int.
        This is the largest integral value <= x.
    
    fmod(...)
        fmod(x, y)
        
        Return fmod(x, y), according to platform C.  x % y may differ.
    
    frexp(...)
        frexp(x)
        
        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(...)
        fsum(iterable)
        
        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(...)
        gamma(x)
        
        Gamma function at x.
    
    hypot(...)
        hypot(x, y)
        
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isfinite(...)
        isfinite(x) -> bool
        
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(...)
        isinf(x) -> bool
        
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(...)
        isnan(x) -> bool
        
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -> Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    pi = 3.141592653589793

FILE
    (built-in)


>>> print(math.tanh.__doc__)
tanh(x)

Return the hyperbolic tangent of x.
>>> float(3)
3.0
>>> float('3.2')
3.2
>>> str(85)
'85'
>>> str(-9.78)
'-9.78'
>>> #comment
>>> #automatically convert ints to floats
>>> int(8.64)
8
>>> round(8.64)
9
>>> round(8.5)
8
>>> float('5.1')
5.1
>>> fruit = "cherry"
>>> fruit
'cherry'
>>> cost = 2.99
>>> 0.1 * cost
0.29900000000000004
>>> x,y,z = 1, 'two', 3.0
>>> x
1
>>> y
'two'
>>> z
3.0
>>> x, y, z
(1, 'two', 3.0)
>>> x + 's'
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x + 's'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> x, y, z
(1, 'two', 3.0)
>>> x, y, z #tuple
(1, 'two', 3.0)
>>> a, b = 5, 9
>>> a, b
(5, 9)
>>> a, b = b, a
>>> a, b
(9, 5)
>>> #swap
>>> print('jack', 'ate', 'no', 'fat', sep = '.')
    
    
    
