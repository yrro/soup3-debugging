# libsoup 3 connection reset test cases

Sample output; note that `test_soup2` and `test_urllib` pass; only `test_soup3`
fails.

To run the tests, you will need the Python packages `python-pytest` and
`python-pytest` available to your system Python environment.

Here's the output of running the tests on my machine. A [nicer HTML-formatted
report](https://raw.githack.com/yrro/soup3-debugging/master/report.html) is also
available.

```
============================================================================================================ test session starts =============================================================================================================
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
metadata: {'Python': '3.11.2', 'Platform': 'Linux-6.1.0-3-amd64-x86_64-with-glibc2.36', 'Packages': {'pytest': '7.2.1', 'pluggy': '0.13.0'}, 'Plugins': {'metadata': '2.0.4', 'html': '3.2.0', 'xdist': '3.1.0', 'forked': '1.4.0'}}
rootdir: /home/example.com/yrro/src/soup3-debugging
plugins: metadata-2.0.4, html-3.2.0, xdist-3.1.0, forked-1.4.0
collected 18 items                                                                                                                                                                                                                           

test_curl.py::test_curl[https://www.bing.com/-HTTP/1.1] PASSED                                                                                                                                                                         [  5%]
test_curl.py::test_curl[https://www.bing.com/-HTTP/2] PASSED                                                                                                                                                                           [ 11%]
test_curl.py::test_curl[https://www.bing.com/-HTTP/3] SKIPPED (curl error: E_UNSUPPORTED_PROTOCOL)                                                                                                                                     [ 16%]
test_curl.py::test_curl[https://www.google.com/-HTTP/1.1] PASSED                                                                                                                                                                       [ 22%]
test_curl.py::test_curl[https://www.google.com/-HTTP/2] PASSED                                                                                                                                                                         [ 27%]
test_curl.py::test_curl[https://www.google.com/-HTTP/3] SKIPPED (curl error: E_UNSUPPORTED_PROTOCOL)                                                                                                                                   [ 33%]
test_curl.py::test_curl[https://www.bbc.co.uk/-HTTP/1.1] PASSED                                                                                                                                                                        [ 38%]
test_curl.py::test_curl[https://www.bbc.co.uk/-HTTP/2] PASSED                                                                                                                                                                          [ 44%]
test_curl.py::test_curl[https://www.bbc.co.uk/-HTTP/3] SKIPPED (curl error: E_UNSUPPORTED_PROTOCOL)                                                                                                                                    [ 50%]
test_soup.py::test_soup3[https://www.bing.com/-3.0] FAILED                                                                                                                                                                             [ 55%]
test_soup.py::test_soup3[https://www.google.com/-3.0] FAILED                                                                                                                                                                           [ 61%]
test_soup.py::test_soup3[https://www.bbc.co.uk/-3.0] FAILED                                                                                                                                                                            [ 66%]
test_soup.py::test_soup2[https://www.bing.com/-2.4] PASSED                                                                                                                                                                             [ 72%]
test_soup.py::test_soup2[https://www.google.com/-2.4] PASSED                                                                                                                                                                           [ 77%]
test_soup.py::test_soup2[https://www.bbc.co.uk/-2.4] PASSED                                                                                                                                                                            [ 83%]
test_urllib.py::test_urllib[https://www.bing.com/] PASSED                                                                                                                                                                              [ 88%]
test_urllib.py::test_urllib[https://www.google.com/] PASSED                                                                                                                                                                            [ 94%]
test_urllib.py::test_urllib[https://www.bbc.co.uk/] PASSED                                                                                                                                                                             [100%]

================================================================================================================== FAILURES ==================================================================================================================
___________________________________________________________________________________________________ test_soup3[https://www.bing.com/-3.0] ____________________________________________________________________________________________________
url = 'https://www.bing.com/', Soup = <IntrospectionModule 'Soup' from '/usr/lib/x86_64-linux-gnu/girepository-1.0/Soup-3.0.typelib'>

    @pytest.mark.parametrize("Soup", ["3.0"], indirect=True)
    @pytest.mark.parametrize(
        "url", urls
    )
    def test_soup3(url, Soup):
        mes = Soup.Message.new_from_encoded_form("GET", url, "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: g-io-error-quark: Error receiving data: Connection reset by peer (44)

test_soup.py:29: Error
------------------------------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------------------------------
(process:1414222): GLib-GIO-DEBUG: 14:23:17.395: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
(process:1414222): dconf-DEBUG: 14:23:17.395: watch_fast: "/system/proxy/" (establishing: 0, active: 0)
(process:1414222): dconf-DEBUG: 14:23:17.395: watch_fast: "/system/proxy/http/" (establishing: 0, active: 0)
(process:1414222): dconf-DEBUG: 14:23:17.395: watch_fast: "/system/proxy/https/" (establishing: 0, active: 0)
(process:1414222): dconf-DEBUG: 14:23:17.396: watch_fast: "/system/proxy/ftp/" (establishing: 0, active: 0)
(process:1414222): dconf-DEBUG: 14:23:17.396: watch_fast: "/system/proxy/socks/" (establishing: 0, active: 0)
(process:1414222): GLib-GIO-DEBUG: 14:23:17.396: _g_io_module_get_default: Found default implementation gnome (GProxyResolverGnome) for ‘gio-proxy-resolver’
(process:1414222): GLib-GIO-DEBUG: 14:23:17.396: Using cross-namespace EXTERNAL authentication (this will deadlock if server is GDBus < 2.73.3)
(process:1414222): dconf-DEBUG: 14:23:17.398: watch_established: "/system/proxy/" (establishing: 1)
(process:1414222): dconf-DEBUG: 14:23:17.398: watch_established: "/system/proxy/http/" (establishing: 1)
(process:1414222): dconf-DEBUG: 14:23:17.398: watch_established: "/system/proxy/https/" (establishing: 1)
(process:1414222): dconf-DEBUG: 14:23:17.398: watch_established: "/system/proxy/ftp/" (establishing: 1)
(process:1414222): dconf-DEBUG: 14:23:17.398: watch_established: "/system/proxy/socks/" (establishing: 1)
(process:1414222): GLib-GIO-DEBUG: 14:23:17.416: _g_io_module_get_default: Found default implementation gnutls (GTlsBackendGnutls) for ‘gio-tls-backend’
(process:1414222): GLib-Net-DEBUG: 14:23:17.416: CLIENT[0x26141e0]: Starting synchronous TLS handshake
(process:1414222): GLib-Net-DEBUG: 14:23:17.416: CLIENT[0x26141e0]: TLS handshake thread starts
(process:1414222): GLib-Net-DEBUG: 14:23:17.416: CLIENT[0x26141e0]: claiming operation OP_HANDSHAKE
(process:1414222): GLib-Net-DEBUG: 14:23:17.417: CLIENT[0x26141e0]: claiming operation OP_HANDSHAKE succeeded
(process:1414222): GLib-Net-DEBUG: 14:23:17.442: CLIENT[0x26141e0]: verifying peer certificate
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: TLS handshake thread succeeded
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: synchronous TLS handshake thread completed
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: finishing TLS handshake
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: TLS handshake has finished successfully
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: yielding operation OP_HANDSHAKE
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: starting to write 99 bytes to TLS connection
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: claiming operation OP_WRITE
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: claiming operation OP_WRITE succeeded
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: yielding operation OP_WRITE
(process:1414222): GLib-Net-DEBUG: 14:23:17.484: CLIENT[0x26141e0]: successfully write 99 bytes to TLS connection
(process:1414222): GLib-Net-DEBUG: 14:23:17.485: CLIENT[0x26141e0]: starting to read data from TLS connection
(process:1414222): GLib-Net-DEBUG: 14:23:17.485: CLIENT[0x26141e0]: claiming operation OP_READ
(process:1414222): GLib-Net-DEBUG: 14:23:17.485: CLIENT[0x26141e0]: claiming operation OP_READ succeeded
(process:1414222): GLib-Net-DEBUG: 14:23:17.485: CLIENT[0x26141e0]: yielding operation OP_READ
(process:1414222): GLib-Net-DEBUG: 14:23:17.485: CLIENT[0x26141e0]: successfully read 40 bytes from TLS connection
(process:1414222): GLib-Net-DEBUG: 14:23:17.485: CLIENT[0x26141e0]: starting to read data from TLS connection
(process:1414222): GLib-Net-DEBUG: 14:23:17.485: CLIENT[0x26141e0]: claiming operation OP_READ
(process:1414222): GLib-Net-DEBUG: 14:23:17.485: CLIENT[0x26141e0]: claiming operation OP_READ succeeded
(process:1414222): GLib-Net-DEBUG: 14:23:17.502: CLIENT[0x26141e0]: yielding operation OP_READ
(process:1414222): GLib-Net-DEBUG: 14:23:17.502: CLIENT[0x26141e0]: reading data from TLS connection has failed: ERROR
(process:1414222): GLib-Net-DEBUG: 14:23:17.502: CLIENT[0x26141e0]: starting to close the TLS connection
(process:1414222): GLib-Net-DEBUG: 14:23:17.502: CLIENT[0x26141e0]: claiming operation OP_CLOSE_BOTH
(process:1414222): GLib-Net-DEBUG: 14:23:17.502: CLIENT[0x26141e0]: claiming operation OP_CLOSE_BOTH succeeded
(process:1414222): GLib-Net-DEBUG: 14:23:17.502: CLIENT[0x26141e0]: yielding operation OP_CLOSE_BOTH
(process:1414222): GLib-Net-DEBUG: 14:23:17.502: CLIENT[0x26141e0]: error closing TLS connection: Error sending data: Broken pipe
__________________________________________________________________________________________________ test_soup3[https://www.google.com/-3.0] ___________________________________________________________________________________________________
url = 'https://www.google.com/', Soup = <IntrospectionModule 'Soup' from '/usr/lib/x86_64-linux-gnu/girepository-1.0/Soup-3.0.typelib'>

    @pytest.mark.parametrize("Soup", ["3.0"], indirect=True)
    @pytest.mark.parametrize(
        "url", urls
    )
    def test_soup3(url, Soup):
        mes = Soup.Message.new_from_encoded_form("GET", url, "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: g-tls-error-quark: Error reading data from TLS socket: The specified session has been invalidated for some reason. (1)

test_soup.py:29: Error
------------------------------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------------------------------
(process:1414229): GLib-GIO-DEBUG: 14:23:17.563: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
(process:1414229): dconf-DEBUG: 14:23:17.563: watch_fast: "/system/proxy/" (establishing: 0, active: 0)
(process:1414229): dconf-DEBUG: 14:23:17.563: watch_fast: "/system/proxy/http/" (establishing: 0, active: 0)
(process:1414229): dconf-DEBUG: 14:23:17.563: watch_fast: "/system/proxy/https/" (establishing: 0, active: 0)
(process:1414229): dconf-DEBUG: 14:23:17.563: watch_fast: "/system/proxy/ftp/" (establishing: 0, active: 0)
(process:1414229): dconf-DEBUG: 14:23:17.563: watch_fast: "/system/proxy/socks/" (establishing: 0, active: 0)
(process:1414229): GLib-GIO-DEBUG: 14:23:17.563: _g_io_module_get_default: Found default implementation gnome (GProxyResolverGnome) for ‘gio-proxy-resolver’
(process:1414229): GLib-GIO-DEBUG: 14:23:17.564: Using cross-namespace EXTERNAL authentication (this will deadlock if server is GDBus < 2.73.3)
(process:1414229): dconf-DEBUG: 14:23:17.566: watch_established: "/system/proxy/" (establishing: 1)
(process:1414229): dconf-DEBUG: 14:23:17.566: watch_established: "/system/proxy/http/" (establishing: 1)
(process:1414229): dconf-DEBUG: 14:23:17.566: watch_established: "/system/proxy/https/" (establishing: 1)
(process:1414229): dconf-DEBUG: 14:23:17.566: watch_established: "/system/proxy/ftp/" (establishing: 1)
(process:1414229): dconf-DEBUG: 14:23:17.566: watch_established: "/system/proxy/socks/" (establishing: 1)
(process:1414229): GLib-GIO-DEBUG: 14:23:17.587: _g_io_module_get_default: Found default implementation gnutls (GTlsBackendGnutls) for ‘gio-tls-backend’
(process:1414229): GLib-Net-DEBUG: 14:23:17.587: CLIENT[0x26161e0]: Starting synchronous TLS handshake
(process:1414229): GLib-Net-DEBUG: 14:23:17.588: CLIENT[0x26161e0]: TLS handshake thread starts
(process:1414229): GLib-Net-DEBUG: 14:23:17.588: CLIENT[0x26161e0]: claiming operation OP_HANDSHAKE
(process:1414229): GLib-Net-DEBUG: 14:23:17.588: CLIENT[0x26161e0]: claiming operation OP_HANDSHAKE succeeded
(process:1414229): GLib-Net-DEBUG: 14:23:17.621: CLIENT[0x26161e0]: verifying peer certificate
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: TLS handshake thread succeeded
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: synchronous TLS handshake thread completed
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: finishing TLS handshake
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: TLS handshake has finished successfully
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: yielding operation OP_HANDSHAKE
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: starting to write 101 bytes to TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: claiming operation OP_WRITE
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: claiming operation OP_WRITE succeeded
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: yielding operation OP_WRITE
(process:1414229): GLib-Net-DEBUG: 14:23:17.637: CLIENT[0x26161e0]: successfully write 101 bytes to TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.638: CLIENT[0x26161e0]: starting to read data from TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.638: CLIENT[0x26161e0]: claiming operation OP_READ
(process:1414229): GLib-Net-DEBUG: 14:23:17.638: CLIENT[0x26161e0]: claiming operation OP_READ succeeded
(process:1414229): GLib-Net-DEBUG: 14:23:17.661: CLIENT[0x26161e0]: yielding operation OP_READ
(process:1414229): GLib-Net-DEBUG: 14:23:17.661: CLIENT[0x26161e0]: successfully read 40 bytes from TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.662: CLIENT[0x26161e0]: starting to read data from TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.662: CLIENT[0x26161e0]: claiming operation OP_READ
(process:1414229): GLib-Net-DEBUG: 14:23:17.662: CLIENT[0x26161e0]: claiming operation OP_READ succeeded
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: yielding operation OP_READ
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: successfully read 39 bytes from TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: starting to read data from TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: claiming operation OP_READ
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: claiming operation OP_READ succeeded
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: yielding operation OP_READ
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: successfully read 0 bytes from TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: starting to read data from TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: claiming operation OP_READ
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: claiming operation OP_READ succeeded
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: yielding operation OP_READ
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: reading data from TLS connection has failed: ERROR
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: starting to close the TLS connection
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: claiming operation OP_CLOSE_BOTH
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: claiming operation OP_CLOSE_BOTH succeeded
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: yielding operation OP_CLOSE_BOTH
(process:1414229): GLib-Net-DEBUG: 14:23:17.664: CLIENT[0x26161e0]: the TLS connection has been closed successfully
___________________________________________________________________________________________________ test_soup3[https://www.bbc.co.uk/-3.0] ___________________________________________________________________________________________________
url = 'https://www.bbc.co.uk/', Soup = <IntrospectionModule 'Soup' from '/usr/lib/x86_64-linux-gnu/girepository-1.0/Soup-3.0.typelib'>

    @pytest.mark.parametrize("Soup", ["3.0"], indirect=True)
    @pytest.mark.parametrize(
        "url", urls
    )
    def test_soup3(url, Soup):
        mes = Soup.Message.new_from_encoded_form("GET", url, "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: soup-session-error-quark: Could not parse HTTP response (0)

test_soup.py:29: Error
------------------------------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------------------------------
(process:1414234): GLib-GIO-DEBUG: 14:23:17.726: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
(process:1414234): dconf-DEBUG: 14:23:17.726: watch_fast: "/system/proxy/" (establishing: 0, active: 0)
(process:1414234): dconf-DEBUG: 14:23:17.726: watch_fast: "/system/proxy/http/" (establishing: 0, active: 0)
(process:1414234): dconf-DEBUG: 14:23:17.726: watch_fast: "/system/proxy/https/" (establishing: 0, active: 0)
(process:1414234): dconf-DEBUG: 14:23:17.726: watch_fast: "/system/proxy/ftp/" (establishing: 0, active: 0)
(process:1414234): dconf-DEBUG: 14:23:17.726: watch_fast: "/system/proxy/socks/" (establishing: 0, active: 0)
(process:1414234): GLib-GIO-DEBUG: 14:23:17.727: _g_io_module_get_default: Found default implementation gnome (GProxyResolverGnome) for ‘gio-proxy-resolver’
(process:1414234): GLib-GIO-DEBUG: 14:23:17.727: Using cross-namespace EXTERNAL authentication (this will deadlock if server is GDBus < 2.73.3)
(process:1414234): dconf-DEBUG: 14:23:17.729: watch_established: "/system/proxy/" (establishing: 1)
(process:1414234): dconf-DEBUG: 14:23:17.729: watch_established: "/system/proxy/http/" (establishing: 1)
(process:1414234): dconf-DEBUG: 14:23:17.729: watch_established: "/system/proxy/https/" (establishing: 1)
(process:1414234): dconf-DEBUG: 14:23:17.729: watch_established: "/system/proxy/ftp/" (establishing: 1)
(process:1414234): dconf-DEBUG: 14:23:17.729: watch_established: "/system/proxy/socks/" (establishing: 1)
(process:1414234): GLib-GIO-DEBUG: 14:23:17.749: _g_io_module_get_default: Found default implementation gnutls (GTlsBackendGnutls) for ‘gio-tls-backend’
(process:1414234): GLib-Net-DEBUG: 14:23:17.750: CLIENT[0x26181e0]: Starting synchronous TLS handshake
(process:1414234): GLib-Net-DEBUG: 14:23:17.750: CLIENT[0x26181e0]: TLS handshake thread starts
(process:1414234): GLib-Net-DEBUG: 14:23:17.750: CLIENT[0x26181e0]: claiming operation OP_HANDSHAKE
(process:1414234): GLib-Net-DEBUG: 14:23:17.750: CLIENT[0x26181e0]: claiming operation OP_HANDSHAKE succeeded
(process:1414234): GLib-Net-DEBUG: 14:23:17.818: CLIENT[0x26181e0]: verifying peer certificate
(process:1414234): GLib-Net-DEBUG: 14:23:17.841: CLIENT[0x26181e0]: TLS handshake thread succeeded
(process:1414234): GLib-Net-DEBUG: 14:23:17.841: CLIENT[0x26181e0]: synchronous TLS handshake thread completed
(process:1414234): GLib-Net-DEBUG: 14:23:17.841: CLIENT[0x26181e0]: finishing TLS handshake
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: TLS handshake has finished successfully
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: yielding operation OP_HANDSHAKE
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: starting to write 100 bytes to TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: claiming operation OP_WRITE
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: claiming operation OP_WRITE succeeded
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: yielding operation OP_WRITE
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: successfully write 100 bytes to TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: starting to read data from TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: claiming operation OP_READ
(process:1414234): GLib-Net-DEBUG: 14:23:17.842: CLIENT[0x26181e0]: claiming operation OP_READ succeeded
(process:1414234): GLib-Net-DEBUG: 14:23:17.859: CLIENT[0x26181e0]: yielding operation OP_READ
(process:1414234): GLib-Net-DEBUG: 14:23:17.859: CLIENT[0x26181e0]: successfully read 40 bytes from TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.859: CLIENT[0x26181e0]: starting to read data from TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.859: CLIENT[0x26181e0]: claiming operation OP_READ
(process:1414234): GLib-Net-DEBUG: 14:23:17.859: CLIENT[0x26181e0]: claiming operation OP_READ succeeded
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: yielding operation OP_READ
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: successfully read 17 bytes from TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: starting to read data from TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: claiming operation OP_READ
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: claiming operation OP_READ succeeded
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: yielding operation OP_READ
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: successfully read 0 bytes from TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: starting to read data from TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: claiming operation OP_READ
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: claiming operation OP_READ succeeded
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: yielding operation OP_READ
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: successfully read 0 bytes from TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: starting to close the TLS connection
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: claiming operation OP_CLOSE_BOTH
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: claiming operation OP_CLOSE_BOTH succeeded
(process:1414234): GLib-Net-DEBUG: 14:23:17.863: CLIENT[0x26181e0]: yielding operation OP_CLOSE_BOTH
(process:1414234): GLib-Net-DEBUG: 14:23:17.864: CLIENT[0x26181e0]: the TLS connection has been closed successfully
-------------------------------------------------------------------------- generated html file: file:///home/example.com/yrro/src/soup3-debugging/report.html ---------------------------------------------------------------------------
========================================================================================================== short test summary info ===========================================================================================================
FAILED test_soup.py::test_soup3[https://www.bing.com/-3.0]
FAILED test_soup.py::test_soup3[https://www.google.com/-3.0]
FAILED test_soup.py::test_soup3[https://www.bbc.co.uk/-3.0]
================================================================================================== 3 failed, 12 passed, 3 skipped in 4.53s ===================================================================================================
```
