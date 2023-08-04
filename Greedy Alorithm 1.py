# This program tells you the least amount of coins you need to pay the specified bill.
money = int(input("Input the amount of money you have to pay: "))
coins = [int(i) for i in input("Input the coins you have: ").split()]

# For finding the least amount of coins we have to sort the coins first
def sort(a):
    for x in range(len(a)-1):
        for y in range(len(a)-1):
            z = y + 1
            if a[z] > a[y]:
                t = a[z]
                a[z] = a[y]
                a[y] = t
    return a
sort(coins)

n = [0] * len(coins)
c = 0
while money > 0:
    n[c] = money // coins[c]
    money = money % coins[c]
    c += 1

for i in range(len(coins)):
    if n[i] > 0:
        print(f"You have to use {n[i]} <{coins[i]}> cents coin.")