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


    '''
    # else:
    #     f_wav_name = tmp
    # 打开WAV文档
    print(f_wav_name)
    f_rb = open(f_wav_name, "rb")
    # 首先载入Python的标准处理WAV文件的模块，然后调用wave.open打开wav文件，注意需要使用"rb"(二进制模式)打开文件：
    f = wave.open(f_wav_name, "rb")
    # open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据：
    # 读取格式信息
    # (nchannels, sampwidth, framerate, nframes, comptype, compname)
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]

    # getparams：一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率,
    # 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息：
    # getnchannels, getsampwidth, getframerate, getnframes等方法可以单独返回WAV文件的特定的信息。
    print(nchannels)
    print(sampwidth)
    print(framerate)
    print(nframes)

    # 读取波形数据
    str_data = f.readframes(nframes)
    # readframes：读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位），readframes返回的是二进制数据（一大堆
    # bytes)，在Python中用字符串表示二进制数据：
    f.close()

    i_range = int(nframes)
    L_wav_node = []
    L_wav_abs_node = []
    L_new_wav_node = []

    for i in range(0, i_range):
        i_x = str_data[2 * i + 1] * 256 + str_data[2 * i]
        # convert to signed int
        if i_x > 32768:  # means it is a negative value
            L_wav_node.append(i_x - 65536)
        else:
            L_wav_node.append(i_x)

    # 得到最大值
    int_max = np.max(L_wav_node)
    print(int_max)
    int_dst_max = 32767 * 0.8  # 将振幅拉到70%

    f_times = (int_dst_max / int_max)

    for tmp1 in L_wav_node:
        int_new_value = tmp1 * f_times
        L_new_wav_node.append(round(int_new_value))
        # print(tmp1)
        # print(round(int_new_value))

    L_new_wav_node_one_byte = []

    with open(dst_path + '\\' + str_wav_name, 'wb') as f_dst_wave_file:
        f_dst_wave_file.write(f_rb.read(44))
        for i in range(0, len(L_new_wav_node)):
            if L_new_wav_node[i] >= 0:
                L_new_wav_node_one_byte.append(int(L_new_wav_node[i] % 256))
                L_new_wav_node_one_byte.append(int((L_new_wav_node[i] / 256) % 256))
            else:
                i_new_value = L_new_wav_node[i] + 65536
                L_new_wav_node_one_byte.append(int(i_new_value % 256))
                L_new_wav_node_one_byte.append(int((i_new_value / 256) % 256))

            a = struct.pack('B', L_new_wav_node_one_byte[2 * i])
            f_dst_wave_file.write(a)
            a = struct.pack('B', L_new_wav_node_one_byte[2 * i + 1])
            f_dst_wave_file.write(a)
    f_rb.close()

# #生成新的file list
# fp_out_x = open(cur_path+'\\'+'file_list'+'\\'+temp,'w')
# for one_path_wav in L_wav_file:
#     one_wav_name = one_path_wav.split("\\")[-1] #将原file list的txt中的语音拷贝至新的file list中，然后将路径替换掉
#     dst_path1 = r'\\192.168.200.20\share\Exchange\hftest\wav\20190925yuyinbao'
#     fp_out_x.write(dst_path1+'\\'+one_wav_name)
# fp_out_x.close()
'''
