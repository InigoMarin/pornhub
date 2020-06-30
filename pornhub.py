#!/usr/bin/env python3
# encoding: utf-8

from pornhub_api import PornhubApi
import getopt
import sys

version = '1.0'
api = PornhubApi()


def search(text, page):
    data = api.search.search(text, page=page, ordering="mostviewed")
    for vid in data.videos:
        print(vid.title, ";", vid.url)


def usage():
    print('''
Usage:
    pornhub.py -h | pornhub.py --help
    pornhub.py -v | pornhub.py --version"
    pornhub.py -s <search>
    pornhub.py -s <search> -p <page>
    pornhub.py --search=<search>
    ''')


def main(argv=None):

    searchText = None
    page = 1
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:p:v", [
                                   "help", "search=", "page=", "version"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-v', '--version'):
            print(argv[0] + " " + version)
            sys.exit(0)
        if opt in ('-s', '--search'):
            searchText = arg
        if opt in ('-p', '--page'):
            page = arg
        if opt in ('-h', '--help'):
            usage()
            sys.exit(0)

    search(searchText, page)


if __name__ == '__main__':
    main()
