from output import build
from get import get_html, parse_page


def init(url):
    page = get_html(url)
    soup, css = parse_page(page, url)
    build(soup, css)


init('http://127.0.0.1:5000/')