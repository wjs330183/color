# gamma变换
import cv2
import numpy as np

# 创建用于显示gamma的窗口和调节参数的bar
cv2.namedWindow("de")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 600, 0)

# 创建用于显示gamma的窗口和调节参数的bar
cv2.namedWindow("config", cv2.WINDOW_NORMAL)
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 600, 0)

cv2.createTrackbar("gamma", "config", 0, 10, lambda x: None)
cv2.createTrackbar("gain", "config", 0, 10, lambda x: None)
cv2.createTrackbar("scale", "config", 0, 255, lambda x: None)

image_path = './1.jpg'
img = cv2.imread(image_path)

gamma = cv2.getTrackbarPos("gamma", "config")
gain = cv2.getTrackbarPos("gain", "config")
scale = cv2.getTrackbarPos("scale", "config")

gamma, gain, scale = 0.7, 1, 255
gamma_img = np.zeros_like(img)
for i in range(3):
    gamma_img[:, :, i] = ((img[:, :, i] / scale) ** gamma) * scale * gain
cv2.imshow('img', img)
cv2.imshow('gamma_img', gamma_img)
cv2.waitKey(0)
