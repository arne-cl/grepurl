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

License
-------

GPLv2 or later.


Authors
-------

Gerome Fournier (original author).
Arne Neumann (added -l option for local files).
