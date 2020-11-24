import pickle,numpy
import sys

with open('res_1.bin', 'rb') as f:
    data = pickle.load(f)
    #print(data) 
rects=[]
rects_pos=[]

for z in data:
    rects.append(z[0])

for x in rects:
    rects_pos.append([x[0],x[1]])

print(rects_pos)

###########


