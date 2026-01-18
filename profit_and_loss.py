print("profit loss")
buy=float(input("enter your buying price"))
sell=float(input("enter the selling price"))
if (buy<sell):
    amount=buy-sell
    print("you're in profit, total profit =",amount)
else:
    amount=sell-buy
    print("you're in loss, total loss =",amount)
