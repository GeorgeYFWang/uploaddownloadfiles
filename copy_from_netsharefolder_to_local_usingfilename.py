# -*- coding: utf-8 -*-
import wave
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import os, sys, re
import struct
import time

# 目的：本脚本将file list文件夹下所有list中的语音振幅全部拉至80%处。
#      然后生成新的file list文件夹。该文件夹会生成于本脚本的目录下
#
#

if not os.path.isdir('./wav_word_list_selected'):
    os.makedirs('./wav_word_list_selected')
else:
    for i in os.listdir(r'./wav_word_list_selected'):
        path_file = os.path.join(r'./wav_word_list_selected', i)  # 取文件路径
        if os.path.isfile(path_file):
            os.remove(path_file)

# 修改处1.   存放最后语音的文件夹
dst_path = r'./wav_word_list_selected'

if not os.path.isdir(dst_path):
    os.makedirs(dst_path)
else:
    for i in os.listdir(dst_path):
        path_file = os.path.join(dst_path, i)  # 取文件路径
        if os.path.isfile(path_file):
            os.remove(path_file)

# 修改处2.   原始的语音文件file list
src_path = r'./word_list_selected'

# 生成的最终file list
# 位置位于当前路径下filelist中
#
# 文件夹，存放着不同语音的文件
if os.path.exists(dst_path):
    print('已经存在文件夹')
else:
    os.mkdir(dst_path)

# 生成的wordlist文件夹
cur_path = os.getcwd()
if os.path.exists(cur_path + '\\' + 'file_list'):
    # print('已经存在文件夹')
    for i in os.listdir('file_list'):
        path_file = os.path.join('file_list', i)  # 取文件路径
        if os.path.isfile(path_file):
            os.remove(path_file)
else:
    os.mkdir(cur_path + '\\' + 'file_list')

# dir_name = os.listdir(src_path) #获得命令词列表
# for temp in dir_name: #枚举命令词.txt
#     if '.txt' in temp: #确认是 命令词.txt
#         f_txt_file = src_path+'\\'+temp #该命令词的相对路径
#         with open(f_txt_file,'r',encoding='utf-8') as f_wav_list_file: #打开命令词.txt
#             L_wav_file = f_wav_list_file.readlines()#取得该命令词的所有语音路径列表
wav_name_list = os.listdir(r'./wavs')  # 获取语音文件名列表
for tmp in wav_name_list:  # 对每一个语音路径循环
    # 还原在服务器上的路径
    str_wav_name = tmp  # 取得语音文件名
    tmp = r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\aishell\wav' + '\\' + tmp
    # get wav name
    desFilename = r'D:\pythonproject\yuyinbao\wav_word_list_selected' + '\\' + str_wav_name
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
