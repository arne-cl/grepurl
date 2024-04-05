#!/usr/bin/env python3

"""
grepurl.py: A utility for extracting and optionally downloading URLs
from web pages or local HTML files.

This script allows users to fetch URLs embedded within <a> tags and
<img> tags from either web pages accessed via HTTP requests or local
HTML files.

It supports filtering URLs based on regular expressions,
selectively processing only <a> tags or <img> tags, and downloading the
resources pointed to by these URLs. 
"""

import argparse
import os
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests


def fetch_urls(source, only_a=False, only_img=False, regexp=None, is_local=False):
    """
    Fetch URLs from a web page or a local HTML file.
    
    Parameters
    ----------
    source : str
        The URL of the web page or the path to a local file to process.
    only_a : bool, optional
        If True, fetch URLs only from <a> tags. Default is False.
    only_img : bool, optional
        If True, fetch URLs only from <img> tags. Default is False.
    regexp : str, optional
        A regular expression pattern to filter the URLs. Only URLs
        matching the pattern will be returned. Default is None.
    is_local : bool, optional
        If True, treat the source as a local file path. Otherwise,
        treat it as a URL. Default is False.

    Returns
    -------
    set
        A set of URLs extracted from the specified source, filtered by
        the given criteria.
    """
    urls = set()
    if is_local:
        with open(source, 'r') as file:
            content = file.read()
    else:
        response = requests.get(source)
        content = response.text

    soup = BeautifulSoup(content, 'html.parser')

    if not only_img:  # process <a> tags unless we're only processing <img> tags
        for link in soup.find_all('a', href=True):
            urls.add(link['href'])

    if not only_a:  # process <img> tags unless we're only processing <a> tags
        for img in soup.find_all('img', src=True):
            urls.add(img['src'])

    if regexp:
        regexp_compiled = re.compile(regexp)
        urls = {url for url in urls if regexp_compiled.search(url)}

    return urls

def download_resource(url, output_dir, base_url=None):
    """
    Download a resource from the given URL and save it to the specified
    output directory.
    
    Parameters
    ----------
    url : str
        The URL of the resource to download. If `base_url` is provided,
        `url` is treated as a relative URL.
    output_dir : str
        The directory where the downloaded resource will be saved.
    base_url : str, optional
        The base URL to be joined with a relative URL. Default is None,
        meaning `url` is considered an absolute URL.

    Returns
    -------
    None
        The resource is saved to a file in the specified output directory.
    """
    if not base_url:
        resource = requests.get(url)
    else:
        full_url = urljoin(base_url, url)
        resource = requests.get(full_url)

    filename = url.split('/')[-1]
    path = os.path.join(output_dir, filename)

    with open(path, 'wb') as file:
        file.write(resource.content)

def main():
    parser = argparse.ArgumentParser(
        description='Grep URLs from a web page and eventually download the resources they point to.')
    parser.add_argument('URL', nargs='*', help='URL(s) to process')
    parser.add_argument('-a', '--only-a', action='store_true',
        help='grep only URLs inside <a> tags')
    parser.add_argument('-i', '--only-img', action='store_true',
        help='grep only URLs inside <img> tags')
    parser.add_argument('-r', '--regexp', metavar='<regexp>',
        help="return only URLs matching '<regexp>'")
    parser.add_argument('-d', '--download', action='store_true',
        help='download resources')
    parser.add_argument('-o', '--output-dir', metavar='<dir>',
        help="store downloaded resources inside '<dir>'", default='.')
    parser.add_argument('-l', '--local', action='store_true',
        help='grep URLs from a LOCAL file')

    args = parser.parse_args()

    if not args.URL and not args.local:
        print("Please provide at least one URL or specify --local to process files.")
        return

    sources = args.URL if not args.local else args.URL[0]

    if args.local:
        urls = fetch_urls(sources, args.only_a, args.only_img, args.regexp, args.local)
    else:
        urls = set()
        for source in args.URL:
            urls |= fetch_urls(source, args.only_a, args.only_img, args.regexp)

    for url in urls:
        print(url)
        if args.download:
            download_resource(url, args.output_dir, None if args.local else source)


if __name__ == "__main__":
    main()
