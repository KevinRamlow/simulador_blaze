def calculation(sequence_list, betting_bank, crash, money):  
    for c in range(0, len(sequence_list)):
        if crash <= sequence_list[c]:
            betting_bank += money
        else:
            betting_bank -= money

    return betting_bank
        
    




    
        
