import zlib
import lzma
import lz4.frame as lz4
import bz2

class Compress:
    def __init__(self, content) -> None:
        self.__content = content

    def deflate(self):
        self.__content_compressed = zlib.compress(self.__content)
        return self.__content_compressed

    def lzma(self):
        self.__content_compressed = lzma.compress(self.__content)
        return self.__content_compressed

    def lz4(self):
        self.__content_compressed = lz4.compress(self.__content)
        return self.__content_compressed

    def BZip2(self):
        self.__content_compressed = bz2.compress(self.__content)
        return self.__content_compressed