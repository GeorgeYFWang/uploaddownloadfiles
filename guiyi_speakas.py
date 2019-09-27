# -*- coding: utf-8 -*-
import wave
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import os
import struct
import time
import shutil


#目的：本脚本将file list文件夹下所有list中的语音振幅全部拉至80%处。
#      然后生成新的file list文件夹。该文件夹会生成于本脚本的目录下
#
#

# if not os.path.isdir('./wav_word_list_selected'):
#     os.makedirs('./wav_word_list_selected')
# else:
#     for i in os.listdir(r'./wav_word_list_selected'):
#         path_file = os.path.join(r'./wav_word_list_selected', i)  # 取文件路径
#         if os.path.isfile(path_file):
#             os.remove(path_file)
#


#修改处1.   存放最后语音的文件夹
dst_path = r'./wav_word_list_selected'
wav_name_path = r'./wavs'
wav_src_path = r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\aishell\wav'

# 创建存放处理后的语音的文件夹，若存在则清空
if not os.path.isdir(dst_path):
    os.makedirs(dst_path)
else:
    for i in os.listdir(dst_path):
        path_file = os.path.join(dst_path, i)  # 取文件路径
        if os.path.isfile(path_file):
            os.remove(path_file)

# 从当前语音文件夹中取得需要处理的语音文件名列表
def get_wav_name_from_dir(dir):
    filePath = dir
    wav_name_list = os.listdir(filePath)
    return wav_name_list

wav_name_list1 = get_wav_name_from_dir(wav_name_path)
wav_name_list2 = get_wav_name_from_dir(wav_src_path)

for i in wav_name_list1:
    if i in wav_name_list2:
        print('have found :' + i)
        src_file = wav_src_path + '\\' + i
        copyCommand = 'copy %s %s' % (src_file,dst_path)
        print('copyCommand' + copyCommand)
        if os.system(copyCommand) == 0:
            print('copy successed!')
        else:
            print('copy failed!')
        break
#
# for temp in wav_name_list1:
#     if temp in wav_name_list2:
#         src = wav_src_path + temp
#         shutil.copy(src, dst_path)
#
#
#
# sharePath =  r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\aishell\wav'
# fileList = os.listdir(sharePath)
#
# for filename in sharePath:
#     if filename == 'toFindFileName':
#         print('have found :' + filename)
#         srcFilename = sharePat + '\\' + filename
#         desFilename = 'd:\\ftp\\下载\\'
#         copyCommand = 'copy %s %s' % (srcFilename, desFilename)
#         print('copyCommand' + copyCommand)
#
#         if os.system(copyCommand) == 0:
#             print('copy successed!')
#         else:
#             print('copy failed!')
#         break