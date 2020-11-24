import pickle
import cv2
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
import numpy
import sys
import fitz
import os
import re 

# code for showing the text boundaries extracted by Tesseract on scanned documents

files=os.listdir('Scanned Docs')
for z in range(len(files)):
    files[z] = files[z].split()

file_names=numpy.array(files)[:, 0]

for i in file_names:
    file='Docs/'+i
    doc=fitz.open(file)

    os.mkdir('Output_Tesseract/'+re.split("\.",i)[0]+' bounds')

    for j in range(0,doc.pageCount):

        file=open('C:/faxes_recognition_pipeline/analysis_out/ocr_'+re.split("\.",i)[0]+'/res_'+str(j)+'.bin','rb')
        rec=pickle.load(file)
        xyz=numpy.array(rec)
        file.close()

        # Display the image
        imgg=Image.open('C:\\faxes_recognition_pipeline\\analysis_out\\scan_'+re.split("\.",i)[0]+'\\img_{0}.png'.format(j))
        plt.imshow(imgg)
        

        for z in range(0,xyz.shape[0]):
            # Add the patch to the Axes
            plt.gca().add_patch(Rectangle((xyz[z,0][0],xyz[z,0][1]),xyz[z,0][2],xyz[z,0][3],linewidth=1,edgecolor='r',facecolor='none'))
        
        manager=plt.get_current_fig_manager()
        manager.window.showMaximized()
        
        plt.savefig('Output_Tesseract/'+re.split("\.",i)[0]+' bounds/pageout{0}.svg'.format(j+1),format='svg',dpi=1200)
        plt.show(block=False)
        plt.pause(2)
        plt.close()
        
    doc.close()