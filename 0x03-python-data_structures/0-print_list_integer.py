#!/usr/bin/python3
if __name__ != "__main__":
    exit


def print_list_integer(my_list=[]):
    """Function that prints all integers of a list.

    Args:
        my_list: list of integers

    Returns:
        None
    """
    for n in my_list:
        print("{:d}".format(n))
