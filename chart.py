from . import general_tools


def chart_link(symbol: str, pastYears: int) -> str:
    """
    Get the link of chart api.
    """
    url = "https://query2.finance.yahoo.com/v8/finance/chart/{}?lang=en-US&region=US&events=div%7Csplit&includeAdjustedClose=true&interval=1d&range={}y".format(
        symbol, pastYears)
    return url


def chart(symbol: str, year: int) -> dict:
    symbol = general_tools.format_symbol(symbol)
    url = chart_link(symbol, year)
    j = general_tools.web_request(url)["chart"]["result"][0]
    data = construct_data()
    data = extract_meta(data, j)
    data = extract_price(data, j)
    data = extract_event(data, j)
    return data


def construct_data() -> dict:
    data = {
        "meta": {},
        "price": {},
        "event": {
            "dividend": {},
            "split": {}
        }
    }
    return data


def extract_meta(data: dict, j: dict) -> dict:
    meta = j["meta"]
    targets = [
        "symbol", "currency", "exchangeName", "instrumentType"
    ]
    for target in targets:
        data["meta"][target] = meta[target]
    data["meta"]["firstTradeDate"] = general_tools.solve_timestamp(
        meta["firstTradeDate"])
    return data


def extract_price(data: dict, j: dict) -> dict:
    stamps = j["timestamp"]
    ops = j["indicators"]["quote"][0]["open"]
    higs = j["indicators"]["quote"][0]["close"]
    lows = j["indicators"]["quote"][0]["low"]
    clos = j["indicators"]["quote"][0]["close"]
    vols = j["indicators"]["quote"][0]["volume"]
    adjclos = j["indicators"]["adjclose"][0]["adjclose"]
    for i in range(len(stamps)):
        data["price"][str(i)] = {
            "date": general_tools.solve_timestamp(stamps[i]),
            "open": ops[i],
            "high": higs[i],
            "low": lows[i],
            "close": clos[i],
            "adjclose": adjclos[i],
            "volume": vols[i]
        }
    return data


def extract_event(data: dict, j: dict) -> dict:
    if not "events" in j:
        return {}
    event = j["events"]
    if "dividends" in event:
        for stamp in event["dividends"]:
            date = general_tools.solve_timestamp(stamp)
            data["event"]["dividend"][date] = event["dividends"][stamp]["amount"]
    if "splits" in event:
        for stamp in event["splits"]:
            date = general_tools.solve_timestamp(stamp)
            data["event"]["split"][date] = event["splits"][stamp]["splitRatio"]
    return data
