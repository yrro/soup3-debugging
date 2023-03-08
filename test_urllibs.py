import pytest 

import gi


test_urls = [
    "https://www.bing.com/",
    "https://www.google.com/",
    "https://www.bbc.co.uk/",
]


@pytest.fixture
def soup3():
    from gi import require_version

    gi.require_version("Soup", "3.0")



@pytest.fixture
def soup2():
    from gi import require_version

    gi.require_version("Soup", "2.4")


@pytest.mark.parametrize(
    "url", test_urls
)
def test_soup3(url, soup3):
    from gi.repository import Soup

    mes = Soup.Message.new_from_encoded_form("GET",
                                             url,
                                             "")

    ses = Soup.Session()
    ses.send_and_read(mes)


@pytest.mark.parametrize(
    "url", test_urls
)
def test_soup2(url, soup2):
    from gi.repository import Soup

    mes = Soup.Message.new("GET", url)

    ses = Soup.Session()
    ses.send_message(mes)


@pytest.mark.parametrize(
    "url", test_urls
)
def test_urllib(url):
    from urllib import request

    request.urlopen(url).read()

# vim: ts=8 sts=4 sw=4 et
