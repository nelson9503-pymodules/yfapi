from .general import (
    format_symbol
)
from .url_requests import (
    requests_chart,
    requests_info1,
    requests_info2
)
from .data_extractor import (
    ExtractChart,
    ExtractInfo1,
    ExtractInfo2
)


def query(symbol: str, pastYears: int, disablePrice: bool = False, disableInfo: bool = False) -> dict:

    symbol = format_symbol(symbol)

    data = {
        "info": {},
        "price": {},
        "dividend": {},
        "stocksplit": {}
    }

    if not disablePrice == True:
        result = requests_chart(symbol, pastYears)
        j = ExtractChart(result)
        for item in j:
            data[item] = j[item]

    if not disableInfo == True:
        result = requests_info1(symbol)
        j = ExtractInfo1(result)
        for item in j:
            data["info"][item] = j[item]

        result = requests_info2(symbol)
        j = ExtractInfo2(result)
        for item in j:
            data["info"][item] = j[item]

    return data
