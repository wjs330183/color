import cv2
import numpy as np

pic_file = './../2.jpg'
img_bgr = cv2.imread(pic_file, cv2.IMREAD_COLOR)
img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)

cv2.imshow("bgr", img_bgr)
cv2.imshow("yuv", img_yuv)

Y, U, V = cv2.split(img_yuv)
img_Y = cv2.inRange(Y, 130, 255)
Y_ret, Y_binary = cv2.threshold(img_Y, 200, 255, cv2.THRESH_BINARY)
Y_canny = cv2.Canny(Y_binary, 50, 150)
Y_edge = img_bgr.copy()
Y_lines = cv2.HoughLinesP(Y_canny, 1, np.pi / 180, 10, minLineLength=100, maxLineGap=50)
for line in Y_lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(Y_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("Y_ret", Y_ret)
cv2.imshow("Y_binary", Y_binary)
cv2.imshow("Y_canny", Y_canny)
cv2.imshow("Y_edge", Y_edge)


img_U = cv2.inRange(U, 130, 255)

U_ret, U_binary = cv2.threshold(img_U, 200, 255, cv2.THRESH_BINARY)
U_canny = cv2.Canny(U_binary, 50, 150)
U_edge = img_bgr.copy()
U_lines = cv2.HoughLinesP(U_canny, 1, np.pi / 180, 10, minLineLength=100, maxLineGap=50)
for line in U_lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(U_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)



cv2.imshow("U_ret", U_ret)
cv2.imshow("U_binary", U_binary)
cv2.imshow("U_canny", U_canny)
cv2.imshow("U_edge", U_edge)


img_V = cv2.inRange(V, 170, 255)
V_ret, V_binary = cv2.threshold(img_V, 200, 255, cv2.THRESH_BINARY)
V_canny = cv2.Canny(V_binary, 50, 150)
V_edge = img_bgr.copy()
V_lines = cv2.HoughLinesP(V_canny, 1, np.pi / 180, 10, minLineLength=100, maxLineGap=50)
if V_lines is not None:
    for line in V_lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(V_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("V_ret", V_ret)
cv2.imshow("V_binary", V_binary)
cv2.imshow("V_canny", V_canny)
cv2.imshow("V_edge", V_edge)

cv2.imshow("Y", img_Y)
cv2.imshow("U", img_U)
cv2.imshow("V", img_V)
cv2.waitKey(0)
