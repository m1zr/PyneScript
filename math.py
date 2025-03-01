# pynescript/math.py
import math as m


def abs(x):
    return m.fabs(x)


def ceil(x):
    return m.ceil(x)


def floor(x):
    return m.floor(x)


def round(x):
    return __import__("builtins").round(x)


def max(x, y):
    return x if x > y else y


def min(x, y):
    return x if x < y else y


def pow(base, exponent):
    return m.pow(base, exponent)


def sqrt(x):
    return m.sqrt(x)


def log(x):
    return m.log(x)


def log10(x):
    return m.log10(x)


def exp(x):
    return m.exp(x)


def sin(x):
    return m.sin(x)


def cos(x):
    return m.cos(x)


def tan(x):
    return m.tan(x)


def asin(x):
    return m.asin(x)


def acos(x):
    return m.acos(x)


def atan(x):
    return m.atan(x)


def atan2(y, x):
    return m.atan2(y, x)
