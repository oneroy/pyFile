#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 将各种URL整理成struts2网站URL

def my_struts2(line):
    if 'index?' in line or '.asp?' in line or '.aspx?' in line or '.php?' in line or '.jsp?' in line or '.act?id=' in line or '.htm' in line or '__html' in line or '.xhtml' in line or 'shtml?' in line or '/wiki/' in line or 'action=' in line or '/action' in line or '-action-' in line or '_action_' in line or '-action/' in line:
        return ''
    elif '.do?' in line:
        myline = line.split('.do')[0] + '.do'
    elif '.action?' in line or '.action;' in line:
        myline = line.split('.action')[0] + '.action'
    elif '.do' in line and 'd' == line[-2] and 'o' == line[-1]:
        myline = line.split('.do')[0] + '.do'
    elif '.do;'  in line:
        myline = line.split('.do')[0] + '.do'
    elif '.action' in line and 'o' == line[-2] and 'n' == line[-1]:
        myline = line.split('.action')[0] + '.action'
    else:
        myline = line + 'index.action'
##    print myline
    return myline

def main():
    inFile=open('S2.txt','r')
    outFile=open('struts2.txt','a+')

    while True:
        line=inFile.readline()
        if len(line)==0:break
        myline = my_struts2(line)
        if myline != '':
            outFile.write(myline +'\n')
    inFile.close()
    outFile.close()
    print 'Done'

if __name__ == '__main__':
    main()

