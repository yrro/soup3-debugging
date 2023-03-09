import io

import pycurl
import pytest


test_urls = [
    "https://www.bing.com/",
    "https://www.google.com/",
    "https://www.bbc.co.uk/",
]


@pytest.fixture
def Soup(monkeypatch, request):
    monkeypatch.setenv("G_MESSAGES_DEBUG", "all")

    from gi import require_version

    try:
        require_version("Soup", request.param)
    except ValueError as e:
        pytest.skip(str(e))

    from gi.repository import Soup
    return Soup


@pytest.mark.parametrize("Soup", ["3.0"], indirect=True)
@pytest.mark.parametrize(
    "url", test_urls
)
def test_soup3(url, Soup):
    mes = Soup.Message.new_from_encoded_form("GET", url, "")

    ses = Soup.Session()
    ses.send_and_read(mes)


@pytest.mark.parametrize("Soup", ["2.4"], indirect=True)
@pytest.mark.parametrize(
    "url", test_urls
)
def test_soup2(url, Soup):
    mes = Soup.Message.new("GET", url)

    ses = Soup.Session()
    ses.send_message(mes)


@pytest.fixture(scope="function")
def curl(request):
    print(f"pycurl.version: {pycurl.version}")
    curl = pycurl.Curl()
    curl.setopt(pycurl.HTTP_VERSION, request.param)
    return curl

@pytest.mark.parametrize(
    "curl", [
        pycurl.CURL_HTTP_VERSION_1_1,
        pycurl.CURL_HTTP_VERSION_2,
        pycurl.CURL_HTTP_VERSION_3,
    ], ids=[
        "HTTP/1.1",
        "HTTP/2",
        "HTTP/3",
    ],
    indirect=True,
)
@pytest.mark.parametrize(
    "url", test_urls,
)
def test_curl(url, curl):
    buffer = io.BytesIO()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.perform()
    curl.close()


@pytest.mark.parametrize(
    "url", test_urls
)
def test_urllib(url):
    from urllib import request

    request.urlopen(url).read()

# vim: ts=8 sts=4 sw=4 et
