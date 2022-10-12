#!/usr/bin/python3

def safe_print_integer(value):
    '''print an integer with "{:d}".format().
    Args:
    value (int): The integer to print.
    Return:
    If a TypeError or ValueError occurs - false. otherwise - True.
    '''
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
