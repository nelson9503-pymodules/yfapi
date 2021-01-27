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
