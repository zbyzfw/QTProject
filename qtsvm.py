import os
import cv2
import skimage.color
import skimage.feature
import skimage.io
import skimage.transform


# 图片调整
def read_and_preprocess(im_path):
    # print(im_path)
    # MyMainWindow.printf(self,im_path)
    im = cv2.imread(im_path,0)
    # if len(im.shape) == 3:
    #     im = skimage.color.rgb2gray(im)
    # im = skimage.transform.resize(im, (128, 128))
    im = cv2.resize(im,(256,256))
    return im

def get_data_tr(train_path):
    X = []
    Y = []
    for entry in os.scandir(os.path.join(train_path,'cat/')):
        # print('========',entry)
        im = read_and_preprocess(entry.path)
        hf = skimage.feature.hog(im, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))
        X.append(hf)
        Y.append(0)
    for entry in os.scandir(os.path.join(train_path,'dog/')):
        im = read_and_preprocess(entry.path)
        hf = skimage.feature.hog(im, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))
        X.append(hf)
        Y.append(1)
    return X, Y

def get_data_te(test_path):
    X = []
    Y = []
    for entry in os.scandir(os.path.join(test_path,'cat/')):
        im = read_and_preprocess(entry.path)
        hf = skimage.feature.hog(im, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))
        X.append(hf)
        Y.append(0)
    for entry in os.scandir(os.path.join(test_path,'dog/')):
        im = read_and_preprocess(entry.path)
        hf = skimage.feature.hog(im, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))
        X.append(hf)
        Y.append(1)
    return X, Y

