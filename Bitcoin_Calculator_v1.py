# How much does it take?

original = float(input("Whats the current or original price of Bitcoin for when you plan to invest?: "))
investment = float(input("What is the original dollar amount of money you wish to put into bitcoin?: "))
percentdiff = (investment / original)
new_price1 = float(input("At what dollar price would you like to see bitcoin in order to take profit?: "))



percent_diff_raw = ((new_price1 - original) / original)
percent_diff = (round(percent_diff_raw, 4))
percent_diff_done = (percent_diff * 100)



invest_profit_diff = ((percent_diff_done * investment) / 100)
percent_plus_invest = (invest_profit_diff + investment)
BTC = investment / original


print(" ")
print(" ")
print("Your balance in BTC is: " + str(round(BTC, 8)) + "BTC")  #This string limits float to 8 decimals.
print("Your difference will be " + str(round(percent_diff_done, 6)) + "%")
print(f"Your profit will be ${invest_profit_diff}")  #round to the second decimal
print("Your new balance will be $" + str(percent_plus_invest))
print(" ")

print("Always remember to have a plan for when to take profit."
      "A great place to start is taking out your initial investment"
      "if you make over 100%. Never hurts to take profit.")
print("Also risk only what you are willing to lose. At least if you take profit, the rest is on the house.")
