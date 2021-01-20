import json
import requests
import datetime


def requests_to_yfserver(url: str) -> dict:
    r = requests.get(url)
    j = json.loads(r.text)
    return j


def format_symbol(symbol: str) -> str:
    symbol = symbol.upper()
    symbol = symbol.replace("-", ".")
    return symbol


def timestamp_to_timestring(stamp: int) -> str:
    stamp = int(stamp)
    date = datetime.datetime(1970, 1, 1) + \
        datetime.timedelta(seconds=(stamp))
    date = "{:04d}-{:02d}-{:02d}".format(date.year, date.month, date.day)
    return date
