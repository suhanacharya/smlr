# SMLR

## Abstract


## Purpose
The main purpose of this project is to compress the text files into binary file in order to reduce the file size.  Usually data which are fetched from the backend server can be of large size.  These data should be compressed to smaller size to reduce the time required to fetch the data from server and also the time required to format the data to be received by the client and to be displayed in the client’s computer system.

## Scope
In the real world scenario, when the files are fetched from the server the files which the  user  receives  will  be  compressed  using  qzip  technique.   Gzip  is  based  on  theDEFLATE  algorithm,  which  is  a  combination  of  LZ77  and  Huffman  coding.   This application provides the information regarding file, like it’s actual size of the file and the size of the file after compression.  It displays he compression ratio along with the real time progress of the compression process and estimated time for the completion of the process.

## Overview
Since everyone is dependent on internet for day to day activities these days, the time required  to  transfer  data  through  the  network  should  be  as  minimum  as  possible.Trivial task should be performed with lesser time and important task should be give higher priority.  This will create a balance in the network traffic.  This application usesHuffman text data compression encoding, to compress text file into binary file.  With the help of tree and heap data structures, we are creating nodes which will be used to compare and generate the binary output file.  This file is compressed to a smaller sized binary file.

## How to run
If python isn't installed on your machine then do [install](https://www.python.org/downloads/). Once installed run teh following command.

```
python main.py
```
or 
```
python3 main.py
```