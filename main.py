import json

import requests

import func_arbitrage

"""
Set Variables
"""
ticker_url = "https://api.poloniex.com/markets/ticker24h"

"""
Step 0: Finding coins which can be traded
Exchange: Poloniex
https://docs.poloniex.com/#introduction
"""
def step_0():
    coin_list = func_arbitrage.get_coin_tickers(ticker_url)

    return coin_list


""" 
Step 1: Structuring Triangular Pairs
Calculation Only
"""
def step_1(coin_list):
    structured_list = func_arbitrage.structure_traingular_pairs(coin_list)

    # Save structured list
    with open("structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)

"""
    Step 2: Calculate Surface Arbitrage Opportunities
    Exchange: Poloniex
    https://docs.poloniex.com/#public-endpoints-reference-data-symbol-information
"""
def step_2(coin_list):
    url = "https://api.exchange.coinbase.com/products/BTC-USD/ticker"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text)





""" MAIN """
if __name__ == "__main__":
    coin_list = step_0()
    # structured_pairs = step_1(coin_list)
    step_2(coin_list)