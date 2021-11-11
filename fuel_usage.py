def miles_per_gallon(start, end, gallons):
    mpg = (end - start) / gallons
    return(mpg)

def liters_per_100_kilometers(mpg):
    lp100k = 235.215 / mpg
    return(lp100k)

def main():
    starting_number = float(input('Please enter the starting value on the odometer:'))
    ending_number = float(input('Please enter the ending value on the odometer:'))
    gas_used = float(input('Please enter the amount of gallons of gas used:'))
    mpg = miles_per_gallon(starting_number, ending_number, gas_used)
    lp100k = liters_per_100_kilometers(mpg)
    print(f'{mpg:.2f} miles per gallon.')
    print(f'{lp100k:.2f} liters per 100 kilometers.')
main()