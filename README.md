# yfapi - Yahoo! Finance API

This api requests the data from Yahoo! Finance REST API.

## Getting Start

```python
import yfapi

query = yfapi.YFAPI("AAPL") # symbol should be in Yahoo! Finance style.

# query historical price
price = query.price()

# query dividend
divid = query.dividend()

# query dividend
split = query.stocksplit()

# query short name
shortname = query.shortName()

# query long name
longName = query.lognName()

# query market
market = query.market()

# query trading currency
tradeCurrency = query.tradeCurrency()

# query financial currency
financialCurrency = query.financialCurrency()

# query market Cap
cap = query.marketCap()

# query share outstanding
shares = query.sharesOutstanding()

# query sector
sector = query.sector()

# query industry
industry = query.industry()

# query website
website = query.website()

```

---
