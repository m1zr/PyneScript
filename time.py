# pynescript/time.py
import datetime


def time(timeframe, session):
    """
    Returns a timestamp adjusted for the given timeframe and session.
    (For this implementation, returns the current system time.)
    """
    return datetime.datetime.now().timestamp()


def timenow():
    return datetime.datetime.now().timestamp()


def year(ts):
    return datetime.datetime.fromtimestamp(ts).year


def month(ts):
    return datetime.datetime.fromtimestamp(ts).month


def dayofmonth(ts):
    return datetime.datetime.fromtimestamp(ts).day


def dayofweek(ts):
    # ISO weekday: Monday=1, Sunday=7.
    return datetime.datetime.fromtimestamp(ts).isoweekday()


def hour(ts):
    return datetime.datetime.fromtimestamp(ts).hour


def minute(ts):
    return datetime.datetime.fromtimestamp(ts).minute


def second(ts):
    return datetime.datetime.fromtimestamp(ts).second


def timestamp(year_val, month_val, day, hour_val, minute_val):
    dt = datetime.datetime(year_val, month_val, day, hour_val, minute_val)
    return dt.timestamp()


class syminfo:
    # In Pine Script, syminfo.timezone returns the chart’s timezone.
    timezone = "UTC"


class session:
    @staticmethod
    def isregular(ctx):
        # For simulation, assume session is always regular.
        return True

    @staticmethod
    def isfirstbar(ctx):
        return ctx.get("bar_index", 0) == 0

    @staticmethod
    def islastbar(ctx, data_length):
        return ctx.get("bar_index", 0) == data_length - 1
