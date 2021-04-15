from .requests_yfinance import (
    request_chart_data,
    request_info1_data,
    request_info2_data
)

from .data_extractor import (
    extract_chart_data,
    extract_info1_data,
    extract_info2_data
)


class YFAPI:

    def __init__(self, symbol: str):
        symbol = symbol.upper()
        symbol = symbol.replace(".", "-")
        self.__symbol = symbol
        self.__price = None
        self.__dividend = None
        self.__stocksplit = None
        self.__info = None
        self.__type = None

    def price(self) -> dict:
        """
        Get historical price.
        """
        if self.__price == None:
            self.__get_chart_data()
        return self.__price

    def dividend(self) -> dict:
        """
        Get dividend.
        """
        if self.__dividend == None:
            self.__get_chart_data()
        return self.__dividend

    def stocksplit(self) -> dict:
        """
        Get stock split.
        """
        if self.__stocksplit == None:
            self.__get_chart_data()
        return self.__stocksplit

    def longName(self) -> str:
        """
        Get long name.
        """
        if self.__info == None or not "longName" in self.__info:
            self.__get_info1_data()
        return self.__info["longName"]

    def shortName(self) -> str:
        """
        Get short Name.
        """
        if self.__info == None or not "shortName" in self.__info:
            self.__get_info1_data()
        return self.__info["shortName"]

    def market(self) -> str:
        """
        Get market.
        """
        if self.__info == None or not "market" in self.__info:
            self.__get_info1_data()
        return self.__info["market"]

    def tradeCurrency(self) -> str:
        """
        Get trade currency.
        """
        if self.__info == None or not "currency" in self.__info:
            self.__get_info1_data()
        return self.__info["currency"]

    def financialCurrency(self) -> str:
        """
        Get financial currency.
        """
        if self.__info == None or not "financialCurrency" in self.__info:
            self.__get_info1_data()
        return self.__info["financialCurrency"]

    def marketCap(self) -> int:
        """
        Get market Cap.
        """
        if self.__info == None or not "marketCap" in self.__info:
            self.__get_info1_data()
        return self.__info["marketCap"]

    def sharesOutstanding(self) -> int:
        """
        Get shares outstanding.
        """
        if self.__info == None or not "sharesOutstanding" in self.__info:
            self.__get_info1_data()
        return self.__info["sharesOutstanding"]
    
    def quoteType(self) -> str:
        if self.__info == None or not "quoteType" in self.__info:
            self.__get_info1_data()
        if not self.__info["quoteType"] == None:
            self.__info["quoteType"] = self.__info["quoteType"].lower()
        return self.__info["quoteType"]

    def sector(self) -> str:
        """
        Get sector.
        """
        if self.__info == None or not "sector" in self.__info:
            self.__get_info2_data()
        return self.__info["sector"]

    def industry(self) -> str:
        """
        Get industry.
        """
        if self.__info == None or not "industry" in self.__info:
            self.__get_info2_data()
        return self.__info["industry"]

    def website(self) -> str:
        """
        Get website.
        """
        if self.__info == None or not "website" in self.__info:
            self.__get_info2_data()
        return self.__info["website"]

    def __get_chart_data(self):
        chart = request_chart_data(self.__symbol, 1000)
        data = extract_chart_data(chart)
        self.__price = data["price"]
        self.__dividend = data["dividend"]
        self.__stocksplit = data["stocksplit"]

    def __get_info1_data(self):
        info = request_info1_data(self.__symbol)
        data = extract_info1_data(info)
        if self.__info == None:
            self.__info = {}
        for item in data:
            self.__info[item] = data[item]

    def __get_info2_data(self):
        info = request_info2_data(self.__symbol)
        data = extract_info2_data(info)
        if self.__info == None:
            self.__info = {}
        for item in data:
            self.__info[item] = data[item]
