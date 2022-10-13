import func_arbitrage
import json

# Set Variables
coin_price_url = "https://poloniex.com/public?command=returnTicker"

"""
Step 0: Finding coins which can be traded
Exchange: Poloniex
https://docs.poloniex.com/#introduction
"""


def step_0():
    coin_list = func_arbitrage.get_coin_tickers(coin_price_url)

    return coin_list


""" 
Step 1: Structuring Triangular Pairs
Calculation Only
"""


def step_1(coin_list):
    structured_list = func_arbitrage.structure_triangular_pairs(coin_list)

    # Save structured list
    with open("structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)


"""
    Step 2: Calculate Surface Arbitrage Opportunities
    Exchange: Poloniex
    https://docs.poloniex.com/#public-endpoints-reference-data-symbol-information
"""


def step_2():
    # Get Structured Pairs
    with open("structured_triangular_pairs.json") as json_file:
        structured_pairs = json.load(json_file)

    # Get latest surface prices
    prices_json = func_arbitrage.get_coin_tickers(coin_price_url)

    # Loop through and get structured price information
    for t_pairs in structured_pairs:
        prices_dict = func_arbitrage.get_price_for_t_pair(t_pairs, prices_json)
        surface_arb = func_arbitrage.calc_triangular_arb_surface_rate(t_pairs, prices_dict)


""" MAIN """
if __name__ == "__main__":
    # coin_list = step_0()
    # structured_pairs = step_1(coin_list)
    step_2()
