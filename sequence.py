# Pegar um sequencia aleatoria dos dados
import random

data_list = []
sequence_list = []

def sequence(data, bets):
    for c in data:
        data_list.append(data[c])

    value = random.randint(0, len(data_list))
    amount = 1

    while amount <= bets:
        sequence_list.append(data_list[value])
        value += 1
        amount += 1
    print(sequence_list)
    return sequence_list

