import pytest

from conftest import urls


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
    "url", urls
)
def test_soup3(url, Soup):
    mes = Soup.Message.new_from_encoded_form("GET", url, "")

    ses = Soup.Session()
    ses.send_and_read(mes)


@pytest.mark.parametrize("Soup", ["2.4"], indirect=True)
@pytest.mark.parametrize(
    "url", urls
)
def test_soup2(url, Soup):
    mes = Soup.Message.new("GET", url)

    ses = Soup.Session()
    ses.send_message(mes)


