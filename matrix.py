# pynescript/matrix.py


class Matrix:
    def __init__(self, rows, columns, initial_value=0):
        self._data = [[initial_value for _ in range(columns)] for _ in range(rows)]
        self._rows = rows
        self._columns = columns

    def get(self, row, column):
        return self._data[row][column]

    def set(self, row, column, value):
        self._data[row][column] = value

    def rows(self):
        return self._rows

    def columns(self):
        return self._columns


def new_matrix(rows, columns, initial_value=0):
    return Matrix(rows, columns, initial_value)
