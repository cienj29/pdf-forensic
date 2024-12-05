#!/usr/bin/env python
import PyPDF2
import argparse
from PyPDF2 import PdfFileReader

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

def printMeta(filename):
	pdfFile = PdfFileReader(open(filename, 'rb'))
	docInfo = pdfFile.getDocumentInfo()
	print('[*] PDF MetaData for: ' + str(filename))
	for metaItem in docInfo:
		print('[+] ' + metaItem + ': ' + docInfo[metaItem])

def main():
	parser = argparse.ArgumentParser(description='Usage program: -F <PDF file name>')
	parser.add_argument('-F', dest='fileName', type='str', help='Please specify the PDF File name')
	args = parser.parse_args()
	fileName = args.fileName
	if not fileName:
		print(parser.print_help())
		exit(0)
	else:
		printMeta(fileName)
if __name__ == '__main__':
	main()
