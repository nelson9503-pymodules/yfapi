# This script is used to make a request to the Yahoo! Finance REST API Server, and
# get the response in dictionary from the server.

# The data is splited to 3 parts:
#   - Chart Data (including historical price, dividends and stock splits)
#   - Info Data part 1 (about company name, market Cap, shares outstanding, etc.)
#   - Info Data part 2 (about sector, industry, etc.)

import json
import requests


def request_chart_data(symbol: str, max_years: int) -> dict:
    """
    Request chart data. (including histrical price, dividends and stock splits)
    """
    url = "https://query2.finance.yahoo.com/v8/finance/chart/{}?lang=en-US&region=US&events=div%7Csplit&includeAdjustedClose=true&interval=1d&range={}y".format(
        symbol, max_years)
    j = request_to_server(url)
    return j


def request_info1_data(symbol: str) -> dict:
    """
    Request info data part 1. (including name, marketCap, sharesOutstanding...)
    """
    url = "https://query2.finance.yahoo.com/v7/finance/quote?symbols={}".format(
        symbol)
    j = request_to_server(url)
    return j


def request_info2_data(symbol: str) -> dict:
    """
    Request info data part 2. (including sector, industry...)
    """
    url = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/{}?formatted=true&crumb=DNjBp8dU.yQ&lang=en-US&region=US&modules=assetProfile".format(
        symbol)
    j = request_to_server(url)
    return j


def request_to_server(url: str) -> dict:
    """
    Send a request to the Server and get the json response from it.
    """
    retry = 0
    # sometimes, a connection failure will raise.
    # retry 3 times then give up
    while True: 
        try:
            r = requests.get(url)
            j = json.loads(r.text)
            break
        except:
            retry += 1
            if retry == 3:
                j = {}
                break
    return j


def format_symbol(symbol: str) -> str:
    """
    To ensure the symbol is in Yahoo! Finance Style.
    """
    symbol = symbol.upper()
    symbol = symbol.replace("-", ".")
    return symbol
