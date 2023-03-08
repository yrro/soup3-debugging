import pytest 

import gi


test_urls = [
    "https://www.bing.com/",
    "https://www.google.com/",
    "https://www.bbc.co.uk/",
]


@pytest.fixture
def Soup3(monkeypatch):
    monkeypatch.setenv("G_MESSAGES_DEBUG", "all")

    from gi import require_version

    gi.require_version("Soup", "3.0")

    from gi.repository import Soup
    return Soup


@pytest.fixture
def Soup2(monkeypatch):
    monkeypatch.setenv("G_MESSAGES_DEBUG", "all")

    from gi import require_version

    gi.require_version("Soup", "2.4")

    from gi.repository import Soup
    return Soup


@pytest.mark.parametrize(
    "url", test_urls
)
def test_soup3(url, Soup3):
    mes = Soup3.Message.new_from_encoded_form("GET", url, "")

    ses = Soup3.Session()
    ses.send_and_read(mes)


@pytest.mark.parametrize(
    "url", test_urls
)
def test_soup2(url, Soup2):
    mes = Soup2.Message.new("GET", url)

    ses = Soup2.Session()
    ses.send_message(mes)


@pytest.mark.parametrize(
    "url", test_urls
)
def test_urllib(url):
    from urllib import request

    request.urlopen(url).read()

# vim: ts=8 sts=4 sw=4 et
