import os
import time
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys

# 获取文件夹路径
app = QApplication(sys.argv)
path = QFileDialog.getExistingDirectory(None, "选择图片所在的文件夹", "/")
print('你选择的目录是: '+path)
print('')
# 获取文件夹路径
img_path = path
#保存图片路径的的文件名
f_name = input(" 输入保存提取图片名的文件(默认为:picname.txt, 默认回车):")
if f_name == '':
    f_name = "picname.txt"
try:
    f = open(f_name ,'r')
    f.close()
except IOError:
    f = open(f_name ,'w')
    f.close()
print('读取写入中...') 
print('') 
# 读取文件夹中的所有文件
imgs = os.listdir(img_path)
# 图片名列表
names = []
# 过滤：只保留图片格式
for img in imgs:
    if  (img.endswith('.jpg') or img.endswith('.png') or img.endswith('.jpeg')):
        names.append(img)
txt = open(f_name,'a')
for name in names:  
    txt.write(name + '\n')  # 逐行写入图片名，'\n'表示换行
txt.close()
print("已将 ("+img_path+")的图片信息保存到当前目录的"+f_name+"中")
print('') 
print('完成!')
print('') 
for i in range(10, 0, -1):
    print("\r程序{}秒后自动退出..".format(i), end="", flush=True)
    time.sleep(1)
