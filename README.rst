grepurl
=======

``grepurl`` is a command line tool that extracts URLs from a website (or a
local HTML file).

Usage
-----

::

    grepurl http://example.com/
    grepurl -a http://example.com/foo.htm # only extract from <a> tags (i.e. links)
    grepurl -i http://example.com/bar.htm # only extract from <img> tags (i.e. images)
    grepurl -r "\.py$" http://example.com/ # only extract links that end in '.py'

Installation
------------

::

    sudo apt install libcurl4-openssl-dev
    sudo python setup.py install

License
-------

GPLv2 or later.


Authors
-------

Gerome Fournier (original author). His implementation is only available via the
`Internet Archive`_.

Arne Neumann (added -l option for local files, minor changes).

.. _`Internet Archive`: http://web.archive.org/web/20101116071317/http://jefke.free.fr/stuff/python/grepurl/grepurl
