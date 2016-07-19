# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# 合并当前文件夹下所有txt文件到指定文件(e.g. email.txt)
# Author : oneroy@qq.com
#-------------------------------------------------------------------------------
import os
import time

def main():
    docList = os.listdir(os.curdir)
    docList.sort()                # 显示当前文件夹下所有文件列表并进行排序

    for i in docList:
        print i         #输出文件名

    fname = open("email.txt", "w")              #创建一个xx.txt文件
    for i in docList:
        if '.txt' in i:
            x = open (i ,  "r")                      #打开列表中的文件读取文件内容
            fname.write(x.read())                    #写入xx.txt中
            x.close()                                #关闭列表文件

    fname.close()
    print 'Done!'

if __name__ == '__main__':
    main()
