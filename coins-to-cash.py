def calc_dollars(**coins):
    dollarAmount = 0
    dollarAmount += (coins["pennies"] * .01) + (coins["nickels"] * .05) + \
        (coins["dimes"] * .10) + (coins["quarters"] * .25)
    print(f"${dollarAmount}")
calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)