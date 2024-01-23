#!/usr/bin/python3

def safe_function(fct, *args):

	"""Executes a function safely"""

    import sys

	try:
		ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
