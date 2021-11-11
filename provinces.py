import csv


def main():
    list = read_list('provinces.txt')
    
   

def read_list(filename):
    list_temp = []
    count = 0
    with open(filename, 'rt') as province_list:
        for lines in province_list:
            clean_line = lines.strip()
            list_temp.append(clean_line)
        list_temp.pop(0)
        list_temp.pop(-1)
        for line in list_temp:
            if line == 'AB':
                line = 'Alberta'
                count += 1
                print(line)
            elif line =='Alberta':
                count +=1
                print(line)
            else: 
                print(line)
            
        print(f'Alberta showed up {count} times.')
        


main()