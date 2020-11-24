import cv2
import numpy as np

# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('img_0.tiff')
processed=image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Create rectangular structuring element and dilate
#kernel=np.ones((5,5),np.uint8)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.dilate(thresh, kernel, iterations=6)

# Find contours and draw rectangle
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

rects=[]
paras=[]

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    rects.append((x,y,w,h))

#paragraph extraction

sf1=0.75
sf2=0.05

for box in rects:
    if box[2]>image.shape[1]*sf1 and box[3]>image.shape[0]*sf2:
        paras.append(box)

for para in paras:
    x=para[0]
    y=para[1]
    w=para[2]
    h=para[3]
    cv2.rectangle(processed, (x, y), (x + w, y + h), (36,255,12), 2)

#analysis 

print("Boundaries: ", rects)
print("Paragraphs: ", paras)
print("Resolution", image.shape)

dilateR=cv2.resize(dilate,(610,800))
imageR=cv2.resize(image,(610,800))
processedR=cv2.resize(processed,(610,800))

cv2.imshow('dilate', dilateR)
cv2.imshow('image', imageR)
cv2.imshow('paragraphs',processedR)
cv2.waitKey()