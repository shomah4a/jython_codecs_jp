#-*- coding:utf-8 -*-

import sys

def main():


    if len(sys.argv) > 1:
        codec = sys.argv[1]
    else:
        codec = 'sjis'

    print u'あいうえお'.encode(codec)



if __name__ == '__main__':
    main()
