import json


def toBin(huff_code):
    str_huff_code = json.dumps(huff_code)

    bin_huff_code = ""

    for s in str_huff_code:
        bin_huff_code += bin(ord(s))[2:].rjust(8, "0")

    # print(bin_huff_code)

    return bin_huff_code
