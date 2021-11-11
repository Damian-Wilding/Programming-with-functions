    import math
    number_of_items_made = int(input('How many manufactured items?'))
    number_of_items_per_box = int(input('How manny items will be in each box?'))
    boxes = float(number_of_items_made / number_of_items_per_box) 
    boxes_rounded = math.ceil(boxes)
    print(boxes_rounded)
