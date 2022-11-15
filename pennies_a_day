#python 3.10
#80k or 1 penny a day


import math
from time import sleep as S


print("You have 2 choices. $80,000 or ill pay you 1 penny a day. You cannot touch your pay until the last day, but Ill double the balance on a daily basis for up to only a max of 30 days worth of your labor.")


ch = int(input("What's it gunna be? Choice(1) or Choice(2): "))

if ch == 1:
  print("Congrats. You just made the easiest $80,000 you may ever make in your life.")

elif ch == 2:
  print(" ")
  d = int(input("Enter the amount of days you plan to work: "))
  count = 0
  count1 = .00
  #print("Day 0:\033[32m $0.01\033[0m")
  S(1)
  for i in range(d):
    count += 1
  
    count1 = count1 + count1    
    if count <=30:
        count1 += .01
        count2 = "${:,.2f}" .format(count1)
        print(f"Day {count}: \033[32m{count2}\033[0m")

            
    elif count >30:
        count1 += .01
        count2 = "${:,.2f}" .format(count1)
        print(f"Day {count}: \033[31m{count2}\033[0m")
    S(1)
        
        
elif ch != 1 or 2:
  print("Wow you had one simple task. Choose 1 or 2.")
else:
  print("Thank you. Come again.")
