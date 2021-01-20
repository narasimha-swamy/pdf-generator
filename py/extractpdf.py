from PyPDF2 import PdfFileReader, PdfFileWriter
import sys,os, subprocess

def extract(input, pageno, outfile):
    filename = input.split('\\')[-1].split('.')[0] + '.pdf'
    output = PdfFileWriter()
    input = PdfFileReader(open(input, "rb"))
    output.addPage(input.getPage(int(pageno)))
    outputStream = open(outfile + '\\' + filename, 'wb')
    output.write(outputStream)
    outputStream.close()

extractfilelocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\App\\Extractfile'
# print(extractfilelocation)

if (os.path.isfile(extractfilelocation) == True):
    if __name__ == "__main__":
        extract(sys.argv[1], sys.argv[2], extractfilelocation)
else:
    subprocess.call('mkdir ' + extractfilelocation, shell=True)
    if __name__ == "__main__":
        extract(sys.argv[1], sys.argv[2], extractfilelocation)
