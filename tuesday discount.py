from datetime import datetime
datenow = datetime.weekday(datetime.today())


subtotal = float(input('What is the subtotal?'))
if datenow == 1 or datenow == 2 :
    if subtotal >= 50 :
        total_before_tax = subtotal * 0.9
        total = total_before_tax * 1.06
        discount = subtotal - total
        print(f'Your total is ${total:.2f}. You saved ${discount:.2f}')
    else:
        total = subtotal * 1.06
        print(f'Your total is ${total:.2f} Be sure to spend $50 or more one Tuesday or Wednesday to save 10% off your total!')
else:
    total = subtotal * 1.06
    print(f'Your total is ${total:.2f} Be sure to spend $50 or more one Tuesday or Wednesday to save 10% off your total!')