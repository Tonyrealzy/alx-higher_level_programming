#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        count += 1

    try:
        while x <= count:
            if x == 0:
                return my_list[0]
            else if x > 0:
                return my_list[0:(x - 1)]
    except:
        x > count
        return count


