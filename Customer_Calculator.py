from YearlyEnergyConsumption import real_enery_consumption

Number_stuffs = input("How many different stuffs you need to check their consumptions? :")
for i in range (Number_stuffs):
    Watts = input("Please type the energy used in Watt by the stuff: ")
    Number = input("How many of this stuff you have?: ")
    Hrs = input("How many hours your stuff is used in a year?: ")
    Kilowatt_cost = input("How many cents you pay for each kilowatt/hours to your electricity company?: ")
    print "For %i of stuff %i with energy consumption %i Watts for each, your annual cost is %0.2f Euros!" %(Number, i+1, Watts, real_enery_consumption(Watts, Number, Hrs, Kilowatt_cost))
