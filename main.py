# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox,QFileDialog
import sys, os
import cv2 as cv
import traceback
import cgitb

# from sklearn.svm import SVC
from boxui import Ui_MainWindow  # 导入 uiDemo4.py 中的 Ui_MainWindow 界面类
# from qtsvm import get_data_tr, get_data_te
# import skimage.feature
from tools.infer.predict import detect_roi

# 彩色图像转换
def cv2qt(img):
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_dis = QImage(rgb_img, rgb_img.shape[1], rgb_img.shape[0], QImage.Format_RGB888)
    print(rgb_img.shape[2],rgb_img.shape[1], rgb_img.shape[0])
    # img_dis = QPixmap(img_dis).scaled(rgb_img.shape[1] / 6, rgb_img.shape[0] / 6)
    return QPixmap(img_dis)

# 灰度图像转换
def cv2qtdim2(img):
    # rgb_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blue = img
    # blue = cv.split(rgb_img)[0]  ##得到图像蓝色通道灰度图
    # img_dis = QImage(rgb_img, rgb_img.shape[1], rgb_img.shape[0], QImage.Format_RGB888)
    img_dis = QImage(blue, blue.shape[1], blue.shape[0], blue.shape[1], QImage.Format_Grayscale16)
    print(blue.shape[1], blue.shape[0])
    # img_dis = QPixmap(img_dis).scaled(rgb_img.shape[1] / 6, rgb_img.shape[0] / 6)
    return QPixmap(img_dis)

class MyMainWindow(QMainWindow, Ui_MainWindow):  # 继承 QMainWindow类和 Ui_MainWindow界面类
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类
        # self.treeWidget.itemClicked.connect(self.click_treeWidget)  # 点击 treeWidget 触发
        self.btn_openFile.clicked.connect(self.openFile)
        self.btn_openFile_2.clicked.connect(self.openFile2)
        # self.pushButton_2.clicked.connect(self.openImg)
        self.btn_train.clicked.connect(self.train)
        self.btn_test.clicked.connect(self.test)
        self.pushButton_9.clicked.connect(self.img_hog)
        self.img = None

    def decorator(self,fun):
        def warp(*args, **kwargs):
            try:
                ret = fun(*args, **kwargs)
            except Exception as e:
                self.printf(e)
            # print(f"计算结果是:{ret}")  # 新功能,打印计算的结果
            return ret

        return warp

    def catch_exceptions(self, ty, value, traceback):
        """
        捕获异常，并弹窗显示
        :param ty: 异常的类型
        :param value: 异常的对象
        :param traceback: 异常的traceback
        """
        traceback_format = traceback.format_exception(ty, value, traceback)
        traceback_string = "".join(traceback_format)
        print(traceback_string,traceback_format)
        # QMessageBox.critical(self, "An exception was raised", "{}".format(traceback_string))
        self.old_hook(ty, value, traceback)

    '''打开文件'''
    def openFile(self):
        # 其中self指向自身，"读取文件夹"为标题名，"./"为打开时候的当前路径
        directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")  # 起始路径
        self.lineEdit.setText(directory1)

    def openFile2(self):
        # 其中self指向自身，"读取文件夹"为标题名，"./"为打开时候的当前路径
        directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")  # 起始路径
        # print(directory1)
        self.lineEdit_2.setText(directory1)

    def train(self):
        # 训练
        print(self.lineEdit.text())
        # Xtr, Ytr = get_data_tr(self.lineEdit.text())
        # clf = SVC(probability=True)
        # clf.fit(Xtr, Ytr)
        # joblib.dump(clf, "train_model.m")
        self.printf(f'训练成功,模型保存在{os.getcwd()}/train_model.m')

    def test(self):
        # Xte, Yte = get_data_te(self.lineEdit_2.text())
        # clf = joblib.load("train_model.m")
        # r = clf.predict(Xte)
        # s = 0
        # for i in range(len(r)):
        #     if r[i] == Yte[i]:
        #         s += 1
        # self.printf(f'测试模型准确率为: {s / len(r)}')
        self.printf(f'测试模型准确率为: aaa')

    def printf(self, mes):
        self.textBrowser.append(mes)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

    def click_pushButton_2(self):  # 点击 pushButton_2 触发
        self.lineEdit_2.setText("click_pushButton_2")
        return

    def click_pushButton_1(self):  # 点击 pushButton_1 触发
        # self.textEdit.append("当前动作：click_pushButton_1")

        self.textEdit.append("选择堆叠布局页面：page_0")
        img = QFileDialog.getOpenFileName(self, "选取文件", "./")  # 起始路径
        print(img)
        self.printf(f"选择图片：{img[0]}")
        self.stackedWidget.setCurrentIndex(0)  # 打开 stackedWidget > page_0
        self.img = cv.imread(img[0])
        # self.img = cv.resize(self.img, (550, 300))
        self.label.setPixmap(cv2qt(self.img))
        return

    def img_hog(self):
        # 灰度变换
        # if len(self.img.shape) == 3:
        #     gray = cv.resize(cv.cvtColor(self.img, cv.COLOR_BGR2GRAY),(256, 256))
        # else:
        #     gray = cv.resize(self.img, (256, 256))
        # 每个滑动窗口的pixels_per_cell = [像素宽度，像素高度], cell_per_block = [宽度，高度】
        # normalised_blocks,hf = skimage.feature.hog(gray, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1),visualize=True)
        # print(hf.shape)
        results = detect_roi(self.img,True)
        print(results)
        myWin.printf(str(results))
        imgShow = QPixmap('inference_results/' + 'output.jpg')
        self.label.setPixmap(imgShow)
        # cv.imshow('hog', hf)
        # cv.waitKey(5)

    def click_pushButton_4(self):  # 点击 pushButton_1 触发
        self.textEdit.append("当前动作：click_pushButton_1")
        self.textEdit.append("选择堆叠布局页面：page_0")
        self.stackedWidget.setCurrentIndex(2)  # 打开 stackedWidget > page_0
        # self.label.setPixmap(cv2qt(cv.imread("image/img.png")))
        return

    def click_treeWidget(self, item, column):  # 点击 treeWidget 触发
        # item = self.treeWidget.currentItem()  # 获得当前项 Item
        # if item != None:  # 根据 item 选择执行其它操作

        print('key = {}\tvalue = {}'.format(item.text(0), item.text(1)))
        self.plainTextEdit.appendPlainText("Click: treeWidget")
        self.plainTextEdit.appendPlainText("  key ：{}".format(item.text(0)))

    def click_pushButton_3(self):  # 点击 pushButton_3 触发
        self.textEdit.append("当前动作：click_pushButton_1")
        self.textEdit.append("选择堆叠布局页面：page_0")
        self.stackedWidget.setCurrentIndex(1)  # 打开 stackedWidget > page_0
        # self.label.setPixmap(cv2qt(cv.imread("image/img.png")))
        return

    def trigger_actHelp(self):  # 动作 actHelp 触发
        QMessageBox.about(self, "About",
                          """数字图像处理工具箱 v1.0\nCopyright YouCans, XUPT 2021""")
        return

if __name__ == '__main__':
    cgitb.enable(format='text')
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口
    try:
        myWin.show()  # 在桌面显示控件 myWin
    except Exception as e:
        print(e)
        myWin.printf(e)

    sys.exit(app.exec_())  # 结束进程，退出程序

