def color_to_asci(color, bg=False):
    #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
    if not color:
        if bg:
            return '\033[47m'
        else:
            return '\033[37m'

    if bg:#if we want bg colors returned
        colors = {'BLACK' : '\033[40m', 'RED' : '\033[41m', 'GREEN' : '\033[42m', 'YELLOW' : '\033[43m', 'BLUE' : '\033[44m', 'MAGENTA' : '\033[45m', 'CYAN' : '\033[46m', 'WHITE' : '\033[47m' }
    else:
        colors = {'BLACK' : '\033[30m', 'RED' : '\033[31m', 'GREEN' : '\033[32m', 'YELLOW' : '\033[33m', 'BLUE' : '\033[34m', 'MAGENTA' : '\033[35m', 'CYAN' : '\033[36m', 'WHITE' : '\033[37m' }
    return colors[color.upper()]

def percent_to_absolute(percent, num, dpi):
    """
    percent : string representation of a percent
    num : int representation of number of rows or columns
    dpi : the number of pixels per row or column value
    returns an absolute number based off percent
    """
    return int((float(percent.strip('%'))/100 * num) / dpi)

def px_to_int(px):
    return int(px.strip('px'))

def get_abs_num(val, num=None, dpi=None):
    if not val:
        return 0
    if 'px' in val:
        return px_to_int(val)
    if '%' in val:
        return percent_to_absolute(val, num, dpi)