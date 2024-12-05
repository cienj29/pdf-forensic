#!/usr/bin/env python3

import argparse
from PyPDF2 import PdfReader

def banner():
	print ('##########################################')
	print ('##                                      ##')
	print ('##      Author: Sazzad Ovi              ##')
	print ('##                                      ##')
	print ('##           XOVIM001                   ##')
	print ('##                                      ##')
	print ('##                                      ##')
	print ('##########################################')

banner()

# Function to start metadata extraction
def printMeta(filename):
	try:
		pdfFile = PdfFileReader(open(filename, 'rb'))
		docInfo = pdfFile.metadata
		
		print(f'[*] PDF MetaData for: {filename}')
		if docInfo:
			for metaItem, value in docInfo.items():
				print(f'[+] {metaItem}: {value}')
		else:
			print('[!] No metadata found in this PDF.')	
	except FileNotFoundError:
		print(f"Error: File '{filename}' is not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

def main():
	parser = argparse.ArgumentParser(description='Usage program: -F <PDF file name>')
	parser.add_argument('-F', dest='fileName', type=str, help='Please specify the PDF File name')
	args = parser.parse_args()
	fileName = args.fileName
	if not fileName:
		print(parser.print_help())
		exit(0)
	else:
		printMeta(fileName)
if __name__ == '__main__':
	main()
