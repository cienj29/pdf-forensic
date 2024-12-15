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

#Save metadata to text file
def save_metadata_to_text(filename, metadata):
	output_file = f"{filename}_metadata.txt"
	try:
		with open(output_file, 'w') as f:
			f.write(f"Metadata for {filename}:\n\n")
			if metadata:
				for key, value in metadata.items():
					f.write(f"{key}: {value}\n")
			else:
				f.write("No metadata found.")
		print(f"[+] Metadata saved to {output_file}")
	except Exception as e:
		print(f"[!] Error saving metadata to text file: {e}")

# Function to start metadata extraction
def printMeta(filename):
	try:
		pdfFile = PdfReader(filename)
		docInfo = pdfFile.metadata
		
		print(f'[*] PDF MetaData for: {filename}')
		if docInfo:
			for metaItem, value in docInfo.items():
				print(f'[+] {metaItem}: {value}')
		#Save metadata to text file
			save_metadata_to_text(filename, docInfo)
		else:
			print('[!] No metadata found in this PDF.')
			save_metadata_to_text(filename, None)
	except FileNotFoundError:
		print(f"Error: File '{filename}' is not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

#Main function to parse arguments
def main():
	parser = argparse.ArgumentParser(description='Usage program: -F <PDF file name>')
	parser.add_argument('-F', dest='fileName', type=str, help='Please specify the PDF File name')
	args = parser.parse_args()
	fileName = args.fileName
	if not fileName:
		parser.print_help()
		exit(0)
	else:
		printMeta(fileName)
if __name__ == '__main__':
	main()
