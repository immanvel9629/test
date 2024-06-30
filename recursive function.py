def cook(balance_mavvu):
    if balance_mavvu ==1:
        return 1
    else:
        total =1+cook(balance_mavvu-1)
        return total
    
    total_vadai =cook(2)