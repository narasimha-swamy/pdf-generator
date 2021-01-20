from docx2pdf import convert
import os
import sys
import subprocess

def wordtopdf(input, output):
    filename = input.split('\\')[-1].split('.')[0]
    # print(filename)
    convert(input, output + '\\' + filename + '.pdf') 

pdflocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\App\\PDFfiles'

if (os.path.isfile(pdflocation) == True):
    if __name__ == "__main__":
        wordtopdf(sys.argv[1], pdflocation)
else:
    subprocess.call('mkdir ' + pdflocation, shell=True)
    if __name__ == "__main__":
        wordtopdf(sys.argv[1], pdflocation)

# subprocess.call('mkdir ' + pdflocation, shell=True)