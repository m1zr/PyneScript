# pynescript/__init__.py
from .__version__ import __version__, __author__

# Core engine and strategy functions:
from .engine import Engine
from .strategy import (
    entry,
    exit,
    order,
    close,
    position_size,
    position_avg_price,
    cancel,
    reset_strategy,
    Strategy,
    set_risk_allow_entry,
    set_risk_max_drawdown,
    set_oca_cancel,
    set_oca_reduce,
    set_commission_value,
    set_commission_percent,
)

# Technical Analysis indicators:
from .ta import (
    sma,
    ema,
    rsi,
    macd,
    bollinger_bands,
    stochastic,
    wma,
    stoch,
    atr,
    tr,
    cmo,
    dmi,
    vwap,
)

# Input functions:
from .input import (
    input,
    input_int,
    input_float,
    input_bool,
    input_string,
    input_symbol,
    input_timeframe,
)

# Built-in helper functions:
from .builtins import nz, iff, na

# Math functions (arithmetic and math operations):
from .math import (
    abs,
    ceil,
    floor,
    round,
    max,
    min,
    pow,
    sqrt,
    log,
    log10,
    exp,
    sin,
    cos,
    tan,
    asin,
    acos,
    atan,
    atan2,
)

# Time and Date functions:
from .time import (
    time as time_func,
    timenow,
    year,
    month,
    dayofmonth,
    dayofweek,
    hour,
    minute,
    second,
    timestamp,
    syminfo,
    session,
)

# Series functions:
from .series import (
    valuewhen,
    change,
    highest,
    lowest,
    highestbars,
    lowestbars,
    sum as sum_series,
    avg,
    stdev,
    variance,
    correlation,
    covariance,
)

# Array functions:
from .array import (
    new_array,
    new_int_array,
    new_float_array,
    new_bool_array,
    new_string_array,
)

# Persistent variable functions:
from .variables import var, varip, set_var

# Color functions:
from .color import rgb, new as new_color, from_gradient

# String functions:
from .string import (
    format,
    tostring,
    tonumber,
    length,
    lower,
    upper,
    contains,
    startswith,
    endswith,
    replace,
)

# Matrix functions:
from .matrix import new_matrix

__all__ = [
    "Engine",
    "entry",
    "exit",
    "order",
    "close",
    "position_size",
    "position_avg_price",
    "cancel",
    "reset_strategy",
    "Strategy",
    "set_risk_allow_entry",
    "set_risk_max_drawdown",
    "set_oca_cancel",
    "set_oca_reduce",
    "set_commission_value",
    "set_commission_percent",
    "sma",
    "ema",
    "rsi",
    "macd",
    "bollinger_bands",
    "stochastic",
    "wma",
    "stoch",
    "atr",
    "tr",
    "cmo",
    "dmi",
    "vwap",
    "input",
    "input_int",
    "input_float",
    "input_bool",
    "input_string",
    "input_symbol",
    "input_timeframe",
    "nz",
    "iff",
    "na",
    "abs",
    "ceil",
    "floor",
    "round",
    "max",
    "min",
    "pow",
    "sqrt",
    "log",
    "log10",
    "exp",
    "sin",
    "cos",
    "tan",
    "asin",
    "acos",
    "atan",
    "atan2",
    "time_func",
    "timenow",
    "year",
    "month",
    "dayofmonth",
    "dayofweek",
    "hour",
    "minute",
    "second",
    "timestamp",
    "syminfo",
    "session",
    "valuewhen",
    "change",
    "highest",
    "lowest",
    "highestbars",
    "lowestbars",
    "sum_series",
    "avg",
    "stdev",
    "variance",
    "correlation",
    "covariance",
    "new_array",
    "new_int_array",
    "new_float_array",
    "new_bool_array",
    "new_string_array",
    "var",
    "varip",
    "set_var",
    "rgb",
    "new_color",
    "from_gradient",
    "format",
    "tostring",
    "tonumber",
    "length",
    "lower",
    "upper",
    "contains",
    "startswith",
    "endswith",
    "replace",
    "new_matrix",
]
