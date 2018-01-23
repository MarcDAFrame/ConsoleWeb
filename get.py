import urllib.request
import bs4

from css import get_css, css_dict, create_css


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

    css = create_css(styles)

    return soup, css


def get_html(url):
    '''
    returns page
    '''
    page = urllib.request.urlopen(url).read()
    # print(bs4.BeautifulSoup(page, "lxml"))
    return page