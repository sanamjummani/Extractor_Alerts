from extractor.extractor import Extract


if __name__ == '__main__':
    data_str = [
        "1",
        "BTC",
        "https://production.api.coindesk.com/v2/tb/price/values/BTC?start_date={{ current_date | add_mins(-2) | fmt_date('%Y-%m-%dT%H:%M') }}&end_date={{ current_date | fmt_date('%Y-%m-%dT%H:%M') }}&interval=1m&ohlc=true",
        "JSON",
        "data.entries[-1][-1]",
        "lte",
        "60000",
    ]
    extract = Extract(data_str)