# libsoup 3 connection reset test cases

Sample output; note that `test_soup2` and `test_urllib` pass; only `test_soup3`
fails.

```
$ pytest --forked -v
============================================================================================= test session starts ==============================================================================================
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/phe.gov.uk/sam.morris/src/soup3-debugging
plugins: xdist-3.1.0, forked-1.4.0
collected 9 items                                                                                                                                                                                              

test_urllibs.py::test_soup3[https://www.bing.com/] FAILED                                                                                                                                                [ 11%]
test_urllibs.py::test_soup3[https://www.google.com/] FAILED                                                                                                                                              [ 22%]
test_urllibs.py::test_soup3[https://www.bbc.co.uk/] FAILED                                                                                                                                               [ 33%]
test_urllibs.py::test_soup2[https://www.bing.com/] PASSED                                                                                                                                                [ 44%]
test_urllibs.py::test_soup2[https://www.google.com/] PASSED                                                                                                                                              [ 55%]
test_urllibs.py::test_soup2[https://www.bbc.co.uk/] PASSED                                                                                                                                               [ 66%]
test_urllibs.py::test_urllib[https://www.bing.com/] PASSED                                                                                                                                               [ 77%]
test_urllibs.py::test_urllib[https://www.google.com/] PASSED                                                                                                                                             [ 88%]
test_urllibs.py::test_urllib[https://www.bbc.co.uk/] PASSED                                                                                                                                              [100%]

=================================================================================================== FAILURES ===================================================================================================
______________________________________________________________________________________ test_soup3[https://www.bing.com/] _______________________________________________________________________________________
url = 'https://www.bing.com/', soup3 = None

    @pytest.mark.parametrize(
        "url", test_urls
    )
    def test_soup3(url, soup3):
        from gi.repository import Soup
    
        mes = Soup.Message.new_from_encoded_form("GET",
                                                 url,
                                                 "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: g-io-error-quark: Error receiving data: Connection reset by peer (44)

test_urllibs.py:39: Error
_____________________________________________________________________________________ test_soup3[https://www.google.com/] ______________________________________________________________________________________
url = 'https://www.google.com/', soup3 = None

    @pytest.mark.parametrize(
        "url", test_urls
    )
    def test_soup3(url, soup3):
        from gi.repository import Soup
    
        mes = Soup.Message.new_from_encoded_form("GET",
                                                 url,
                                                 "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: g-tls-error-quark: Error reading data from TLS socket: The specified session has been invalidated for some reason. (1)

test_urllibs.py:39: Error
______________________________________________________________________________________ test_soup3[https://www.bbc.co.uk/] ______________________________________________________________________________________
url = 'https://www.bbc.co.uk/', soup3 = None

    @pytest.mark.parametrize(
        "url", test_urls
    )
    def test_soup3(url, soup3):
        from gi.repository import Soup
    
        mes = Soup.Message.new_from_encoded_form("GET",
                                                 url,
                                                 "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: soup-session-error-quark: Could not parse HTTP response (0)

test_urllibs.py:39: Error
=========================================================================================== short test summary info ============================================================================================
FAILED test_urllibs.py::test_soup3[https://www.bing.com/]
FAILED test_urllibs.py::test_soup3[https://www.google.com/]
FAILED test_urllibs.py::test_soup3[https://www.bbc.co.uk/]
========================================================================================= 3 failed, 6 passed in 2.04s ==========================================================================================
```
