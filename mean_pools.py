import os
import sys
import cv2
import numpy as np

if __name__=="__main__":
    if(len(sys.argv)<2):
        print ("Usage :: python mean_pools.py <img_path> 3")
        sys.exit()    
    img_path = sys.argv[1]
    pool_size = int(sys.argv[2])
    
    img = cv2.imread(img_path,0)
    rows = img.shape[0]
    cols = img.shape[1]
    
    ro=int(rows/pool_size+1)
    co=int(cols/pool_size+1)
    pool_arr=[]

    for r in range(ro):
        r1=r*pool_size
        r2=min(r1+pool_size,rows+1)
        pool_col=[]
        for c in range(co):
            c1=c*pool_size
            c2=min(c1+pool_size,cols+1)
            print (r1,r2,c1,c2)
            m = int(np.mean(img[r1:r2,c1:c2]))
            pool_col.append(m) 
        pool_arr.append(pool_col)    
    res = np.array(pool_arr)
    cv2.imshow("mean_op",res)
    print ("size is ",res.shape,type(img),type(pool_arr),type(res))
    print ("original size::",img.shape)
    key = cv2.waitKey(5000)
    if(key==27): #exit on ESC key
        sys.exit()