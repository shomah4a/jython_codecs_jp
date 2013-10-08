#-*- coding: utf-8 -*-

import codecs

import java

from org.python.core import util


def wrap(s):

    if s < 0:
        return s + 0x100

    return s



def unicode2str(s, code):
    u'''
    unicode 文字列を code で指定した文字コードの文字列に変換
    '''

    sjis = java.nio.charset.Charset.forName(code)

    result = []

    for x in sjis.encode(s).array():

        if x == '\0':
            break

        result.append(chr(wrap(x)))

    return ''.join(result)



def str2unicode(s, code):
    u'''
    文字列を code で指定した文字コードを使って unicode 文字列に変換
    '''

    buf = java.nio.ByteBuffer.allocate(len(s) * 4)
    buf.put(util.StringUtil.toBytes(s))
    buf.position(0)
    sjis = java.nio.charset.Charset.forName(code)
    ary = sjis.decode(buf).array()

    result = []

    for x in ary:

        if x == '\0':
            break

        result.append(unichr(ord(x)))

    return u''.join(result)



class CodecInfo(object):

    def __init__(self, code):

        self.code = code


    def encode(self, s):

        return unicode2str(s, self.code), len(s)


    def decode(self, s):

        return str2unicode(s, self.code), len(s)




CODEC_MAP = {
    'cp932': CodecInfo('MS932'),
    'sjis': CodecInfo('Shift_JIS'),
    'Shift_JIS': CodecInfo('Shift_JIS'),
    'eucjp': CodecInfo('EUC-JP'),
    'euc-jp': CodecInfo('EUC-JP'),
    }


def getcodec(name):

    m = CODEC_MAP.get(name)

    if m is None:
        return None

    return m.encode, m.decode, None, None



codecs.register(getcodec)





