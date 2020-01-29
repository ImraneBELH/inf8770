import lzw
from run_len import calculate_compression_ratio

file = lzw.readbytes("Unknown.bmp")

lzw.writebytes("compressed",lzw.decompress(file))