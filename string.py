# pynescript/string.py


def format(fmt, *args, **kwargs):
    """
    Returns a formatted string.
    """
    return fmt.format(*args, **kwargs)


def tostring(value):
    """
    Converts a value to string.
    """
    return str(value)


def tonumber(s):
    """
    Converts a string to a float; returns None if conversion fails.
    """
    try:
        return float(s)
    except Exception:
        return None


def length(s):
    return len(s)


def lower(s):
    return s.lower()


def upper(s):
    return s.upper()


def contains(s, sub):
    return sub in s


def startswith(s, prefix):
    return s.startswith(prefix)


def endswith(s, suffix):
    return s.endswith(suffix)


def replace(s, old, new):
    return s.replace(old, new)
