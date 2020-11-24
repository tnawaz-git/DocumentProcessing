import cv2
import matplotlib.pyplot as plt
import numpy as np

file=r'test3.png'
table_image_contour=cv2.imread(file,0)
table_image=cv2.imread(file)


ret,thresh_value=cv2.threshold(table_image_contour, 180, 255, cv2.THRESH_BINARY_INV)

kernel=np.ones((5,5),np.uint8)
dilated_value=cv2.dilate(thresh_value, kernel, iterations=4)

contours, hierachy= cv2.findContours(dilated_value, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    # bounding the images
    if y < 300:
        table_image = cv2.rectangle(table_image, (x, y), (x + w, y + h), (0, 0, 255), 1)

plt.imshow(table_image)
plt.show()
cv2.namedWindow('detecttable', cv2.WINDOW_NORMAL)