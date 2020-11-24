import sys,fitz
import cv2
import os

doc=None
file='Docs/doc1.pdf'
try:
    doc=fitz.open(file)
except Exception as e:
    print(e)
    if doc:
        doc.close()
        exit(0)

page=doc[1]
image_matrix=fitz.Matrix(fitz.Identity)
pix=page.getPixmap(alpha=False, matrix=image_matrix) 
#pix.writePNG('result.png')
#print(page.getText("text"))
