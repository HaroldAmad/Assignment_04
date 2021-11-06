def getuserInput ():
    apple_F = int(input("Apples you want to buy: "))
    orange_F = int(input("Oranges you want to buy: "))
    totalprice_F = (apple_F*20) + (orange_F*25)
    return apple_F, orange_F, totalprice_F

def display(totalpriceFunc):
    print(f"The total amount is {totalpriceFunc}")


apple, orange, total = getuserInput()