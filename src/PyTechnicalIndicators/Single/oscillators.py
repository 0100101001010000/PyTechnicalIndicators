

def money_flow_index(typical_prices: list[float], volume: list[int]) -> float:
    """
    Calculates the money flow index from the typical price and volume

    The length of typical prices and volume has to be 14 periods in length, if a custom period is wanted,
    personalised_money_flow_index should be used
    :param typical_prices: List of typical prices
    :param volume: List of volumes
    :return: Returns the money flow index as a float
    """

    if len(typical_prices) != 14 or len(volume) != 14:
        raise Exception(f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be 14 periods in length")

    return personalised_money_flow_index(typical_prices, volume)


def personalised_money_flow_index(typical_prices: list[float], volume: list[int]) -> float:
    """
    Calculates the money flow index from the typical price and volume

    There are no limitation on the period, the period that will be choosen will be that of the length of the lists
    :param typical_prices: List of typical prices
    :param volume: List of volumes
    :return: Returns the money flow index as a float
    """
    typical_price_len = len(typical_prices)

    if typical_price_len != len(volume):
        raise Exception(f"typical_prices ({typical_price_len}) and volume({len(volume)})  need to be of same length")

    raw_money_flow = []

    for i in range(typical_price_len):
        raw_money_flow.append(typical_prices[i] * volume[i])

    positive_money_flow = 0
    negative_money_flow = 0

    for j in range(1, len(raw_money_flow)):
        if raw_money_flow[j] > raw_money_flow[j-1]:
            positive_money_flow += raw_money_flow[j]
        elif raw_money_flow[j] < raw_money_flow[j-1]:
            negative_money_flow += raw_money_flow[j]
        else:
            # TODO: Check if this is correct behaviour
            continue

    if negative_money_flow == 0:
        money_flow_ratio = 100
    else:
        money_flow_ratio = positive_money_flow / negative_money_flow
    mfi = 100 - (100 / (1 + money_flow_ratio))

    return mfi