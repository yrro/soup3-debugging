# libsoup 3 connection reset test cases

Sample output; note that `test_soup2` and `test_urllib` pass; only `test_soup3`
fails.

To run the tests, you will need the Python packages `python-pytest` and
`python-pytest` available to your system Python environment.

Here's the output of running the tests on my machine. A [nicer HTML-formatted
report](https://raw.github.com/yrro/soup3-debugging/master/report.html) is also
available.

```
$ pytest --forked -v
============================================================================================= test session starts ==============================================================================================
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
metadata: {'Python': '3.11.2', 'Platform': 'Linux-6.1.0-3-amd64-x86_64-with-glibc2.36', 'Packages': {'pytest': '7.2.1', 'pluggy': '0.13.0'}, 'Plugins': {'metadata': '2.0.4', 'html': '3.2.0', 'xdist': '3.1.0', 'forked': '1.4.0'}}
rootdir: /home/phe.gov.uk/sam.morris/src/soup3-debugging
plugins: metadata-2.0.4, html-3.2.0, xdist-3.1.0, forked-1.4.0
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
    
        mes = Soup.Message.new_from_encoded_form("GET", url, "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: g-io-error-quark: Error receiving data: Connection reset by peer (44)

test_urllibs.py:40: Error
--------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------
(process:1278228): GLib-GIO-DEBUG: 13:09:58.318: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
(process:1278228): dconf-DEBUG: 13:09:58.318: watch_fast: "/system/proxy/" (establishing: 0, active: 0)
(process:1278228): dconf-DEBUG: 13:09:58.318: watch_fast: "/system/proxy/http/" (establishing: 0, active: 0)
(process:1278228): dconf-DEBUG: 13:09:58.318: watch_fast: "/system/proxy/https/" (establishing: 0, active: 0)
(process:1278228): dconf-DEBUG: 13:09:58.318: watch_fast: "/system/proxy/ftp/" (establishing: 0, active: 0)
(process:1278228): dconf-DEBUG: 13:09:58.318: watch_fast: "/system/proxy/socks/" (establishing: 0, active: 0)
(process:1278228): GLib-GIO-DEBUG: 13:09:58.318: _g_io_module_get_default: Found default implementation gnome (GProxyResolverGnome) for ‘gio-proxy-resolver’
(process:1278228): GLib-GIO-DEBUG: 13:09:58.318: Using cross-namespace EXTERNAL authentication (this will deadlock if server is GDBus < 2.73.3)
(process:1278228): dconf-DEBUG: 13:09:58.320: watch_established: "/system/proxy/" (establishing: 1)
(process:1278228): dconf-DEBUG: 13:09:58.320: watch_established: "/system/proxy/http/" (establishing: 1)
(process:1278228): dconf-DEBUG: 13:09:58.320: watch_established: "/system/proxy/https/" (establishing: 1)
(process:1278228): dconf-DEBUG: 13:09:58.320: watch_established: "/system/proxy/ftp/" (establishing: 1)
(process:1278228): dconf-DEBUG: 13:09:58.320: watch_established: "/system/proxy/socks/" (establishing: 1)
(process:1278228): GLib-GIO-DEBUG: 13:09:58.353: _g_io_module_get_default: Found default implementation gnutls (GTlsBackendGnutls) for ‘gio-tls-backend’
(process:1278228): GLib-Net-DEBUG: 13:09:58.354: CLIENT[0x28c61c0]: Starting synchronous TLS handshake
(process:1278228): GLib-Net-DEBUG: 13:09:58.354: CLIENT[0x28c61c0]: TLS handshake thread starts
(process:1278228): GLib-Net-DEBUG: 13:09:58.354: CLIENT[0x28c61c0]: claiming operation OP_HANDSHAKE
(process:1278228): GLib-Net-DEBUG: 13:09:58.354: CLIENT[0x28c61c0]: claiming operation OP_HANDSHAKE succeeded
(process:1278228): GLib-Net-DEBUG: 13:09:58.377: CLIENT[0x28c61c0]: verifying peer certificate
(process:1278228): GLib-Net-DEBUG: 13:09:58.414: CLIENT[0x28c61c0]: TLS handshake thread succeeded
(process:1278228): GLib-Net-DEBUG: 13:09:58.414: CLIENT[0x28c61c0]: synchronous TLS handshake thread completed
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: finishing TLS handshake
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: TLS handshake has finished successfully
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: yielding operation OP_HANDSHAKE
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: starting to write 99 bytes to TLS connection
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: claiming operation OP_WRITE
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: claiming operation OP_WRITE succeeded
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: yielding operation OP_WRITE
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: successfully write 99 bytes to TLS connection
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: starting to read data from TLS connection
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: claiming operation OP_READ
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: claiming operation OP_READ succeeded
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: yielding operation OP_READ
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: successfully read 40 bytes from TLS connection
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: starting to read data from TLS connection
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: claiming operation OP_READ
(process:1278228): GLib-Net-DEBUG: 13:09:58.415: CLIENT[0x28c61c0]: claiming operation OP_READ succeeded
(process:1278228): GLib-Net-DEBUG: 13:09:58.432: CLIENT[0x28c61c0]: yielding operation OP_READ
(process:1278228): GLib-Net-DEBUG: 13:09:58.432: CLIENT[0x28c61c0]: reading data from TLS connection has failed: ERROR
(process:1278228): GLib-Net-DEBUG: 13:09:58.433: CLIENT[0x28c61c0]: starting to close the TLS connection
(process:1278228): GLib-Net-DEBUG: 13:09:58.433: CLIENT[0x28c61c0]: claiming operation OP_CLOSE_BOTH
(process:1278228): GLib-Net-DEBUG: 13:09:58.433: CLIENT[0x28c61c0]: claiming operation OP_CLOSE_BOTH succeeded
(process:1278228): GLib-Net-DEBUG: 13:09:58.433: CLIENT[0x28c61c0]: yielding operation OP_CLOSE_BOTH
(process:1278228): GLib-Net-DEBUG: 13:09:58.433: CLIENT[0x28c61c0]: error closing TLS connection: Error sending data: Broken pipe
_____________________________________________________________________________________ test_soup3[https://www.google.com/] ______________________________________________________________________________________
url = 'https://www.google.com/', soup3 = None

    @pytest.mark.parametrize(
        "url", test_urls
    )
    def test_soup3(url, soup3):
        from gi.repository import Soup
    
        mes = Soup.Message.new_from_encoded_form("GET", url, "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: g-tls-error-quark: Error reading data from TLS socket: The specified session has been invalidated for some reason. (1)

test_urllibs.py:40: Error
--------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------
(process:1278236): GLib-GIO-DEBUG: 13:09:58.483: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
(process:1278236): dconf-DEBUG: 13:09:58.484: watch_fast: "/system/proxy/" (establishing: 0, active: 0)
(process:1278236): dconf-DEBUG: 13:09:58.484: watch_fast: "/system/proxy/http/" (establishing: 0, active: 0)
(process:1278236): dconf-DEBUG: 13:09:58.484: watch_fast: "/system/proxy/https/" (establishing: 0, active: 0)
(process:1278236): dconf-DEBUG: 13:09:58.484: watch_fast: "/system/proxy/ftp/" (establishing: 0, active: 0)
(process:1278236): dconf-DEBUG: 13:09:58.484: watch_fast: "/system/proxy/socks/" (establishing: 0, active: 0)
(process:1278236): GLib-GIO-DEBUG: 13:09:58.484: _g_io_module_get_default: Found default implementation gnome (GProxyResolverGnome) for ‘gio-proxy-resolver’
(process:1278236): GLib-GIO-DEBUG: 13:09:58.485: Using cross-namespace EXTERNAL authentication (this will deadlock if server is GDBus < 2.73.3)
(process:1278236): dconf-DEBUG: 13:09:58.487: watch_established: "/system/proxy/" (establishing: 1)
(process:1278236): dconf-DEBUG: 13:09:58.487: watch_established: "/system/proxy/http/" (establishing: 1)
(process:1278236): dconf-DEBUG: 13:09:58.487: watch_established: "/system/proxy/https/" (establishing: 1)
(process:1278236): dconf-DEBUG: 13:09:58.487: watch_established: "/system/proxy/ftp/" (establishing: 1)
(process:1278236): dconf-DEBUG: 13:09:58.487: watch_established: "/system/proxy/socks/" (establishing: 1)
(process:1278236): GLib-GIO-DEBUG: 13:09:58.524: _g_io_module_get_default: Found default implementation gnutls (GTlsBackendGnutls) for ‘gio-tls-backend’
(process:1278236): GLib-Net-DEBUG: 13:09:58.524: CLIENT[0x28d21c0]: Starting synchronous TLS handshake
(process:1278236): GLib-Net-DEBUG: 13:09:58.525: CLIENT[0x28d21c0]: TLS handshake thread starts
(process:1278236): GLib-Net-DEBUG: 13:09:58.525: CLIENT[0x28d21c0]: claiming operation OP_HANDSHAKE
(process:1278236): GLib-Net-DEBUG: 13:09:58.525: CLIENT[0x28d21c0]: claiming operation OP_HANDSHAKE succeeded
(process:1278236): GLib-Net-DEBUG: 13:09:58.556: CLIENT[0x28d21c0]: verifying peer certificate
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: TLS handshake thread succeeded
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: synchronous TLS handshake thread completed
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: finishing TLS handshake
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: TLS handshake has finished successfully
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: yielding operation OP_HANDSHAKE
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: starting to write 101 bytes to TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: claiming operation OP_WRITE
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: claiming operation OP_WRITE succeeded
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: yielding operation OP_WRITE
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: successfully write 101 bytes to TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.574: CLIENT[0x28d21c0]: starting to read data from TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.575: CLIENT[0x28d21c0]: claiming operation OP_READ
(process:1278236): GLib-Net-DEBUG: 13:09:58.575: CLIENT[0x28d21c0]: claiming operation OP_READ succeeded
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: yielding operation OP_READ
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: successfully read 40 bytes from TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: starting to read data from TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: claiming operation OP_READ
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: claiming operation OP_READ succeeded
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: yielding operation OP_READ
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: successfully read 39 bytes from TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: starting to read data from TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: claiming operation OP_READ
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: claiming operation OP_READ succeeded
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: yielding operation OP_READ
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: successfully read 0 bytes from TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: starting to read data from TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: claiming operation OP_READ
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: claiming operation OP_READ succeeded
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: yielding operation OP_READ
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: reading data from TLS connection has failed: ERROR
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: starting to close the TLS connection
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: claiming operation OP_CLOSE_BOTH
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: claiming operation OP_CLOSE_BOTH succeeded
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: yielding operation OP_CLOSE_BOTH
(process:1278236): GLib-Net-DEBUG: 13:09:58.596: CLIENT[0x28d21c0]: the TLS connection has been closed successfully
______________________________________________________________________________________ test_soup3[https://www.bbc.co.uk/] ______________________________________________________________________________________
url = 'https://www.bbc.co.uk/', soup3 = None

    @pytest.mark.parametrize(
        "url", test_urls
    )
    def test_soup3(url, soup3):
        from gi.repository import Soup
    
        mes = Soup.Message.new_from_encoded_form("GET", url, "")
    
        ses = Soup.Session()
>       ses.send_and_read(mes)
E       gi.repository.GLib.GError: soup-session-error-quark: Could not parse HTTP response (0)

test_urllibs.py:40: Error
--------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------
(process:1278241): GLib-GIO-DEBUG: 13:09:58.646: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
(process:1278241): dconf-DEBUG: 13:09:58.646: watch_fast: "/system/proxy/" (establishing: 0, active: 0)
(process:1278241): dconf-DEBUG: 13:09:58.646: watch_fast: "/system/proxy/http/" (establishing: 0, active: 0)
(process:1278241): dconf-DEBUG: 13:09:58.646: watch_fast: "/system/proxy/https/" (establishing: 0, active: 0)
(process:1278241): dconf-DEBUG: 13:09:58.646: watch_fast: "/system/proxy/ftp/" (establishing: 0, active: 0)
(process:1278241): dconf-DEBUG: 13:09:58.646: watch_fast: "/system/proxy/socks/" (establishing: 0, active: 0)
(process:1278241): GLib-GIO-DEBUG: 13:09:58.646: _g_io_module_get_default: Found default implementation gnome (GProxyResolverGnome) for ‘gio-proxy-resolver’
(process:1278241): GLib-GIO-DEBUG: 13:09:58.647: Using cross-namespace EXTERNAL authentication (this will deadlock if server is GDBus < 2.73.3)
(process:1278241): dconf-DEBUG: 13:09:58.649: watch_established: "/system/proxy/" (establishing: 1)
(process:1278241): dconf-DEBUG: 13:09:58.649: watch_established: "/system/proxy/http/" (establishing: 1)
(process:1278241): dconf-DEBUG: 13:09:58.649: watch_established: "/system/proxy/https/" (establishing: 1)
(process:1278241): dconf-DEBUG: 13:09:58.649: watch_established: "/system/proxy/ftp/" (establishing: 1)
(process:1278241): dconf-DEBUG: 13:09:58.649: watch_established: "/system/proxy/socks/" (establishing: 1)
(process:1278241): GLib-GIO-DEBUG: 13:09:58.702: _g_io_module_get_default: Found default implementation gnutls (GTlsBackendGnutls) for ‘gio-tls-backend’
(process:1278241): GLib-Net-DEBUG: 13:09:58.702: CLIENT[0x28d41c0]: Starting synchronous TLS handshake
(process:1278241): GLib-Net-DEBUG: 13:09:58.702: CLIENT[0x28d41c0]: TLS handshake thread starts
(process:1278241): GLib-Net-DEBUG: 13:09:58.702: CLIENT[0x28d41c0]: claiming operation OP_HANDSHAKE
(process:1278241): GLib-Net-DEBUG: 13:09:58.702: CLIENT[0x28d41c0]: claiming operation OP_HANDSHAKE succeeded
(process:1278241): GLib-Net-DEBUG: 13:09:58.748: CLIENT[0x28d41c0]: verifying peer certificate
(process:1278241): GLib-Net-DEBUG: 13:09:58.765: CLIENT[0x28d41c0]: TLS handshake thread succeeded
(process:1278241): GLib-Net-DEBUG: 13:09:58.765: CLIENT[0x28d41c0]: synchronous TLS handshake thread completed
(process:1278241): GLib-Net-DEBUG: 13:09:58.765: CLIENT[0x28d41c0]: finishing TLS handshake
(process:1278241): GLib-Net-DEBUG: 13:09:58.765: CLIENT[0x28d41c0]: TLS handshake has finished successfully
(process:1278241): GLib-Net-DEBUG: 13:09:58.765: CLIENT[0x28d41c0]: yielding operation OP_HANDSHAKE
(process:1278241): GLib-Net-DEBUG: 13:09:58.765: CLIENT[0x28d41c0]: starting to write 100 bytes to TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.766: CLIENT[0x28d41c0]: claiming operation OP_WRITE
(process:1278241): GLib-Net-DEBUG: 13:09:58.766: CLIENT[0x28d41c0]: claiming operation OP_WRITE succeeded
(process:1278241): GLib-Net-DEBUG: 13:09:58.766: CLIENT[0x28d41c0]: yielding operation OP_WRITE
(process:1278241): GLib-Net-DEBUG: 13:09:58.766: CLIENT[0x28d41c0]: successfully write 100 bytes to TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.766: CLIENT[0x28d41c0]: starting to read data from TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.766: CLIENT[0x28d41c0]: claiming operation OP_READ
(process:1278241): GLib-Net-DEBUG: 13:09:58.766: CLIENT[0x28d41c0]: claiming operation OP_READ succeeded
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: yielding operation OP_READ
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: successfully read 57 bytes from TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: starting to read data from TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: claiming operation OP_READ
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: claiming operation OP_READ succeeded
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: yielding operation OP_READ
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: successfully read 0 bytes from TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: starting to read data from TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: claiming operation OP_READ
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: claiming operation OP_READ succeeded
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: yielding operation OP_READ
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: successfully read 0 bytes from TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: starting to close the TLS connection
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: claiming operation OP_CLOSE_BOTH
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: claiming operation OP_CLOSE_BOTH succeeded
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: yielding operation OP_CLOSE_BOTH
(process:1278241): GLib-Net-DEBUG: 13:09:58.784: CLIENT[0x28d41c0]: the TLS connection has been closed successfully
=========================================================================================== short test summary info ============================================================================================
FAILED test_urllibs.py::test_soup3[https://www.bing.com/]
FAILED test_urllibs.py::test_soup3[https://www.google.com/]
FAILED test_urllibs.py::test_soup3[https://www.bbc.co.uk/]
========================================================================================= 3 failed, 6 passed in 2.35s ==========================================================================================
```
