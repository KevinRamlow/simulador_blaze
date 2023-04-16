import random

sequence_list = []

def sequence(data, bets):
    value = random.randint(0, len(data))
    amount = 1

    while amount <= bets:
        sequence_list.append(data[value])
        value += 1
        amount += 1
    

    return sequence_list


