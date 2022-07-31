# 霍夫变化及svm向量机包
import joblib
import skimage.feature
import cv2

clf = joblib.load("train_model.m")
roi = cv2.imread('image/02.jpg')
roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
svm_roi = cv2.resize(roi, (256, 256))
v,hf = skimage.feature.hog(svm_roi, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1),visualize=True)
# 预测结果 0为存在电表1为不存在
print(hf.shape)
# svm_result = clf.predict(hf)
cv2.imshow('hog',hf)
cv2.waitKey(0)
# print(v,svm_result)