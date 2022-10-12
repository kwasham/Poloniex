import func_arbitrage

"""
Step 0: Finding coins which can be traded
Exchange: Poloniex
https://docs.poloniex.com/#introduction
"""
def step_0():
    coin_list = func_arbitrage.get_coin_tickers("https://api.poloniex.com/markets/ticker24h")

    return coin_list

""" 
Step 1: Structuring Triangular Pairs
Calculation Only
"""
def step_1(coin_list):

  structured_list = func_arbitrage.structure_traingular_pairs(coin_list)


""" MAIN """
if __name__ == "__main__":
    coin_list = step_0()
    structured_pairs = step_1(coin_list)
