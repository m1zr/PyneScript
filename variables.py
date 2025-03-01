# pynescript/variables.py

# Simple persistent variable storage.
persistent_vars = {}


def var(name, initial_value):
    """
    Returns a persistent variable.
    If not already defined, initializes it with initial_value.
    """
    if name not in persistent_vars:
        persistent_vars[name] = initial_value
    return persistent_vars[name]


def varip(name, initial_value):
    """
    Similar to var(), but intended for in-place updates.
    """
    if name not in persistent_vars:
        persistent_vars[name] = initial_value
    return persistent_vars[name]


def set_var(name, value):
    persistent_vars[name] = value
