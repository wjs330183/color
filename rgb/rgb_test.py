import cv2
import numpy as np

pic_file = './../3.jpg'
img = cv2.imread(pic_file)
b, g, r = cv2.split(img)

cv2.imshow('B', b)

cv2.imshow('G', g)

cv2.imshow('R', r)

# 合并三通道
change_image = cv2.merge([b, g, r])
cv2.imshow('images', change_image)
# 输出照片的种类，像素，尺寸
print(change_image.dtype, change_image.shape, change_image.size)
cv2.waitKey(0)
cv2.destroyAllWindows()
