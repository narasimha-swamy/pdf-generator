import ocrmypdf
import sys
import os
import subprocess

def ocrconverter(input, output):
    filename = input.split('\\')[-1].split('.')[0] + '.pdf'
    ocrmypdf.ocr(input,output + '\\' + filename)

ocrlocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\App\\OCRFiles'

if (os.path.isfile(ocrlocation) == True):
    if __name__ == "__main__":
        ocrconverter(sys.argv[1], ocrlocation)
else:
    subprocess.call('mkdir ' + ocrlocation, shell=True)
    print('hello')
    if __name__ == "__main__":
        ocrconverter(sys.argv[1], ocrlocation)

