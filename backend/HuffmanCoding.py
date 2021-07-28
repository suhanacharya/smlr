import os
from collections import Counter
import heapq
import json
from helper import toBin


class HuffmanCoding:
    def __init__(self):
        self.path = ""
        self.heap = []
        self.codes = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if other == None:
                return False
            if other.char == None:
                return False

            return self.freq == other.freq

    def make_heap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_codes(self):
        while(len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, node, current_code):
        if node == None:
            return

        if node.char != None:
            self.codes[node.char] = current_code

        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        encoded_text = ""

        for character in text:
            encoded_text += self.codes[character]

        return encoded_text

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8

        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)

        encoded_text = padded_info + encoded_text

        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        b = bytearray()

        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i: i+8]
            b.append(int(byte, 2))

        return b

    def compress(self, path):
        self.path = path
        filename, file_ext = os.path.splitext(self.path)
        output_path = filename + "_compressed.bin"
        # dict_path = filename + "_huffman_codes.txt"

        with open(self.path, 'r') as file, open(output_path, 'wb') as output:
            text = file.read().rstrip()
            frequency = dict(Counter(text))
            # print(frequency)
            self.make_heap(frequency)
            self.merge_codes()
            self.make_codes()
            # print(self.codes)
            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)

            padded_huffman_codes = toBin(self.codes)
            padded_huffman_codes_info = bin(len(padded_huffman_codes))[
                2:].rjust(16, "0")

            padded_huffman_codes = padded_huffman_codes_info + padded_huffman_codes

            b = self.get_byte_array(padded_huffman_codes) + b

            output.write(b)

        # with open(dict_path, 'w') as dict_path:
        #     json.dump(self.codes, dict_path)

        print("Compressed Successful!")

        return output_path

    def remove_padding(self, bit_string):
        padded_info = bit_string[:8]
        extra_padding = int(padded_info, 2)

        bit_string = bit_string[8:]
        encoded_text = bit_string[:-1*extra_padding]

        return encoded_text

    def decode_text(self, encoded_text, reverse_mapping):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit

            if current_code in reverse_mapping:
                decoded_text += reverse_mapping[current_code]
                current_code = ""

        return decoded_text

    def decompress(self, input_path):

        print("Decompression Initiated")
        filename, file_ext = os.path.splitext(input_path)
        output_path = filename.split("_")[0] + "_decompressed" + ".txt"
        reverse_mapping = {}

        # with open(decode_dictionary_path, 'r') as d:
        #     reverse_mapping = json.loads(d.read())
        #     reverse_mapping = {v: k for k, v in reverse_mapping.items()}
        #     print(reverse_mapping)

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:

            code_info_string = ""
            code_info = file.read(1)
            converted_code_info = ord(code_info)
            bits = bin(converted_code_info)[2:].rjust(8, "0")
            code_info_string += bits
            code_info = file.read(1)
            converted_code_info = ord(code_info)
            bits = bin(converted_code_info)[2:].rjust(8, "0")
            code_info_string += bits

            code_info = int(code_info_string, 2)

            mappings = file.read(code_info // 8)

            # print("mappings are: ")
            # print(mappings)

            reverse_mapping = json.loads(mappings.decode('UTF-8'))

            reverse_mapping = {v: k for k, v in reverse_mapping.items()}

            bit_string = ""

            byte = file.read(1)

            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, "0")
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)
            decoded_text = self.decode_text(encoded_text, reverse_mapping)

            output.write(decoded_text)
        print("Decompression Completed!")
        print(output_path)
