import sys,fitz
import cv2
import os

# code for scanning documents (converting pdf to png files for processing)
files=os.listdir('Docs')

for i in files:
    doc=None
    file='Docs//'+i
    try:
        doc=fitz.open(file)
    except Exception as e:
        print(e)
        if doc:
            doc.close()
            exit(0)
    os.mkdir('Scanned Docs//'+i+' scan')
    for j in range(0,doc.pageCount):
        page=doc[j]
        image_matrix=fitz.Matrix(fitz.Identity)
        pix=page.getPixmap(alpha=False, matrix=image_matrix)
        pix.writePNG('Scanned Docs//'+i+' scan//page{0}.png'.format(j+1))

    




