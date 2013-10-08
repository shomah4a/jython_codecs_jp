#-*- coding:utf-8 -*-

import java

from org.python.core import util


def wrap(s):

    if s < 0:
        return s + 0x100

    return s



def unicode_to_sjis(s):

    sjis = java.nio.charset.Charset.forName('Shift_JIS')

    result = []

    for x in sjis.encode(s).array():

        if x == '\0':
            break

        result.append(chr(wrap(x)))

    return ''.join(result)



def sjis_to_unicode(s):

    buf = java.nio.ByteBuffer.allocate(len(s) * 4)
    buf.put(util.StringUtil.toBytes(s))
    buf.position(0)
    sjis = java.nio.charset.Charset.forName('Shift_JIS')
    ary = sjis.decode(buf).array()

    result = []

    for x in ary:

        if x == '\0':
            break

        result.append(unichr(ord(x)))

    return u''.join(result)



def encode(s):

    return unicode_to_sjis(s), len(s)


def decode(s):

    return sjis_to_unicode(s), len(s)
