import urllib.request
import bs4

import os
from css import get_css, css_dict
rows, columns = os.popen('stty size', 'r').read().split()
from colors import * 


def fill(rows, columns, color):
    '''
    fills the screen full width and coluns with blocks \u2588 given a color
    TODO:
        - fill with a list of colors proportional to columns and rows
    '''
    for i in range(int(columns)):
        for j in range(int(rows)-1):
            print(color+'\u2588'+W, end='')

def get_element_css(element, styles)
    '''
    given the element name will return a dictionary containing the styles of element
    @param - element {str} - string representing element
    @param - styles {dict} - dictionary containing raw 
    TODO: 
        - FIND CSS FROM THE ID AS WELL
    '''
    css = {}
    css_raw = []
    css_raw.append(styles[element])
    for class_ in soup.body['class']:
        # print(class_)
        css_raw.append(styles['.'+class_])
    for i in css_raw:
        for j in i.split(';'):
            temp = j.split(':')
            css[temp[0].strip().strip('\n')] = temp[1].strip().strip('\n')
    return css

def display(soup, styles):
    '''
    given the soup and styles will get css from styles for an element and display to terminal
    @param soup {obj} - beautifulsoup object of the website
    @param styles - dict representation of the webpages full styles
    TODO:
        - better colors system that can work with RGB and hex
    '''
    colors = {'purple' : P, 'blue' : B, 'red' : R, 'green' : G}
    
    body_css = get_element_css('body', styles)
    
    # print(css)
    fill(rows, columns, colors[body_css['background-color']])


def parse_page(page, url):
    '''
    given page and url will create soup and styles
    @param page {bytes} 
    @param url {str} - string representation of 
    '''
    soup = bs4.BeautifulSoup(page, "html.parser")
    # print(soup.find('body')['class'])
    # print()
    styles = {}
    styles.update(css_dict(soup.style.text))
    for i in soup.find_all('link', rel="stylesheet"):
        print(i['href'])
        if i['href'][0:3] != 'http':
            css_raw = get_css(url+i['href'])
        else:
            css_raw = get_css(i['href'])
        styles.update(css_dict(css_raw))
    print(styles)
    return soup, styles


def get_html(url):
    '''
    returns page
    '''
    page = urllib.request.urlopen(url).read()
    # print(bs4.BeautifulSoup(page, "lxml"))
    return page


def init(url):
    page = get_html(url)
    soup, styles = parse_page(page, url)
    display(soup, styles)


init('http://127.0.0.1:5000/')
