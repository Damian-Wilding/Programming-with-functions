from datetime import datetime
import math
width = int(input('Eneter the width of the tire in mm (ex 205):'))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60):'))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15):'))
volume = (math.pi * width**(2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter))/10000000000
print(f'The approximate volume is {volume:.2f} liters')

make_file = open('volumes.txt', 'a+')
the_date = datetime.date(datetime.today())
with open('volumes.txt', 'at') as filed:


    print(f'{the_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}', file=filed)



make_file.close()