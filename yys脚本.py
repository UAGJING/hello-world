from __future__ import print_function, division
import os
import sys
import time
import numpy as np
import math
import random
from PIL import Image
from six.moves import input
import matplotlib.pyplot as plt

#获取截屏
def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png .')
    fig = plt.figure()
    # im = Image.open('./autojump.png')
    img = np.array(Image.open('autojump.png'))
    im = plt.imshow(img, animated=True)  # 显示图片
    # print(im.size)
    plt.show()

#点击挑战按钮
def challenge_key():
    #产生随机数
    y_randon=int(random.uniform(700, 785))
    x_randon=int(random.uniform(1331, 1520))
    time =int(random.uniform(50, 150))
    print(y_randon,x_randon,time)

    #长按time毫秒
    #cmd ='adb shell input tap {x1} {y1} '.format(x1=y_randon,y1=x_randon) #点击
    #cmd = 'adb shell input swipe 320 410 320 410 3000'
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
            x1=x_randon,
            y1=y_randon,
            x2=x_randon,
            y2=y_randon,
            duration=time
        )
    #print(cmd)
    os.system(cmd)

def anjian2():
    #产生随机数
    y_randon=int(random.uniform(60, 470))
    x_randon=int(random.uniform(20, 1880))
    time =int(random.uniform(60, 180))
    print(y_randon,x_randon,time)

    #长按time毫秒
    #cmd ='adb shell input tap {x1} {y1} '.format(x1=y_randon,y1=x_randon) #点击
    #cmd = 'adb shell input swipe 320 410 320 410 3000'
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
            x1=x_randon,
            y1=y_randon,
            x2=x_randon,
            y2=y_randon,
            duration=time
        )
    #print(cmd)
    os.system(cmd)

def anjian3():
    #产生随机数
    y_randon=int(random.uniform(600, 1000))
    x_randon=int(random.uniform(50, 1850))
    time =int(random.uniform(80, 200))
    print(y_randon,x_randon,time)

    #长按time毫秒
    #cmd ='adb shell input tap {x1} {y1} '.format(x1=y_randon,y1=x_randon) #点击
    #cmd = 'adb shell input swipe 320 410 320 410 3000'21
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
            x1=x_randon,
            y1=y_randon,
            x2=x_randon,
            y2=y_randon,
            duration=time
        )
    #print(cmd)
    os.system(cmd)
#延时函数
def sleep(mytime):
    time.sleep(mytime)

'''
fig = plt.figure()
pull_screenshot()
#im = Image.open('./autojump.png')
img = np.array(Image.open('autojump.png'))
im = plt.imshow(img, animated=True)  #显示图片
#print(im.size)
plt.show()
'''
def main():# 循环加 while True:  循环最后最好加几秒延时
    while True:
        challenge_key()
        print("start...")
        sleep(43)
        print("end...")
        anjian2()
        print("end1...")
        sheep_time1 = random.uniform(6, 9)
        sleep(sheep_time1)
        print("end2...暂停时间%f"%sheep_time1)
        anjian3()
        print("退出...")
        sheep_time2 = random.uniform(5, 8)
        sleep(int(sheep_time2))
        print("下一次挑战,暂停时间%f"%sheep_time2)
        #pull_screenshot()

if __name__ == '__main__':
    main()