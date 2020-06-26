#!/usr/bin/env python3
# encoding: utf-8

from pornhub_api import PornhubApi
import getopt, sys

version='1.0'
api = PornhubApi()


def search(text):
    data = api.search.search(
    text,
    ordering="mostviewed",
    period="weekly",)
    for vid in data.videos:
        print(vid.title,";",vid.url)


def usage():
    print ('''
Usage:
    pornhub -h | pornhub --help
    pornhub -v | pornhub --version"
    pornhub -s <search>
    pornhub --search=<search>
    ''')

def main(argv=None):

    searchText=None
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hs:v", ["help", "search=","version"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(1)

    for opt,arg in opts:
        if opt in ('-v', '--version'):
            print( argv[0] + " " + version)
            sys.exit(0)
        if opt in ('-s', '--search'):
            searchText = arg
        if opt in ('-h', '--help'):
            usage()
            sys.exit(0)

    search(searchText)

if __name__ == '__main__':
    main()
