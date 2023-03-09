import io

import pytest

pycurl = pytest.importorskip("pycurl")

from conftest import urls


@pytest.fixture(scope="function")
def curl(request):
    print(f"pycurl.version: {pycurl.version}")
    curl = pycurl.Curl()
    try:
        curl.setopt(pycurl.HTTP_VERSION, request.param)
    except pycurl.error as e:
        if e.args[0] == pycurl.E_UNSUPPORTED_PROTOCOL:
            pytest.skip(reason="curl error: E_UNSUPPORTED_PROTOCOL")
        raise
    else:
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
    "url", urls,
)
def test_curl(url, curl):
    buffer = io.BytesIO()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.perform()
    curl.close()
