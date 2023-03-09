import io

import pytest

pycurl = pytest.importorskip("pycurl")

from conftest import urls


def build_curl(tls_version, http_version):
    print(f"pycurl.version: {pycurl.version}")
    curl = pycurl.Curl()
    curl.setopt(pycurl.SSLVERSION, tls_version)
    try:
        curl.setopt(pycurl.HTTP_VERSION, http_version)
    except pycurl.error as e:
        if e.args[0] == pycurl.E_UNSUPPORTED_PROTOCOL:
            pytest.skip(reason="curl error: E_UNSUPPORTED_PROTOCOL")
    else:
        return curl

@pytest.mark.parametrize(
    "tls_version", [
        pycurl.SSLVERSION_TLSv1_3,
        pycurl.SSLVERSION_TLSv1_2,
    ], ids=[
        "TLSv1.3",
        "TLSv1.2",
    ],
)
@pytest.mark.parametrize(
    "http_version", [
        pycurl.CURL_HTTP_VERSION_1_1,
        pycurl.CURL_HTTP_VERSION_2,
        pycurl.CURL_HTTP_VERSION_3,
    ], ids=[
        "HTTP/1.1",
        "HTTP/2",
        "HTTP/3",
    ],
)
@pytest.mark.parametrize(
    "url", urls,
)
def test_curl(tls_version, http_version, url):
    curl = build_curl(tls_version, http_version)
    buffer = io.BytesIO()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.perform()
    curl.close()
