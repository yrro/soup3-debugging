from urllib import request

import pytest

from conftest import urls


@pytest.mark.parametrize(
    "url", urls
)
def test_urllib(url):
    request.urlopen(url).read()
