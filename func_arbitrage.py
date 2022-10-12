import requests

def get_coin_tickers(url):
    req = requests.get(url)
    json_resp = req.json()
    return json_resp

#Structure arbitrage pairs
def structure_traingular_pairs(coin_list):

    # Declare Variables
    triangular_pairs_list = []
    remove_duplicates_list = []
    pairs_list = coin_list

    # Get Pair A
    for pair_a in pairs_list:
        pair_a_split = pair_a['symbol'].split('_')
        a_base = pair_a_split[0]
        a_quote = pair_a_split[1]

        #Assign A to a Box
        a_pair_box = [a_base, a_quote]

        #Get Pair B
        for pair_b in pairs_list:
            pair_b_split = pair_b['symbol'].split('_')
            b_base = pair_b_split[0]
            b_quote = pair_b_split[1]

            #Check Pair B
            if pair_b['symbol'] != pair_a['symbol']:
                if b_base in a_pair_box or b_quote in a_pair_box:
                    #Get Pair C
                    for pair_c in pairs_list:
                        pair_c_split = pair_c['symbol'].split('_')
                        c_base = pair_c_split[0]
                        c_quote = pair_c_split[1]

                        #Count the number of matching C items
                        if pair_c['symbol'] != pair_a['symbol'] and pair_c['symbol'] != pair_b['symbol']:
                            combine_all = [pair_a['symbol'], pair_b['symbol'], pair_c['symbol']]
                            pair_box = [a_base, a_quote, b_base, b_quote, c_base, c_quote]

                            counts_c_base = 0
                            for i in pair_box:
                                if i == c_base:
                                    counts_c_base += 1

                            counts_c_quote = 0
                            for i in pair_box:
                                if i == c_quote:
                                    counts_c_quote += 1

                            #Determining Triangular Match
                            if counts_c_base == 2 and counts_c_quote == 2 and c_base != c_quote:
                                print(pair_a['symbol'], pair_b['symbol'], pair_c['symbol'])
