no_of_coins = 0

def store(coins):
    global no_of_coins
    no_of_coins = no_of_coins + coins


inppput = input("Enter the cash you want withdrawn: ")
int_cash = int(inppput)

def update(xy):
    global int_cash   
    store(int_cash//xy)
    int_cash = int_cash%xy

update(500)
update(100)
update(25)
update(10)
update(5)
update(1)



print(no_of_coins)