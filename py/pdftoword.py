import win32com.client
import os
import sys
import subprocess

path = os.path.dirname(os.path.abspath(__file__))

def pdftoword(input, output):
    filename = input.split('\\')[-1].split('.')[0] + '.docx'
    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0
    pdfdoc = input
    todocx = output + '\\' + filename
    wb1 = word.Documents.Open(pdfdoc)
    wb1.SaveAs(todocx, FileFormat=16) 
    wb1.Close()
    word.Quit()

wordlocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\App\\WordFiles'

if (os.path.isfile(wordlocation) == True):
    if __name__ == "__main__":
        pdftoword(sys.argv[1], wordlocation)
else:
    subprocess.call('mkdir ' + wordlocation, shell=True)
    print('hello')
    if __name__ == "__main__":
        pdftoword(sys.argv[1], wordlocation)

