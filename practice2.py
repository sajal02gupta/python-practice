def wallet(balance):
    print('Total balance is: ',balance)
    def amount():
        print("total balance is:",balance)
    def deposit(amount):
        nonlocal balance
        balance=balance+amount
        print("deposited amount",balance)

    def spend(spendamount):
        nonlocal balance
        balance-=spendamount
        print("Remaining balance is ",balance)
    def transfer(fund, wallet):
        nonlocal balance
        balance-= fund
        wallet["Deposit info"](fund)
        print("the transferred fund is:",fund)
        print('Remaining amount is: ',balance)

    #li=[deposit, spend]
    li={
        "Deposit info": deposit,
        "Spending info": spend,
        "transfer": transfer,
        "amount":amount
    }
    return li


w1= wallet(400)
w2=wallet(200)
print(type(w1))
w1["Deposit info"](300)
w1["Spending info"](200)
w1["transfer"](400, w2)
w1["Deposit info"](400)
w2["amount"]()
w1["amount"]()