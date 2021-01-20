from PyPDF2 import PdfFileReader, PdfFileWriter
import sys,os, subprocess

def rearrange(input, list, outfile):
    filename = input.split('\\')[-1].split('.')[0] + '.pdf'
    output = PdfFileWriter()
    input = PdfFileReader(open(input, "rb"))
    list = list.split(',')
    print(list)
    for i in list: 
        output.addPage(input.getPage(int(i) - 1))
    outputStream = open(outfile + '\\' + filename, 'wb')
    output.write(outputStream)
    outputStream.close()

rearrangelocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\App\\Rearrange'
print(rearrangelocation)

if (os.path.isfile(rearrangelocation) == True):
    if __name__ == "__main__":
        rearrange(sys.argv[1], sys.argv[2], rearrangelocation)
else:
    subprocess.call('mkdir ' + rearrangelocation, shell=True)
    if __name__ == "__main__":
        rearrange(sys.argv[1], sys.argv[2], rearrangelocation)
