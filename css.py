import urllib.request
import cssutils
#'http://127.0.0.1:5000/static/test.css'
def css_dict(css_raw): 
    #.decode('utf-8')
    # print(cssutils.parseString(css_raw))
    """
    
    """
    dct = {}
    for rule in cssutils.parseString(css_raw):
        selector = rule.selectorText.strip('.').strip('#')
        styles = rule.style.cssText
        dct[selector] = styles

    return dct

def create_css(styles):
    css = {}

    for key, value in styles.items():
        css[key] = {}
        for items in value.split(';'):
            css[key][items.split(':')[0].strip('\n').strip()] = items.split(':')[1].strip('\n').strip()

    return css

def get_css(url):
    return urllib.request.urlopen(url).read()