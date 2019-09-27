# -*- coding: utf-8 -*-

import os, sys, re

import time


wav_name_list = os.listdir(r'./yuyinbao_wav')  # 获取语音文件名列表
for tmp in wav_name_list:  # 对每一个语音路径循环
    # 还原在服务器上的路径
    str_wav_name = tmp  # 取得语音文件名
    tmp = r'D:\pythonproject\yuyinbao\yuyinbao_wav' + '\\' + tmp

    #tmp = r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\aishell\wav' + '\\' + tmp
    # get wav name
    desFilename = r'\\192.168.200.20\share\Exchange\hftest\wav\20190925yuyinbao' + '\\' + str_wav_name
    print(str_wav_name)

    f_wav_name = tmp

    # 复制文件到本地目标文件夹


    #copyCommand = 'copy %s %s' % (srcFilename, desFilename)
    copyCommand = 'copy %s %s' % (tmp, desFilename)

    try:
        if (os.popen(copyCommand)):  # 不用op.system(copyCommand),因为这个会弹出命令行界面
            print('copy done!')
            status = True
        else:
            print('copy failed!')
            status = False
    except Exception as e:
        print(e)
        status = False
    finally:
        print('copyFile function is quit!')
    time.sleep(1)
