# pynescript/array.py


class Array:
    def __init__(self, initial=None):
        self.data = list(initial) if initial is not None else []

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data[index] = value

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop() if self.data else None

    def size(self):
        return len(self.data)


def new_array(initial=None):
    return Array(initial)


def new_int_array(initial=None):
    return Array(initial)


def new_float_array(initial=None):
    return Array(initial)


def new_bool_array(initial=None):
    return Array(initial)


def new_string_array(initial=None):
    return Array(initial)
