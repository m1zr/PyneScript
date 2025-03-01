# pynescript/strategy.py


class Strategy:
    def __init__(self):
        self.positions = {}  # Active positions by id.
        self.order_history = []  # Log of orders.
        self.equity = 100000  # Starting equity (example).
        self.netprofit = 0
        self.risk = {"allow_entry": True, "max_drawdown": 0.0}
        self.oca = {"cancel": None, "reduce": None}
        self.commission = {"value": 0.0, "percent": 0.0}

    def entry(self, id, qty, direction="long", price=None):
        """
        Opens a new position.
        In Pine Script, strategy.entry() opens a trade.
        """
        self.positions[id] = {"qty": qty, "direction": direction, "entry_price": price}
        self.order_history.append(
            {
                "id": id,
                "action": "entry",
                "qty": qty,
                "direction": direction,
                "price": price,
            }
        )
        print(
            f"[ENTRY] id: {id} | direction: {direction} | qty: {qty} | price: {price}"
        )

    def exit(self, id, qty=None, price=None):
        """
        Closes an open position.
        """
        if id in self.positions:
            position = self.positions[id]
            exit_qty = qty if qty is not None else position["qty"]
            self.order_history.append(
                {"id": id, "action": "exit", "qty": exit_qty, "price": price}
            )
            print(f"[EXIT] id: {id} | qty: {exit_qty} | price: {price}")
            del self.positions[id]
        else:
            print(f"[EXIT] No open position for id '{id}'")

    def order(self, id, qty, order_type="market", price=None, **kwargs):
        """
        Places a generic order.
        """
        self.order_history.append(
            {
                "id": id,
                "action": "order",
                "order_type": order_type,
                "qty": qty,
                "price": price,
                **kwargs,
            }
        )
        print(f"[ORDER] id: {id} | type: {order_type} | qty: {qty} | price: {price}")

    def close(self, id, price=None):
        """Alias for exit()."""
        self.exit(id, price=price)

    def position_size(self, id):
        """Returns the current size of a position."""
        return self.positions.get(id, {}).get("qty", 0)

    def position_avg_price(self, id):
        """Returns the average entry price."""
        return self.positions.get(id, {}).get("entry_price", None)

    def cancel(self, id):
        """Cancels an open order (logs cancellation)."""
        self.order_history.append({"id": id, "action": "cancel"})
        print(f"[CANCEL] id: {id}")

    # Risk and commission settings
    def set_risk_allow_entry(self, value: bool):
        self.risk["allow_entry"] = value

    def set_risk_max_drawdown(self, value: float):
        self.risk["max_drawdown"] = value

    def set_oca_cancel(self, value):
        self.oca["cancel"] = value

    def set_oca_reduce(self, value):
        self.oca["reduce"] = value

    def set_commission_value(self, value: float):
        self.commission["value"] = value

    def set_commission_percent(self, value: float):
        self.commission["percent"] = value


# Global strategy instance.
strategy = Strategy()


def reset_strategy():
    """Resets the global strategy state."""
    global strategy
    strategy = Strategy()


# Convenience functions for use in scripts.
def entry(id, qty, direction="long", price=None):
    return strategy.entry(id, qty, direction, price)


def exit(id, qty=None, price=None):
    return strategy.exit(id, qty, price)


def order(id, qty, order_type="market", price=None, **kwargs):
    return strategy.order(id, qty, order_type, price, **kwargs)


def close(id, price=None):
    return strategy.close(id, price)


def position_size(id):
    return strategy.position_size(id)


def position_avg_price(id):
    return strategy.position_avg_price(id)


def cancel(id):
    return strategy.cancel(id)


def set_risk_allow_entry(value: bool):
    return strategy.set_risk_allow_entry(value)


def set_risk_max_drawdown(value: float):
    return strategy.set_risk_max_drawdown(value)


def set_oca_cancel(value):
    return strategy.set_oca_cancel(value)


def set_oca_reduce(value):
    return strategy.set_oca_reduce(value)


def set_commission_value(value: float):
    return strategy.set_commission_value(value)


def set_commission_percent(value: float):
    return strategy.set_commission_percent(value)
