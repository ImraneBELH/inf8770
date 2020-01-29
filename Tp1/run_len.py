import re


# RLE(run-length encoding) decoder
def decode(string):
    if string == '':
        return ''
    multiplier = 1
    count = 0
    rle_decoding = []

    rle_encoding = []
    # magic regex below  shamelessly pulled from stack overflow: https://stackoverflow.com/questions/33533393/split-string-into-letters-and-numbers?rq=1
    # [\w\s] at the end parses whitespace into the list, now works for encodings with whitespace
    rle_encoding = re.findall(r'[A-Za-z]|-?\d+\.\d+|\d+|[\w\s]', string)
    for item in rle_encoding:
        if item.isdigit():
            multiplier = int(item)
        elif item.isalpha() or item.isspace():
            while count < multiplier:
                rle_decoding.append('{0}'.format(item))
                count += 1
            multiplier = 1
            count = 0
    final = ''.join(rle_decoding)
    return final


# RLE(run-length encoding) encoder
def encode(string):
    if string == '':
        return ''
    i = 0
    count = 0
    letter = string[i]
    rle = []
    while i <= len(string) - 1:
        while string[i] == letter:
            i += 1
            count += 1
            # catch the loop on last character so it doesn't got to top and access out of bounds
            if i > len(string) - 1:
                break
        if count == 1:
            rle.append('{0}'.format(letter))
        else:
            rle.append('{0}{1}'.format(count, letter))
        if i > len(string) - 1:  # ugly that I have to do it twice
            break
        letter = string[i]
        count = 0
    # join list of strings together to create one string to return
    final = ''.join(rle)
    print(final)
    return final


def utf8len(s):
    return len(s.encode('utf-8'))


def calculate_compression_ratio(m, m_e):
    message_length_in_bytes = utf8len(m)
    message_encoded_length_in_bytes = utf8len(m_e)
    ratio = (message_encoded_length_in_bytes / message_length_in_bytes) * 100
    print(str(100 - ratio) + '%')


message = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'
messageEncoded = encode(message)
calculate_compression_ratio(message, messageEncoded)

decode('2 hs2q q2w2 ')