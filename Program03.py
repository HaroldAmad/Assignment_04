def getuserInput ():
    balance_F = int(input("Amount of money: "))
    appleprice_F = int(input("Price of an apple: "))
    totalapple_F = (balance_F/appleprice_F)
    change_F = (balance_F%appleprice_F)
    return balance_F, appleprice_F, totalapple_F, change_F
