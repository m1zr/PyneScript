# pynescript/input.py


def input(value, title=None, type_=None):
    """
    Generic input function.
    In Pine Script, inputs allow the user to set script parameters.
    Here we simply return the default value.
    """
    return value


def input_int(value, title=None):
    return int(value)


def input_float(value, title=None):
    return float(value)


def input_bool(value, title=None):
    return bool(value)


def input_string(value, title=None):
    return str(value)


def input_symbol(value, title=None):
    return str(value)


def input_timeframe(value, title=None):
    return str(value)
