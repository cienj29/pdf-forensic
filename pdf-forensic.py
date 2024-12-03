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
	parser = oargparse.ArgumentParser('usage program: -F <PDF file name>')
	parser.add_option('-F', dest='fileName', type='string',\
		help='Please specify the PDF File name')
	(options, args) = parser.parse_args()
	fileName = options.fileName
	if fileName == None:
		print(parser.usage)
		exit(0)
	else:
		printMeta(fileName)
if __name__ == '__main__':
	main()
