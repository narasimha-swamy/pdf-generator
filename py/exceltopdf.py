import pandas as pd
import pdfkit
import os
import subprocess
import sys

pdflocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\App\\PDFFiles'

def exceltopdf(input, output):
    filename = input.split('\\')[-1].split('.')[0] + '.pdf'
    df = pd.read_excel(input)#input
    df.to_html("input.html")#to html
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file("input.html", output + '\\' + filename, configuration=config)#to pdf


if (os.path.isfile(pdflocation) == True):
    if __name__ == "__main__":
        exceltopdf(sys.argv[1], pdflocation)
else:
    subprocess.call('mkdir ' + pdflocation, shell=True)
    print('hello')
    if __name__ == "__main__":
        exceltopdf(sys.argv[1], pdflocation)
