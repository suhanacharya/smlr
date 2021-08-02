import os
from HuffmanCoding import HuffmanCoding
from rich import print
from rich.console import Console
from rich.table import Column, Table
from rich.progress import track
import time

h = HuffmanCoding()

if __name__ == "__main__":
    while True:

        print("HUFFMAN CODING")
        print("Menu: \n1. Compress\n2. Decompress\n3. Exit")
        choice = int(input())

        if choice == 1:
            print("Enter path of text file to be compressed: ")
            inp_path = input()
            original_file_size = os.path.getsize(inp_path)
            compressed_file_path = h.compress(inp_path)
            compressed_file_size = os.path.getsize(compressed_file_path)

            table = Table(show_lines=False)

            table.add_column("Compression Summary", style="black")
            table.add_column("Size", justify="right", style="green")

            table.add_row("Original File Size", str(
                original_file_size) + " b")
            table.add_row("Compressed File Size", str(
                compressed_file_size) + " b")
            table.add_row("Compression Ratio",
                          str(round(compressed_file_size / original_file_size, 6)))

            console = Console()
            console.print(table)

        elif choice == 2:
            print("Enter path of text file to be decompress: ")
            inp_path = input()
            h.decompress(inp_path)
        elif choice == 3:
            break
