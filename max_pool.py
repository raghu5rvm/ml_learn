import os
import cv2
import sys
import numpy as np

def find_mean(a,n,m):
	s = sum(map(sum, stride))
	return int(s/(n*m))
	

if __name__=="__main__":
    if(len(sys.argv)<2):
        print ("Usage :: python max_pool.py <img_path> 3")
        sys.exit()    
    img_path = sys.argv[1]
    pool_size = int(sys.argv[2])
    
    img = cv2.imread(img_path,0)
    rows = img.shape[0]
    cols = img.shape[1]
    
    o_rows = int(rows/pool_size)
    o_cols = int(cols/pool_size)
    result = [[0]*(o_rows+2)]*(o_cols+2)
    print ("o_rows, o_cols",o_rows,o_cols)
    p=0
    i=0
    row_result = []
    while(i < rows):
        i2 = i + pool_size
        i2 = min(i2,rows)
        j = 0
        q = 0
        col_result = []
        while( j < cols):
            j2 = j + pool_size
            j2 = min(j2,cols)
            print ("take stride",i,i2,j,j2)
            stride = img[i:i2,j:j2,]
            print (stride)
            val = max(map(max, stride))
            print ("val is ",val)
            j = j + pool_size
            q += 1
            col_result.append(val)
        p += 1
        i += pool_size
        print ("p",p,"q is",q)
        row_result.append(col_result)
    cv2.imwrite("/home/ubuntu/Desktop/some.jpg",np.array(result))
    result = np.array(row_result)
    cv2.imshow("output",result)
    print ("size is ",result.shape)
    print (result)
    key = cv2.waitKey(10000)
    if(key==27): #exit on ESC key
        sys.exit()
