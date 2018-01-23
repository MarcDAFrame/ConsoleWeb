import os
rows, cols = os.popen('stty size', 'r').read().split()
from utils import color_to_asci


def build(soup, css):
    """
    given the soup and styles will get css from styles for an element and display to terminal
    @param soup {obj} - beautifulsoup object of the website
    @param styles - dict representation of the webpages full styles
    """
    if css['html']['background-color']:
        c = css['html']['background-color']
        bg_color = color_to_asci(c)
    elif css['body']['background-color']:
        c = css['body']['background-color']
        bg_color = color_to_asci(c)
    else:
        bg_color = W

    page = [[bg_color+'\u2588'+bg_color for i in range(int(cols))] for j in range(int(rows))]
    # print(page)
    # print(soup.text)
    for item in soup.findChildren():
        # print(item['body'])
        print(item)
        print(type(item))

    # print_page(page)
    # print(page)

def print_page(page):
    for row in page:
        for item in row:
            print(item, end='')


# def fill(rows, columns, color):
#     '''
#     fills the screen full width and coluns with blocks \u2588 given a color
#     TODO:
#         - fill with a list of colors proportional to columns and rows
#     '''
#     for i in range(int(columns)):
#         for j in range(int(rows)-1):
#             print(color+'\u2588'+W, end='')

