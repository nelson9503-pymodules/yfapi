import json
import requests
import datetime


def format_symbol(symbol: str) -> str:
    """
    Format the symbol to Yahoo! Finance style:
    1. to upper letters
    2. replace "-" to "."
    """
    symbol = symbol.upper()
    symbol = symbol.replace("-", ".")
    return symbol


def web_request(url: str) -> dict:
    """
    Request to the server.
    Server will response json text.
    """
    r = requests.get(url)
    j = json.loads(r.text)
    return j


def solve_timestamp(stamp: int) -> str:
    """
    Convert the timestamp to date.
    """
    stamp = int(stamp)
    date = datetime.datetime.fromtimestamp(stamp)
    date = "{:04d}-{:02d}-{:02d}".format(date.year, date.month, date.day)
    return date
