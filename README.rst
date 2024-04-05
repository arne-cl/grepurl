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

Installation using pip
----------------------

::

    pip install grepurl

Installation from repository
----------------------------

::

    git clone https://github.com/arne-cl/grepurl
    cd grepurl
    pip install -e .

License
-------

GPLv2 or later.


Authors
-------

Gerome Fournier (original author). His implementation is only available via the
`Internet Archive`_.

Arne Neumann (added -l option for local files, minor changes).

GPT-4 (rewrote the script for Python 3 compatibility).

.. _`Internet Archive`: http://web.archive.org/web/20101116071317/http://jefke.free.fr/stuff/python/grepurl/grepurl
