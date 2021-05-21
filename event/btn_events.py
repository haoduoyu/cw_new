import cv2
import threading
import time
import os
from aip import AipImageClassify
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap

_translate = QtCore.QCoreApplication.translate


class GlobalObj:
    target = None
    check_obj = '猫'  # 设置检测对象默认为猫
    need_monitor = False  # 是否需要监控
    image = None


def monitor_function(image):
    """
    通过全局变量is_monitor决定是否进行检测
    :return:
    """
    if not GlobalObj.need_monitor:
        return

    # 后面这几行不是很好，但是先这样吧
    image_name = './src_pic/%s.jpg' % time.time_ns()
    cv2.imwrite(image_name, image)

    image_bytes = open(image_name, 'rb').read()
    check_pic(image_bytes)


def check_pic(image):
    """
    调用百度接口识别图片信息
    :param image: 待识别的图片
    :return:
    """
    APP_ID = '23390095'
    API_KEY = '0KlDGMvrSTMI7vst9WBWGO7x'
    SECRET_KEY = 'jP3bSbS3yw0XgvbboXHRVD2Q0RX53XvZ'
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
    """ 调用通用物体识别 """
    client.advancedGeneral(image);
    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5
    """ 带参数调用通用物体识别 """
    lst = client.advancedGeneral(image, options)
    GlobalObj.target.infoTextBrowser.append(lst['result'][0]['keyword'] + '\n' + lst['result'][0]['baike_info']['description'])
    # return lst['result'][0]['keyword']


class BtnEvents:

    @staticmethod
    def open_camera_btn_event():
        """
        响应开启摄像头事件
        :return:
        """
        window_name = 'camera'
        cv2.namedWindow(window_name)
        cap = cv2.VideoCapture(0)

        i = 0
        while cap.isOpened():
            ok, frame = cap.read()
            if not ok:
                GlobalObj.target.infoTextBrowser.append("摄像头开启失败")
                break

            img = cv2.resize(frame, (270, 200), interpolation=cv2.INTER_AREA)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            label_image = QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
            GlobalObj.target.cameraLabel.setPixmap(QPixmap(label_image))
            GlobalObj.image = frame

            c = cv2.waitKey(100)

            if i % 3 == 0:
                monitor_function(frame)

            GlobalObj.target.infoTextBrowser.append("摄像头开启成功，按ESC退出")
            if c == 27:
                cv2.destroyAllWindows()
                GlobalObj.target.infoTextBrowser.append("退出摄像头成功")
                break

        cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def pet_kind_btn_event(select_value):
        """
        响应宠物类型事件
        :return:
        """
        GlobalObj.check_obj = select_value
        GlobalObj.target.infoTextBrowser.append("待检测动物为：%s" % select_value)

    @staticmethod
    def select_contract_btn_event():
        """
        响应选择联系人事件
        :return:
        """
        print('选择联系人')

    @staticmethod
    def open_monitor_btn_event():
        """
        响应开启实时监控事件
        :return:
        """
        print('开启实时监控')

        if '开启' in GlobalObj.target.openMonitorBtn.text():
            display_text = '关闭实时监控'
        else:
            display_text = '开启实时监控'

        GlobalObj.target.openMonitorBtn.setText(_translate('MainWindow', display_text))
        GlobalObj.need_monitor = not GlobalObj.need_monitor

    @staticmethod
    def analyse_pic_btn_event():
        """
        响应分析图片事件
        :return:
        """
        print('分析图片')

    @staticmethod
    def test_info_btn_event():
        """
        响应测试信息事件
        :return:
        """
        print('测试信息')

    @staticmethod
    def personal_info_btn_event():
        """
        响应个人信息事件
        :return:
        """
        print('个人事件')
