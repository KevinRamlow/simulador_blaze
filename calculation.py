# Calcular se ganhou ou perdeu
def calculation(sequence_list, betting_bank, crash, money):  
    for c in range(0, len(sequence_list)):
        if crash <= sequence_list[c]:
            betting_bank += money
        else:
            betting_bank -= money

    print(f'Sua banca final foi de: {betting_bank}')
        
    




    
        
