import os
rows, cols = os.popen('stty size', 'r').read().split()
rows = int(rows)-1
print(rows, cols)
cols = int(cols)
from utils import color_to_asci, px_to_int, percent_to_absolute, get_abs_num
import traceback


def build(soup, css):
    """
    given the soup and styles will get css from styles for an element and display to terminal
    @param soup {obj} - beautifulsoup object of the website
    @param styles - dict representation of the webpages full styles
    """

    #CREATE PAGE AND FILL WITH BACKGROUND COLOR
    if css['html']['background-color']:
        c = css['html']['background-color']
        bg_color = color_to_asci(c)
    elif css['body']['background-color']:
        c = css['body']['background-color']
        bg_color = color_to_asci(c)
    else:
        bg_color = W
    page = [[bg_color+'\u2588'+bg_color for i in range(cols)] for j in range(rows)]

    # print(dir(soup.findChildren()[4]))
    # print(str(soup.findChildren()[4]))
    # print(soup.findChildren()[4].name)

    line = 0
    dpr = 16
    dpc = 8
    parent_css = {'margin-top' : '8px', 'margin-bottom' : '8px', 'margin-left' : '8px', 'margin-right' : '8px', 'margin' : '16px'} #we can put all the defaults in here
    current_css = {}
    child_css = {}
    exempt_names = set(['title', 'html', 'head', 'style', 'script', 'link'])
    new_line = set(['h1', 'h2'])
    reset = '\u001b[0m'
    for item in soup.findChildren():
        # print(parent_css, current_css)
        try:

            if item.name in css:
                current_css.update(css[item.name])
                if item.attrs.get('class'):
                    for cl in item.attrs.get('class'):
                        print(css)
                        if css.get(cl):
                            current_css.update(css.get(cl))
                            print('updated css', css.get(cl))

            if item.name in exempt_names:
                continue

            # print(item['body'])
            # print('ITEM', item.name)
            # print(item.child.text)

            print(current_css)

            if item.next_element.strip() != "":
                #if there is text
                color = color_to_asci(current_css['color'])
                bg_color = color_to_asci(current_css['background-color'], bg=True)

                c_margin = 0
                r_margin = 0 
                if parent_css.get('margin'):
                    c_margin = int(get_abs_num(parent_css.get('margin'), num=cols, dpi=dpc)//dpc)
                    r_margin = int(get_abs_num(parent_css.get('margin'), num=rows, dpi=dpr)//dpr)


                # print(c_margin)
                # print(parent_css.get('margin'))
                # print(current_css.get('margin'))

                for x in range(0, len(item.next_element)):
                    page[line+r_margin][x%cols+c_margin] = bg_color+color+item.next_element[x]+reset

                    if (x+1)%cols == 0:
                        line += 1

                line += 1
                # print('ja', item.next_element)
            else:
                height = 0
                for child in item.findChildren():
                    if css.get(child.name):
                        # print(css.get(item.name).get('height'))
                        h = get_abs_num(css.get(child.name).get('height'), rows, dpi=dpr)
                        # if '%' in css.get(child.name).get('height'):
                            # h = percent_to_absolute(css.get(child.name).get('height'))

                        if h > height:
                            height = h

                    if child.next_element.strip() != "":
                        # print(child.next_element.strip())
                        height += len(child.next_element.strip())//cols+1

                print(current_css['background-color'])
                bg_color = color_to_asci(current_css['background-color'], bg=False)

                r_margin = 0
                c_margin = 0
                if parent_css.get('margin'):
                    c_margin = int(get_abs_num(parent_css.get('margin'), num=cols, dpi=dpc)//dpc)
                    r_margin = int(get_abs_num(parent_css.get('margin'), num=rows, dpi=dpr)//dpr)

                print('row', r_margin)
                for i in range(height):
                    for x in range(0, cols-c_margin*2):
                        page[line+i+r_margin][x%cols+c_margin] = bg_color+'\u2588'+reset


            if item.name in css:
                # print(css[item.name])
                parent_css.update(current_css)
            # print(type(item))
        except Exception as e:
            print(str(e)) 
            print(traceback.print_exc())
            # print(help(e.with_traceback))
    print_page(page)
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

