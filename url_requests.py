from . import general


def requests_chart(symbol: str, pastYears: int) -> dict:
    url = "https://query2.finance.yahoo.com/v8/finance/chart/{}?lang=en-US&region=US&events=div%7Csplit&includeAdjustedClose=true&interval=1d&range={}y".format(
        symbol, pastYears)
    j = general.requests_to_yfserver(url)
    return j


def requests_info1(symbol: str) -> dict:
    url = "https://query2.finance.yahoo.com/v7/finance/quote?symbols={}".format(
        symbol)
    j = general.requests_to_yfserver(url)
    return j


def requests_info2(symbol: str) -> dict:
    url = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/{}?formatted=true&crumb=DNjBp8dU.yQ&lang=en-US&region=US&modules=assetProfile".format(
        symbol)
    j = general.requests_to_yfserver(url)
    return j
