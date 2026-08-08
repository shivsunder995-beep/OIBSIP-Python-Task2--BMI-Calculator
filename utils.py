from datetime import datetime

def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%I:%M %p")


def current_date():
    return datetime.now().strftime("%A, %d %B %Y")


def current_time():
    return datetime.now().strftime("%I:%M:%S %p")