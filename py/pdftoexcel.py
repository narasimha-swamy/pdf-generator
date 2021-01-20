from tabula import read_pdf,convert_into
import os
import sys
import subprocess

def pdftoexcel(input, output):
    # df = read_pdf(input, pages='all')
    filename = input.split('\\')[-1].split('.')[0] + '.csv'
    convert_into(input, output + '\\' + filename, output_format="csv", pages='all')

excellocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\App\\ExcelFiles'

if (os.path.isfile(excellocation) == True):
    if __name__ == "__main__":
        pdftoexcel(sys.argv[1], excellocation)
else:
    subprocess.call('mkdir ' + excellocation, shell=True)
    if __name__ == "__main__":
        pdftoexcel(sys.argv[1], excellocation)

