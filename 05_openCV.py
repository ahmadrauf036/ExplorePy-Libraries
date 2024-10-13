import cv2
img = cv2.imread('images.jpeg') #numpy array

# cv2.resizeWindow('image',100,200)
# B,G,R=cv2.split(img) 
# cv2.imshow('B',B)
# cv2.imshow('G',G)
# cv2.imshow('R',R)

# cv2.resize(img,100,200)

# grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #gray scale

# cv2.imshow('gray',grayImg)

crop=img[50:180,40:100]
cv2.imshow('image',img)
cv2.waitKey(0)

print(img.shape)