#coding=utf-8
#使用zipfile做目录压缩，解压缩功能
import os,os.path
import zipfile
 
def zip_dir(dirname1,dirname2,zipfilename):
    filelist = []
    #创建压缩文件    
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)#zipfile.zlib.DEFLATED 亦可
    #获取第一个目录下的文件并加入filelist
    for root, dirs, files in os.walk(dirname1):
        for name in files:
            filelist.append(os.path.join(root, name))#文件入列表
    #写入第一个目录下的文件
    for tar in filelist:
        arcname = tar[len(dirname1):]
        print arcname
        zf.write(tar,arcname)
    zf.write(dirname2,dirname2.split('\\')[-1])
    print dirname2.split('\\')[-1]
##    filelist = []
##    #获取第二个目录下的文件并加入filelist
##    for root, dirs, files in os.walk(dirname2):
##        for name in files:
##            filelist.append(os.path.join(root, name))#文件入列表
##    #写入第二个目录下的文件
##    for tar in filelist:
##        arcname = tar[len(dirname2):]
##        print arcname
##        zf.write(tar,arcname)
    #关闭
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
    dir1=r'E:\test_zdh\TJHKZDH2\img\wgxl\wgxl_add'
    dir2=r'E:\test_zdh\TJHKZDH2\report'
    zippath=r'E:\test_zdh\TJHKZDH2\img\fj_zip.zip'
    zip_dir(dir1,dir2,zippath)
    #unzip_file(r'E:/python/learning/zip.zip',r'E:/python/learning2')
