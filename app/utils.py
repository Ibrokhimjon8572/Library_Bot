from datetime import datetime


def unixToDate(unix=None):
    ts = int(unix)
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
