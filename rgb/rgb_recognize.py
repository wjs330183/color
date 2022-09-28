import cv2
import numpy as np

pic_file = './../2.jpg'

img = cv2.imread(pic_file)
b_img, g_img, r_img = cv2.split(img)
cv2.imshow('B', b_img)

cv2.imshow('G', g_img)

cv2.imshow('R', r_img)
b_ret, b_binary = cv2.threshold(b_img, 200, 255, cv2.THRESH_BINARY)
b_canny = cv2.Canny(b_binary, 50, 150)
b_edge = img.copy()
b_lines = cv2.HoughLinesP(b_canny, 1, np.pi / 180, 10, minLineLength=100, maxLineGap=50)
for line in b_lines:
    x1, y1, x2, y2 = line[0]
    if abs(y1 - y2) < 20:
        cv2.line(b_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("b_ret", b_ret)
cv2.imshow("b_binary", b_binary)
cv2.imshow("b_canny", b_canny)
cv2.imshow("b_edge", b_edge)

g_ret, g_binary = cv2.threshold(g_img, 200, 255, cv2.THRESH_BINARY)
g_canny = cv2.Canny(g_binary, 50, 150)
g_edge = img.copy()
g_lines = cv2.HoughLinesP(g_canny, 1, np.pi / 180, 10, minLineLength=100, maxLineGap=50)
if g_lines is not None:
    for line in g_lines:
        x1, y1, x2, y2 = line[0]
        if abs(y1 - y2) < 20:
            cv2.line(g_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("g_ret", g_ret)
cv2.imshow("g_binary", g_binary)
cv2.imshow("g_canny", g_canny)
cv2.imshow("g_edge", g_edge)

r_ret, r_binary = cv2.threshold(r_img, 200, 255, cv2.THRESH_BINARY)
r_canny = cv2.Canny(r_binary, 50, 150)
r_edge = img.copy()
r_lines = cv2.HoughLinesP(r_canny, 1, np.pi / 180, 10, minLineLength=100, maxLineGap=50)
for line in r_lines:
    x1, y1, x2, y2 = line[0]
    if abs(y1 - y2) < 20:
        cv2.line(r_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("r_ret", r_ret)
cv2.imshow("r_binary", r_binary)
cv2.imshow("r_canny", r_canny)
cv2.imshow("r_edge", r_edge)

cv2.waitKey(0)
