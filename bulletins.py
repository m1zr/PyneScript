# pynescript/builtins.py


def nz(value, replace=0):
    """
    Returns the value if not None/NaN; otherwise returns the 'replace' value.
    """
    if value is None:
        return replace
    try:
        import math

        if isinstance(value, float) and math.isnan(value):
            return replace
    except Exception:
        pass
    return value


def iff(condition, true_val, false_val):
    """
    Ternary operator: returns true_val if condition is True, else false_val.
    """
    return true_val if condition else false_val


def na(x):
    """
    Returns True if x is None or NaN.
    """
    if x is None:
        return True
    try:
        import math

        return math.isnan(x)
    except Exception:
        return False
