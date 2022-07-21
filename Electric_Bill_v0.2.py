#DC systems: electricity moves through the wire. River where all water flows.
#AC systems: no positive or negative. No flow. Transmit through vibration. Waves over ocean as the ocean goes nowhere.


   #Garden hose analogy
#Voltage would be pressure of water. The force of the electrical charge. potential is always there when hose is on.
#Amps would be the thickness of the hose. Bigger hose more water. Bigger amount of electricity the larger the amps need to be.
#Voltage x Amps = Watts


#12v means you can only hook up 12v appliance. 110Vac appliance and 110Vac plug...then they are compatible.

voltlist = []
amplist = []
wattlist = []
count = 0
rate = float(input("What is the rate of your electric charges per kWh? "))
appliances= int(input("So what is the number of appliances we are looking at today? "))
for i in range(appliances):
    count+=1
    name = input(f"What is the name of appliance? ")
    volt = float(input(f"What is the voltage of the {name}? "))
    amps= float(input(f"What are the amps of the {name}? "))
    voltlist.append(f"{name} is {volt}V")
    amplist.append(f"{name} {amps}A." )
#The Math for the Wattage
    watts = volt * amps
    wattlist.append(f"{name} takes up {watts}watts.")
    mincal = float(1/60)
    watthrs1= watts * mincal #1min
    watthrs2 = watts * 1  #1hr
    watthrs3 = watts * 24  #1day
    watthrs4 = watts * 168 #1week
    watthrs5 = watts * 672  #1month
    watthrs6 = watts * 8064 #1year

    kWh1 = watthrs1/1000    #1min in kWh
    kWh2 = watthrs2/1000    #1hr in kWh
    kWh3 = watthrs3 / 1000  # 1day in kWh
    kWh4 = watthrs4 / 1000  # 1week in kWh
    kWh5 = watthrs5 / 1000  # 1month in kWh
    kWh6 = watthrs6 / 1000  # 1year in kWh

    ckWh1 = kWh1*rate
    ckWh12 = kWh2*rate
    ckWh13 = kWh3*rate
    ckWh14 = kWh4 * rate
    ckWh15 = kWh5 * rate
    ckWh16 = kWh6 * rate

    c1 = "${:,.2f}".format(ckWh1)
    c2 = "${:,.2f}".format(ckWh12)
    c3 = "${:,.2f}".format(ckWh13)
    c4 = "${:,.2f}".format(ckWh14)
    c5 = "${:,.2f}".format(ckWh15)
    c6 = "${:,.2f}".format(ckWh16)
    print(" ")

    count = -1
    for app in str(appliances):
        count += 1
        print(voltlist[int(count)])
        print(amplist[int(count)])
        print(wattlist[int(count)])

        print(f"    1 Minute = {watthrs1}watts.  {kWh1}kWh per minute. Costing {c1} for all peaks.")
        print(f"    1 HOUR = {watthrs2}watts.    {kWh2}kWh per hour. Costing {c2} for all peaks.")
        print(f"    1 DAY = {watthrs3}watts.     {kWh3}kWh per day. Costing {c3} for all peaks.")
        print(f"    1 WEEK = {watthrs4}watts.    {kWh4}kWh per week. Costing {c4} for all peaks.")
        print(f"    1 Month = {watthrs5}watts.   {kWh5}kWh per month. Costing {c5} for all peaks.")
        print(f"    1 year = {watthrs6}watts.    {kWh6}kWh per year. Costing {c6} for all peaks.")
        print(" ")
