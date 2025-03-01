# Pynescript

**Write Trading Strategies in Python the Pine Script Way!**

Pynescript is an innovative Python module that brings the simplicity and elegance of Pine Script™ to your favorite Python environment. Whether you're a seasoned trader or a budding developer, Pynescript allows you to craft technical indicators and trading strategies using familiar Pine Script–like functions while leveraging the power of Python’s rich ecosystem, including Pandas and NumPy.

Imagine writing trading logic with functions such as `entry()`, `ema()`, and `rsi()`—all while enjoying the flexibility and performance benefits that Python offers. With Pynescript, you can seamlessly prototype, backtest, and refine your trading ideas without having to learn an entirely new language.

> **Disclaimer:**  
> **Pynescript** closely mimics the behavior and syntax of Pine Script™, but it is an independent, open-source project not affiliated with TradingView. While we have worked hard to replicate Pine Script's functionality, some features may require further refinement. **Use this module at your own risk** and always conduct comprehensive testing before applying any strategy in live trading.

---

## Features

- **Pine Script-like Syntax:** Write trading strategies using familiar function names (e.g., `ps.entry`, `ps.ema`, `ps.rsi`, etc.).
- **Technical Analysis:** Includes popular indicators such as SMA, EMA, RSI, MACD, Bollinger Bands, ATR, and more.
- **Trading Strategy Functions:** Mimics Pine Script strategy functions including order execution, position tracking, and risk management.
- **Additional Utilities:** Offers math, time/date, series, array, color, string, and matrix functions for building custom indicators and scripts.
- **Flexible and Extensible:** Built on top of Python, allowing further enhancements and integration with data science libraries.

---

## Installation

### From PyPI (Future Release)
> *Note: This package is currently in development. You may install from GitHub for now.*

```bash
pip install git+https://github.com/yourusername/pynescript.git
```

## From Source
Clone the repository:
```bash
git clone https://github.com/yourusername/pynescript.git
cd pynescript
```

Install required dependencies:
```bash
pip install -r requirements.txt
```

---

## Dependencies:
Python 3.7+
pandas
numpy
Standard library modules (datetime, math, etc.)

---

# Usage Examples

## Breakout Strategy Example

This example demonstrates a simple breakout strategy that enters a long position when the current close exceeds the highest high of the previous 20 bars.

import pandas as pd
import pynescript as ps

# Example historical data (replace with your data source).

```python
data = pd.DataFrame({
    'open':   [100, 102, 101, 103, 104, 105, 106, 107, 108, 109],
    'high':   [102, 103, 102, 105, 106, 107, 108, 109, 110, 111],
    'low':    [99, 101, 100, 102, 103, 104, 105, 106, 107, 108],
    'close':  [101, 102, 101, 104, 105, 106, 107, 108, 109, 110],
    'volume': [1000, 1100, 1050, 1150, 1200, 1250, 1300, 1280, 1350, 1400]
})

def breakout_strategy(ctx):
    bar = ctx['bar_index']
    if bar < 20:
        return
    highest_high_series = ps.highest(data['high'][:bar+1], length=20)
    highest_high = highest_high_series.iloc[-1]
    current_close = ctx['close']
    if current_close > highest_high:
        ps.entry("Breakout_Long", qty=100, direction='long', price=current_close)
    else:
        ps.exit("Breakout_Long", price=current_close)

engine = ps.Engine(data)
engine.run(breakout_strategy)
```

# High Volatility Detector Example

This example uses the Average True Range (ATR) to detect high volatility. If ATR exceeds a threshold, it prints a message indicating high volatility.

```python
import pandas as pd
import pynescript as ps

data = pd.DataFrame({
    'open':   [100, 101, 99, 102, 103, 104, 105, 107, 108, 109],
    'high':   [102, 103, 101, 104, 105, 107, 108, 109, 111, 112],
    'low':    [98, 99, 97, 100, 101, 102, 103, 105, 106, 107],
    'close':  [101, 102, 100, 103, 104, 105, 107, 108, 110, 111],
    'volume': [1200, 1250, 1230, 1300, 1350, 1400, 1380, 1420, 1450, 1500]
})

VOLATILITY_THRESHOLD = 2.0

def high_volatility_detector(ctx):
    bar = ctx['bar_index']
    if bar < 14:
        return
    atr_series = ps.atr(
        data['high'][:bar+1],
        data['low'][:bar+1],
        data['close'][:bar+1],
        period=14
    )
    current_atr = atr_series.iloc[-1]
    if current_atr > VOLATILITY_THRESHOLD:
        print(f"High volatility detected at bar {bar}: ATR = {current_atr:.2f}")
    else:
        print(f"Normal volatility at bar {bar}: ATR = {current_atr:.2f}")

engine = ps.Engine(data)
engine.run(high_volatility_detector)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your contributions are well documented and tested.

## License
This project is licensed under the MIT License.
