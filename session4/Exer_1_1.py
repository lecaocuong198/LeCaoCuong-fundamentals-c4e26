prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}   

s = 0
for i in prices:
    s += prices[i]*stock[i]
    print(i,"\nprice: ",prices[i],"\nstock: ",stock[i],"\n")

print("Estimated revenue: ",s)