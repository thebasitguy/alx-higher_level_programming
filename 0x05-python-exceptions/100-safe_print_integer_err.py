#!/usr/bin/python3

import sys

def safe_print_integer_err(value):

    """
    Prints an integer using "{:d}".format()

    Args:
        value (int): Integer to print

    Returns:
        True if value has been correctly printed
        Otherwise - False and prints in stderr
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
