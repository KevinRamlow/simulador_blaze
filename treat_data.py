data = {}

def treat_data(multiplier_dict):
    c = 0
    
    for element in multiplier_dict:
        multiplier = float(element.text.replace(' x', ''))
        data[c] = multiplier
        c += 1

    return data