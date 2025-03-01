# pynescript/engine.py
import pandas as pd
from .strategy import reset_strategy


class Engine:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the engine with historical data.
        Data must include at least: 'open', 'high', 'low', 'close'. Optionally, 'volume' and 'timestamp'.
        """
        self.data = data.reset_index(drop=True)
        self.context = {}

    def run(self, script):
        """
        Iterates over each bar (row) in the DataFrame and calls the user-supplied script.
        """
        reset_strategy()  # clear strategy state before each run
        for index, row in self.data.iterrows():
            self.context["bar_index"] = index
            self.context["open"] = row["open"]
            self.context["high"] = row["high"]
            self.context["low"] = row["low"]
            self.context["close"] = row["close"]
            if "volume" in row:
                self.context["volume"] = row["volume"]
            if "timestamp" in row:
                self.context["timestamp"] = row["timestamp"]
            # Call the trading logic provided by the user with the current context.
            script(self.context)
