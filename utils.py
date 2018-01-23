def color_to_asci(color):
    #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

    colors = {'BLACK' : '\033[30m', 'RED' : '\033[31m', 'GREEN' : '\033[32m', 'YELLOW' : '\033[33m', 'BLUE' : '\033[34m', 'MAGENTA' : '\033[35m', 'CYAN' : '\033[36m', 'WHITE' : '\033[37m' }
    return colors[color.upper()]