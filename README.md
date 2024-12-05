# pdf-forensic

Overview
=========
pdf-forensic is a PDF file investigation tool which extract the MetaData from the pdf file and print it on the screen. From the MetaData, it is possible to find out the author's name of the pdf file, modification date, creation date, what technology used to create the file and many more. It's a great tool focused on forensic investigation. This forensic investigation was proved useful in the arrest of a member of the hacker group Anonymous in 2010.

Requirements
============
1. Python 2.7
2. Before run the tool, please install the PyPDF2 module along with python. To do that please follow the command:
'pip install PyPDF2'

[2024 UPDATE] Install latest version of PyPDF2 when prompted/ when using Python Version 3.13.0

Compatibility:
============
Tested on Python 2.7 installed windows and Linux OS.

[2024 UPDATE] Tested on Python 3.13.0 on Mac OS. Ensure usage of Python 3.13.0 for compatability with updated libraries.

Usage
=====
Navigate to the file folder and run the following command:

python pdf-forensic.py -F <File Name>

[2024 UPDATE] Download .py file and open terminal. Run command: 
python3 pdf-forensic.py -F /your/path/to/FileName.pdf

Examples
========
python pdf-forensic.py -F test.pdf

[2024 UPDATE] python3 pdf-forensic.py -F /User/yourname/Downloads/TEST.pdf

Bugs & Contact
==============
Feel free to mail me with any problem, bug, suggestions or fixes at:
Sazzad Ovi <ovisecret@gmail.com>
