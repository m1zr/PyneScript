# pynescript/series.py
import pandas as pd
import numpy as np


def valuewhen(condition, source, occurrence):
    """
    Returns the value from 'source' when 'condition' was true for the given occurrence (1=most recent).
    The function iterates over the boolean condition list and returns the corresponding source value.
    """
    indexes = [i for i, cond in enumerate(condition) if cond]
    if len(indexes) >= occurrence:
        return source[indexes[-occurrence]]
    else:
        return None


def change(series: pd.Series) -> pd.Series:
    """Returns the difference between current and previous value."""
    return series.diff()


def highest(series: pd.Series, length: int) -> pd.Series:
    """Returns the highest value over the given window."""
    return series.rolling(window=length, min_periods=length).max()


def lowest(series: pd.Series, length: int) -> pd.Series:
    """Returns the lowest value over the given window."""
    return series.rolling(window=length, min_periods=length).min()


def highestbars(series: pd.Series, length: int) -> pd.Series:
    """
    Returns the number of bars since the highest value occurred.
    """

    def func(x):
        return length - 1 - np.argmax(x)

    return series.rolling(window=length, min_periods=length).apply(func, raw=True)


def lowestbars(series: pd.Series, length: int) -> pd.Series:
    """
    Returns the number of bars since the lowest value occurred.
    """

    def func(x):
        return length - 1 - np.argmin(x)

    return series.rolling(window=length, min_periods=length).apply(func, raw=True)


def sum(series: pd.Series, length: int) -> pd.Series:
    """Returns the rolling sum over the specified window."""
    return series.rolling(window=length, min_periods=length).sum()


def avg(*series):
    """
    Returns the element-wise average of multiple series.
    Combines the series into a DataFrame and calculates the mean across columns.
    """
    import pandas as pd

    df = pd.concat(series, axis=1)
    return df.mean(axis=1)


def stdev(series: pd.Series, length: int) -> pd.Series:
    """Returns the rolling standard deviation."""
    return series.rolling(window=length, min_periods=length).std()


def variance(series: pd.Series, length: int) -> pd.Series:
    """Returns the rolling variance."""
    return series.rolling(window=length, min_periods=length).var()


def correlation(series1: pd.Series, series2: pd.Series, length: int) -> pd.Series:
    """Returns the rolling correlation between two series."""
    return series1.rolling(window=length, min_periods=length).corr(series2)


def covariance(series1: pd.Series, series2: pd.Series, length: int) -> pd.Series:
    """Returns the rolling covariance between two series."""
    return series1.rolling(window=length, min_periods=length).cov(series2)
