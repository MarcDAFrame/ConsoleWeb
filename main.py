from output import build
from get import get_html, parse_page


def start(url):
    page = get_html(url)
    soup, css = parse_page(page, url)
    build(soup, css)


if __name__ == "__main__":
    start('http://127.0.0.1:5000/')

