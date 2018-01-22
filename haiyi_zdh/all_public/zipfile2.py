#coding=utf-8
#使用zipfile做目录压缩，解压缩功能
import os,os.path
import zipfile
 
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)#当前文件入列表
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))#文件入列表
                print filelist
    #创建压缩文件    
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)#zipfile.zlib.DEFLATED 亦可
    #写入目录树
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
 
 
def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')
        
        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:            
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
 
if __name__ == '__main__':
    zip_dir(r'E:\test_zdh\TJHKZDH2\img',r'E:\test_zdh\TJHKZDH2\img\img.zip')
    #unzip_file(r'E:/python/learning/zip.zip',r'E:/python/learning2')