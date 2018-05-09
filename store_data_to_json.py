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
