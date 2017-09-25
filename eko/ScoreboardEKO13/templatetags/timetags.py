from django import template
from time import gmtime, strftime

register = template.Library()


def print_timestamp(timestamp):
    try:
        # assume, that timestamp is given in seconds with decimal point
        ts = float(timestamp)
    except ValueError:
        return None

    return strftime('%H:%M:%S', gmtime(ts))


register.filter(print_timestamp)
