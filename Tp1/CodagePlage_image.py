# import lzw
# import os
# from run_len import calculate_compression_ratio
#
#
#
# file = lzw.readbytes("haha")
#
# print(file.gi_frame)
# lzw.writebytes("done.bmp",lzw.decompress(file))
#
# bytes = "hahahhahahhaha"
#
# h = b" ".join(lzw.compress(bytes))
# print(bytes)
# print(str(h))
#
# print(os.stat('haha').st_size)
#
# print(os.stat('badr.bmp').st_size)
#
# print(calculate_compression_ratio(os.stat('haha').st_size, os.stat('badr.bmp').st_size))