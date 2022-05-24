from math import trunc

t = input("(y) or (n) to play: ")
count = 0
while t == "y":
  count+=1
  if count >= 2 :
    t = input("(y) or (n) to continue: ")
    if t == "n":
      break
      
  btc = float(input("Enter the dollar amount you want to put into bitcoin: $"))
  btc1 = float(input("Enter the dollar amount Bitcoin is worth: "))


  Btc1 = btc/btc1

  p = (Btc1)
  pp = (p * 100000000)#makes sure to get best whole number
  ppp = trunc(pp)#strips decimals
  Pppp = "{:,.8f}".format(p)#convert for Bitcoin 8 decimals.
  pppp = "{:,.0f}".format(ppp)#converts with comma 0 decimals.
  print(f" ***${btc} is {Pppp}BTC, which converts to {pppp}sats.***")
  print("\n\n")
else:
  input("End the program.")

