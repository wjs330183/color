import cv2
import numpy as np

pic_file = './../colors.jpeg'
img = cv2.imread(pic_file, cv2.IMREAD_COLOR)

b, g, r = cv2.split(img)

whiteLower = np.array([150, 150, 150])
whiteUpper = np.array([255, 255, 255])
white_mask = cv2.inRange(img, whiteLower, whiteUpper)
cv2.imshow('white_mask', white_mask)



blueLower = np.array([255, 0, 0])
blueUpper = np.array([255, 255, 200])
blue_mask = cv2.inRange(img, blueLower, blueUpper)
cv2.imshow('blue_mask', blue_mask)


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
