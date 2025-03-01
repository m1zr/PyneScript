# pynescript/ta.py
import pandas as pd
import numpy as np


def sma(series: pd.Series, period: int) -> pd.Series:
    """Simple Moving Average: average of the last 'period' values."""
    return series.rolling(window=period, min_periods=period).mean()


def ema(series: pd.Series, period: int) -> pd.Series:
    """Exponential Moving Average: weighted moving average with exponential decay."""
    return series.ewm(span=period, adjust=False).mean()


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """
    Relative Strength Index: measures the speed and change of price movements.
    Formula: RSI = 100 - (100 / (1 + RS))
    where RS is the ratio of average gains to losses.
    """
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss.replace(0, 1e-10)
    return 100 - (100 / (1 + rs))


def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    """
    Moving Average Convergence Divergence:
      macd_line = EMA(fast) - EMA(slow)
      signal_line = EMA(macd_line)
      histogram = macd_line - signal_line
    """
    ema_fast = ema(series, fast)
    ema_slow = ema(series, slow)
    macd_line = ema_fast - ema_slow
    signal_line = ema(macd_line, signal)
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram


def bollinger_bands(series: pd.Series, period: int = 20, std_multiplier: float = 2.0):
    """
    Bollinger Bands:
      middle_band = sma(series, period)
      upper_band = middle_band + (std_multiplier * standard deviation)
      lower_band = middle_band - (std_multiplier * standard deviation)
    """
    middle_band = sma(series, period)
    std = series.rolling(window=period, min_periods=period).std()
    upper_band = middle_band + std_multiplier * std
    lower_band = middle_band - std_multiplier * std
    return upper_band, middle_band, lower_band


def stochastic(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    k_period: int = 14,
    d_period: int = 3,
):
    """
    Stochastic Oscillator:
      %K = 100 * ((close - lowest_low) / (highest_high - lowest_low))
      %D = sma(%K, d_period)
    """
    lowest_low = low.rolling(window=k_period, min_periods=k_period).min()
    highest_high = high.rolling(window=k_period, min_periods=k_period).max()
    k = 100 * ((close - lowest_low) / ((highest_high - lowest_low) + 1e-10))
    d = sma(k, d_period)
    return k, d


def wma(series: pd.Series, period: int) -> pd.Series:
    """Weighted Moving Average: uses linear weights."""
    weights = pd.Series(range(1, period + 1))

    def weighted_avg(x):
        return (x * weights).sum() / weights.sum()

    return series.rolling(window=period, min_periods=period).apply(
        weighted_avg, raw=True
    )


# Alias for stochastic – some users prefer the name stoch.
def stoch(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    k_period: int = 14,
    d_period: int = 3,
):
    return stochastic(high, low, close, k_period, d_period)


def tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """
    True Range: maximum of (high - low, abs(high - previous close), abs(low - previous close))
    """
    high_low = high - low
    high_prev_close = (high - close.shift()).abs()
    low_prev_close = (low - close.shift()).abs()
    return pd.concat([high_low, high_prev_close, low_prev_close], axis=1).max(axis=1)


def atr(
    high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14
) -> pd.Series:
    """
    Average True Range: rolling average of the True Range.
    """
    tr_val = tr(high, low, close)
    return tr_val.rolling(window=period, min_periods=period).mean()


def cmo(series: pd.Series, period: int) -> pd.Series:
    """
    Chande Momentum Oscillator:
      CMO = 100 * (sum(up) - sum(down)) / (sum(up) + sum(down))
    """
    delta = series.diff()
    up = delta.clip(lower=0).rolling(window=period, min_periods=period).sum()
    down = (-delta.clip(upper=0)).rolling(window=period, min_periods=period).sum()
    return 100 * (up - down) / (up + down + 1e-10)


def dmi(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    period: int = 14,
    smooth: int = 14,
):
    """
    Directional Movement Index (simplified):
      Computes plus and minus DI.
    """
    up_move = high.diff()
    down_move = low.diff().abs()
    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)
    tr_val = tr(high, low, close)
    atr_val = tr_val.rolling(window=period, min_periods=period).mean()
    plus_di = (
        100
        * pd.Series(plus_dm).rolling(window=period, min_periods=period).sum()
        / atr_val
    )
    minus_di = (
        100
        * pd.Series(minus_dm).rolling(window=period, min_periods=period).sum()
        / atr_val
    )
    return plus_di, minus_di


def vwap(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Volume Weighted Average Price:
      VWAP = cumulative(sum(close*volume)) / cumulative(sum(volume))
    """
    pv = close * volume
    cum_pv = pv.cumsum()
    cum_volume = volume.cumsum().replace(0, 1e-10)
    return cum_pv / cum_volume
