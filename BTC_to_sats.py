import math
BTC = float(input("Enter the amount of Bitcoin: "))
print(f"From {BTC} BTC")

p = BTC
pp = int(p * 100000000)
ppp = math.trunc(pp)
pppp = "{:,.0f}".format(ppp)
print(f"To {pppp} sats")
