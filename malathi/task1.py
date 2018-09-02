import cv2
image=imread("1.jpg",0)
print(image)
arr=[[1,2,3],[5,6,7],[9,10,11]];
rows=len(arr)
columns=len(arr[0])
k=2
test = [[]*1 for i in range(0,rows-k+1)]
max=arr[0][0]
for m in range(0,rows-k+1):
    for n in range(0,columns-k+1):
        for i in range(m,k+m):
            for j in range(n,k+n):
                if arr[i][j]>max:
                    max=arr[i][j]
        test[m].append(max)
print(test)
