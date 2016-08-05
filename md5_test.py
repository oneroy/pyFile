#python 检测文件MD5值
#python version 2.6

import hashlib
import os,sys
import urllib2
import md5

sys.argv = ["detect.py","http://www.motorchina.com/sysImages/folder/error.gif"]
##sys.argv = ["detect.py","error.gif"]

#简单的测试一个字符串的MD5值
def GetStrMd5(src):
    m0=hashlib.md5()
    m0.update(src)
    print m0.hexdigest()
    pass

#大文件的MD5值
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
        return hash

def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        print('md5=========', hash)
        return hash

def CalcMD5_byUrl(url):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    data = res.read()
    myHash = md5.md5(data).hexdigest()
    print ('md5_byUrl=========',myHash)
    return myHash

if __name__ == "__main__":
    if len(sys.argv)==2 :
        hashfile = sys.argv[1]
        if 'http://' in hashfile or 'https://' in hashfile:
            CalcMD5_byUrl(hashfile)
##            req = urllib2.Request(hashfile)
##            res = urllib2.urlopen(req)
##            data = res.read()
##            print 'md5=========',md5.md5(data).hexdigest()
        else:
            if not os.path.exists(hashfile):
                hashfile = os.path.join(os.path.dirname(__file__),hashfile)
                if not os.path.exists(hashfile):
                    print("cannot found file")
                else:
                    CalcMD5(hashfile)
            else:
                CalcMD5(hashfile)
                #raw_input("pause")
    else:
        print("no filename")