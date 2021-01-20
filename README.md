# yfapi - Yahoo! Finance API

Yahoo! Finance API requests the data from the Yahoo! Finance REST API. All the query actions are compacted into one api function. User can get the results in python dictionary.

## Methods Discovery

**func |** query ( symbol: `str`, pastYears: `int`, disablePrice: `bool`, disableInfo: `bool` ) **->** results: `dict`

* symbol is in Yahoo! Finance Style
* pastYears only affacts historical price, dividends and stock splits.
* Users can disable the price query (including price, dividends and stock splits) or disable the info query to speed up the query process.
