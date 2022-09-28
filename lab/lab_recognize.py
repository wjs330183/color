import numpy as np
import cv2
import matplotlib.pyplot as plt

# 读取图片
pic_file = './../3.jpg'
img_bgr = cv2.imread(pic_file, cv2.IMREAD_COLOR)
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
cv2.namedWindow("input", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("input", img_lab)

# 分别获取三个通道的ndarray数据
img_ls = img_lab[:, :, 0]
ls_ret, ls_binary = cv2.threshold(img_ls, 200, 255, cv2.THRESH_BINARY)
ls_canny = cv2.Canny(ls_binary, 50, 150)
ls_edge = img_bgr.copy()
ls_lines = cv2.HoughLinesP(ls_canny, 1, np.pi / 180, 10, minLineLength=50, maxLineGap=50)
for line in ls_lines:
    x1, y1, x2, y2 = line[0]
    if abs(y1 - y2) < 20:
        cv2.line(ls_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("ls_ret", ls_ret)
cv2.imshow("ls_binary", ls_binary)
cv2.imshow("ls_canny", ls_canny)
cv2.imshow("ls_edge", ls_edge)


img_as = img_lab[:, :, 1]

as_ret, as_binary = cv2.threshold(img_as, 240, 255, cv2.THRESH_BINARY)
as_canny = cv2.Canny(as_binary, 50, 150)
as_edge = img_bgr.copy()
as_lines = cv2.HoughLinesP(as_canny, 1, np.pi / 180, 10, minLineLength=50, maxLineGap=50)
if as_lines is not None:
    for line in as_lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(as_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("as_ret", as_ret)
cv2.imshow("as_binary", as_binary)
cv2.imshow("as_canny", as_canny)
cv2.imshow("as_edge", as_edge)


img_bs = img_lab[:, :, 2]

bs_ret, bs_binary = cv2.threshold(img_bs, 100, 255, cv2.THRESH_BINARY)
bs_canny = cv2.Canny(bs_binary, 50, 150)
bs_edge = img_bgr.copy()
bs_lines = cv2.HoughLinesP(bs_canny, 1, np.pi / 180, 10, minLineLength=50, maxLineGap=50)
if bs_lines is not None:
    for line in bs_lines:
        x1, y1, x2, y2 = line[0]
        if abs(y1 - y2) < 20:
            cv2.line(bs_edge, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("bs_ret", bs_ret)
cv2.imshow("bs_binary", bs_binary)
cv2.imshow("bs_canny", bs_canny)
cv2.imshow("bs_edge", bs_edge)


cv2.imshow("img_ls", img_ls)
cv2.imshow("img_as", img_as)
cv2.imshow("img_bs", img_bs)
cv2.waitKey(0)




#
# '''按L、A、B三个通道分别计算颜色直方图'''
# ls_hist = cv2.calcHist([img_lab], [0], None, [256], [0, 255])
# as_hist = cv2.calcHist([img_lab], [1], None, [256], [0, 255])
# bs_hist = cv2.calcHist([img_lab], [2], None, [256], [0, 255])
# # m,dev = cv2.meanStdDev(img_lab)  #计算L、A、B三通道的均值和方差
# # print(m)
#
# '''显示三个通道的颜色直方图'''
# plt.plot(ls_hist, label='l', color='blue')
# plt.plot(as_hist, label='a', color='green')
# plt.plot(bs_hist, label='b', color='red')
# plt.legend(loc='best')
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)
