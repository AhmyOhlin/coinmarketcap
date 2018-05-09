import json, os
from coinmarketcap import Market

#print(dir(Market))
coinmarketcap = Market()

def store_data_to_json():
    try:  # does the data structure exist yet? Let's try opening the file...
        with open("Ethereum.json") as feedjson:
            json_data = json.load(feedjson)
    except FileNotFoundError:  # this must be the first execution. Create an empty data structure.
        json_data = {"all_coins": []}

    data = coinmarketcap.ticker(start = 0, limit=99, convert='USD')
    for entity in data:
        print(entity)
        json_data['all_coins'].append(entity)
    print('len', json_data['all_coins'].__len__())

    # overwrite the old json dict with the updated one
    with open('Ethereum.json', "w") as feedjson:
        json.dump(json_data, feedjson, indent=4)
        feedjson.write('\n')

store_data_to_json()

                                                           #Output:                                      
#{
#    "all_coins": [
#        {
#            "id": "bitcoin",
#            "name": "Bitcoin",
#            "symbol": "BTC",
#            "rank": "1",
#            "price_usd": "9295.14",
#            "price_btc": "1.0",
#            "24h_volume_usd": "7307120000.0",
#            "market_cap_usd": "158238483495",
#            "available_supply": "17023787.0",
#            "total_supply": "17023787.0",
#            "max_supply": "21000000.0",
#            "percent_change_1h": "0.64",
#            "percent_change_24h": "0.99",
#            "percent_change_7d": "1.59",
#            "last_updated": "1525868972",
#            "cached": false
#        },
#        {
#            "id": "bitcoin",
#            "name": "Bitcoin",
#            "symbol": "BTC",
#            "rank": "1",
#            "price_usd": "9295.14",
#            "price_btc": "1.0",
#            "24h_volume_usd": "7307120000.0",
#            "market_cap_usd": "158238483495",
#            "available_supply": "17023787.0",
#            "total_supply": "17023787.0",
#            "max_supply": "21000000.0",
#            "percent_change_1h": "0.64",
#            "percent_change_24h": "0.99",
#            "percent_change_7d": "1.59",
#            "last_updated": "1525868972",
#            "cached": true
#        },
# ......
