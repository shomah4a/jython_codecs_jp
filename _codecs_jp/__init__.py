#-*- coding: utf-8 -*-

import codecs

from . import sjis

CODEC_MAP = {
    'cp932': sjis,
    'sjis': sjis,
    'Shift_JIS': sjis,
    }


def getcodec(name):

    m = CODEC_MAP.get(name)

    if m is None:
        return None

    return m.encode, m.decode, None, None



codecs.register(getcodec)





