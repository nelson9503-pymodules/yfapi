from . import general_tools


def info_link1(symbol: str) -> str:
    url = "https://query2.finance.yahoo.com/v7/finance/quote?symbols={}".format(
        symbol)
    return url


def info_link2(symbol: str) -> str:
    url = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/{}?formatted=true&crumb=DNjBp8dU.yQ&lang=en-US&region=US&modules=assetProfile".format(
        symbol)
    return url


def info(symbol: str) -> dict:
    symbol = general_tools.format_symbol(symbol)
    url = info_link1(symbol)
    data = general_tools.web_request(url)["quoteResponse"]["result"][0]
    url = info_link2(symbol)
    j = general_tools.web_request(
        url)["quoteSummary"]["result"][0]["assetProfile"]
    for key in j:
        data[key] = j[key]
    return data
