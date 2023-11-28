data = []


multiplier_list = ['8.156,97 x']
def treat_data(multiplier_list):
    for number in multiplier_list:       
        number = number.replace('.', '').replace(' x', '')
        number = float(number.replace(',', '.'))

        data.append(number)
   
    return data

