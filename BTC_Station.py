#make sure to download bitcoin with "pip install bitcoin"
#make sure to download blockchain with "pip install blockchain"


class btcTown():
    def btConvert(self,B_USD):
        for i in B_USD:
            x = i[1]
            print(f"1 Bitcoin is ${x}")
        EnD=input("Choose (y) or (n) to continue: ")
        if EnD == "y":
            main()
        elif EnD == "n":
            quit
        else:
            print("Invalid input. Thank you, come again!")
            quit
    def btCSpec(self,ticker,spec):
        x = spec, ticker[spec].p15min        
        X = x[0]
        X2 = x[1]
        print(f"A whole Bitcoin is worth {X2} {X}")
        EnD=input("Choose (y) or (n) to continue: ")
        if EnD == "y":
            main()
        else:
            quit
    def btCVmnt(self, ticker,spec,ducket):
        x = exchangerates.to_btc(spec, ducket)
        p = (x * 100000000)#makes sure to get best whole number
        pp = trunc(p)#strips decimals     
        P = "{:,.8f}".format(x)        
        PP = "{:,.0f}".format(p)         
        d = trunc(ducket)
        print(f"{d} {spec} in Bitcoin is: {P} btc")
        print(f"{d} {spec} in satoshi is: {PP} sats")
        EnD=input("Choose (y) or (n) to continue: ")
        if EnD == "y":
            main()
        elif EnD == "n":
            quit
    def btCVolume(self):
        stat = statistics.get()
        print("\n")
        x = stat.trade_volume_btc        
        print(f"Bitcoin Trade Volume: ${x}\n\n")
        EnD=input("Choose (y) or (n) to continue: ")
        if EnD == "y":
            main()
        else:
            quit
    def btCMined(self):
        stat = statistics.get()
        print("\n")
        x = stat.btc_mined
        print(f"Total Bitcoin Mined: {x}")
        EnD=input("Choose (y) or (n) to continue: ")
        if EnD == "y":
            main()
        else:
            quit
    def btCVolumUSD(self):
        stat = statistics.get()
        print("\n")
        x = stat.trade_volume_usd
        p = "{:,.4f}".format(x)
        print(f"Total USD worth of Bitcoin traded: ${p}")
        EnD=input("Choose (y) or (n) to continue: ")
        if EnD == "y":
            main()
        else:
            quit
class btcNation():

    def BtcWallt(self):
        # Generating a Private key.
        my_private_key = random_key()
        print("Private Key: %s\n" % my_private_key)
        # Generating a public key derived from private key
        my_public_key = privtopub(my_private_key)
        print("Public Key: %s\n" % my_public_key)
        # Create a bitcoin address
        my_bitcoin_address = pubtoaddr(my_public_key)
        print("Bitcoin Address: %s\n" % my_bitcoin_address)
        EnD=input("Choose (y) or (n) to continue: ")
        if EnD == "y":
            main()
        elif EnD == "n":
            quit

    def BtcPrice(self):        
        ticker = exchangerates.get_ticker()
        print("Bitcoin Prices in various currencies:")
        # print(f"1.) {ticker}")
        for k in ticker:
            # print(k, ticker[k].p15min)
            pass
        # Bitcoin only rate
        B_USD = []
        for btc in ticker:
            if btc == "USD":
                x = btc, ticker[btc].p15min
                B_USD.append(x)
        BtC.btConvert(B_USD)
    
    #This will print all fiat values of Bitcoin
    def BtcValue(self):        
        ticker = exchangerates.get_ticker()
        print("Bitcoin Prices in various currencies:")
        # print(f"1.) {ticker}")
        #Print All Bictoin values
        for k in ticker:
            print(k, ticker[k].p15min)
        print("\n\n")
        EnD=input("Choose (y) or (n) to continue: ")
        if EnD == "y":
            main()
        elif EnD == "n":
            quit
    
    #This will specifically call for Bitcoin and user input fiat of choice
    def BtcSpec(self):
        list=[]
        ticker = exchangerates.get_ticker()
        for i in ticker:
            list.append(i)
        print(list,"\n\n")
        spec = input("Now choose a currency: ")        
        for Spec in list:            
            if spec == Spec:
                BtC.btCSpec(ticker, spec)
    
    #This will give us the fiat amount of Bitcoin from country user inputs.
    def BtcVspec(self):
        list=[]
        ticker = exchangerates.get_ticker()
        for i in ticker:
            list.append(i)
        print(list,"\n\n")
        spec = input("Now choose a currency: ")
        ducket = float(input(f"Lastly, please enter the amount of {spec}: "))
        for Spec in list:            
            if spec == Spec:
                BtC.btCVmnt(ticker, spec, ducket)
    
    #This will lead to a list of stats for the bitcoin blockchain.
    def BtcStats(self):
        choice = '''        
        1.) Bitcoin Trade Volume
        2.) Bitcoin Trade Volume in USD
        3.) Bitcoin Mined
         
        '''
        print(choice)
        vol = int(input("Enter an addition choice for stats: "))
        if vol == 1:
            BtC.btCVolume()
        elif vol == 2:
            BtC.btCVolumUSD()
        elif vol == 3:
            BtC.btCMined()
        else:
            EnD=input("Choose (y) or (n) to continue: ")
            if EnD == "y":
                main()
            else:
                quit





from blockchain import exchangerates
from blockchain import statistics
from bitcoin import *
from math import trunc
BtC = btcTown()
def main():
    
    choice = '''
    
    ***Bitcoin Project***
    
    
    1.) Current Bitcoin value in USD
    2.) All fiat values of Bitcoin
    3.) Create Bitcoin Wallet
    4.) Choose a fiat to Bitcoin value
    5.) Enter fiat amount to view Bitcoin amount
    6.) Look at Bitcoin Stats
    
      '''
    print(choice)
    Q = int(input("Enter your choice: "))
    btC = btcNation()
    BtC = btcTown()
    if Q == 1:
        btC.BtcPrice()
    if Q == 2:
        btC.BtcValue()    
    if Q == 3:
        btC.BtcWallt()
    if Q == 4:
        btC.BtcSpec()
    if Q == 5:
        btC.BtcVspec()
    if Q == 6:
        btC.BtcStats()
    else:
        print("")

if __name__=="__main__":
    main()
    
