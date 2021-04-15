# Since the raw data from Yahoo! Finance Server is a complicated nested dictionary structure,
# this script is some extractors to extract the data from it.


def extract_chart_data(result: dict) -> dict:
    """
    Extract historical price, dividends and stock splits from 
    the Yahoo! Finance raw data.
    """
    data = {
        "price": {},
        "dividend": {},
        "stocksplit": {}
    }
    check = checkif_skip_extract_chart(result)
    if check == False:
        return data
    result = result["chart"]["result"][0]
    data = extract_historical_data(result, data)
    data = extract_dividend_data(result, data)
    data = extract_stock_split(result, data)
    return data


def checkif_skip_extract_chart(result: dict) -> bool:
    """
    Check if no data return from Yahoo! Finance server on chart data.
    """
    if not "chart" in result:
        return False
    if not "result" in result["chart"]:
        return False
    if result["chart"]["result"] == None:
        return False
    if not len(result["chart"]["result"]) > 0:
        return False
    return True


def extract_historical_data(result: dict, data: dict) -> dict:
    """
    Extract historical data.
    """
    if "timestamp" in result:
        stamps = result["timestamp"]
    else:
        stamps = []
    for i in range(len(stamps)):
        stamp = int(stamps[i])
        data["price"][stamp] = {}
        data["price"][stamp]["open"] = result["indicators"]["quote"][0]["open"][i]
        data["price"][stamp]["high"] = result["indicators"]["quote"][0]["high"][i]
        data["price"][stamp]["low"] = result["indicators"]["quote"][0]["low"][i]
        data["price"][stamp]["close"] = result["indicators"]["quote"][0]["close"][i]
        if "adjclose" in result["indicators"]:
            data["price"][stamp]["adjclose"] = result["indicators"]["adjclose"][0]["adjclose"][i]
        data["price"][stamp]["volume"] = result["indicators"]["quote"][0]["volume"][i]
    return data


def extract_dividend_data(result: dict, data: dict) -> dict:
    """
    Extract dividend data.
    """
    if "events" in result and "dividends" in result["events"]:
        for stamp in result["events"]["dividends"]:
            data["dividend"][int(stamp)] = {
                "dividend": result["events"]["dividends"][stamp]["amount"]}
    return data


def extract_stock_split(result: dict, data: dict) -> dict:
    """
    Extract stock split data.
    """
    if "events" in result and "splits" in result["events"]:
        for stamp in result["events"]["splits"]:
            data["stocksplit"][int(stamp)] = {
                "stocksplit": result["events"]["splits"][stamp]["splitRatio"]}
    return data


def extract_info1_data(result: dict) -> dict:
    """
    Extract info part 1 data.
    """
    data = {
        "longName": None,
        "shortName": None,
        "market": None,
        "currency": None,
        "financialCurrency": None,
        "marketCap": None,
        "quoteType": None,
        "sharesOutstanding": None
    }
    check = checkif_skip_extract_info1(result)
    if check == False:
        return data
    result = result["quoteResponse"]["result"][0]
    for item in data:
        if item in result:
            data[item] = result[item]
    return data


def checkif_skip_extract_info1(result: dict) -> bool:
    """
    Check if no data return from Yahoo! Finance on info part 1.
    """
    if not "quoteResponse" in result:
        return False
    if not "result" in result["quoteResponse"]:
        return False
    if not len(result["quoteResponse"]["result"]) > 0:
        return False
    if result["quoteResponse"]["result"] == None:
        return False
    return True


def extract_info2_data(result: dict) -> dict:
    """
    Extract info part 2 data.
    """
    data = {
        "sector": None,
        "industry": None,
        "website": None
    }
    check = checkif_skip_extract_info2(result)
    if check == False:
        return data
    result = result["quoteSummary"]["result"][0]["assetProfile"]
    for item in data:
        if item in result:
            data[item] = str(result[item]).replace(
                "—", "-").replace("â€”", "-")
    return data


def checkif_skip_extract_info2(result: dict) -> bool:
    """
    Check if no data return from Yahoo! Finance server on info part 2.
    """
    if not "quoteSummary" in result:
        return False
    if not "result" in result["quoteSummary"]:
        return False
    if result["quoteSummary"]["result"] == None:
        return False
    if not len(result["quoteSummary"]["result"]) > 0:
        return False
    if not "assetProfile" in result["quoteSummary"]["result"][0]:
        return False
    return True
