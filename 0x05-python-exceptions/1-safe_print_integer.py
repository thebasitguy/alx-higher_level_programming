#!/usr/bin/python3

def safe_print_integer(value):

    """
    Function that prints an integer with "{:d}".format()

    Args:
        value (int): The integer to print

    Returns:
        True if value has been correctly printed
        Otherwise - False
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
