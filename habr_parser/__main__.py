import httpx
from lxml import html
from lxml.html import HtmlElement

URL = 'https://habr.com/ru/articles/top/daily/'
TITLE_CLASS = 'tm-title__link'
COUNTER_CLASS = 'tm-icon-counter__value'

response = httpx.get(URL)

tree: HtmlElement = html.fromstring(response.text)
titles: list[HtmlElement] = tree.find_class(TITLE_CLASS)
counts: list[HtmlElement] = tree.find_class(COUNTER_CLASS)

for i, (t, c) in enumerate(zip(titles, counts), 1):
    title = t.find('span')
    print(f"{i}. {title.text} | {c.text}")
