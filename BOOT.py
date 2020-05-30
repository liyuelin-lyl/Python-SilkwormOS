# -*- coding: utf-8 -*-
#copyright(c) 2020 Li Yuelin
#All right Reserved
##############################################

print("Hello!")
print("Thank you used SilkwormOS!")
print("  ")
print("  ")
print("==================================================================================")
print("  ")
print("本操作系统部分源码来自网上，若有侵权请联系删除（其实一些简单的是原创的，难的是搜到的）!")
print("by liyuelin♂")
print("qq号：2756254671")

#下面是有用的源码。
import pywifi
from pywifi import const,Profile
import os
import requests
import webbrowser as web
import webbrowser
import time
from zipfile import ZipFile
import zipfile
from zipfile import *
import sys
import pygame
import shutil
from shutil import make_archive
from pyftpdlib.authorizers import DummyAuthorizer
from  pyftpdlib.handlers  import FTPHandler
from  pyftpdlib.servers import FTPServer
import smtplib
import qrcode
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from os import listdir
from os.path import isfile, isdir, join
from email.utils import parseaddr, formataddr
class OS():
    def __init__(self):
        self.dict={
            "open_file":self.open_file,   
            "cd":self.cd,
            "create_file":self.create_file,
            "web_request":self.web_request,
            "picture_show":self.picture_show,
            "create_dir":self.create_dir,
            "remove_dir":self.remove_dir,
            "walk_tree":self.walk_tree,
            "FTP_server":self.ftp_server,
            "power_off":self.power_off,
            "FTP_client":self.ftp_client,
            "connect_wifi":self.connect_wifi,
            "math":self.math,
            "send_mail":self.send_mail,
            "catch_mail":self.catch_mail,
            "make_qr":self.make_qr,
            "info":self.info,
            "web_browser":self.web_browser,
            "unzip":self.unzip,
            "new_zip":self.new_zip,
            "add_file_to_zip":self.add_zip,
            "del_file":self.del_file,
            "rename":self.rename,
            "help":self.help,
            "run":self.run,
            "python":self.python
            }
            
    def cd(self):
        a=input("cd Path>")
        print(os.getcwd()) 
        os.chdir(a)
    def open_file(self):
        a=input("filename>")
        f=open(a,"a+")
        for ff in f.readlines():
            print(ff)
        print("==================")
        while True:
            wr=input("Write[type ___QUIT__;; to quit writing mode.]>")
            if wr == "___QUIT__;;":
                print("Quit successfully.")
                break
            else:
                f.write(wr)
        f.close()
    def create_file(self):
        creat=open(input("New file name>"),"w")
        print("create new file successfully.")
        creat.close()
    
    def web_request(self):
        w=input("web_site>")
        headers={'User-Agent':'OW64; rv:59.0 Gecko/20100101 Firefox/59.0'}
        try:
            r=requests.get(w,headers=headers,timeout=120)
            print("status:",r.status_code)
            print("url:",r.url)
            print("headers:",r.headers)
            print("cookies:",r.cookies)
            print("code[text]:",r.text)
            print("code[content]:",r.content)
        except:
            print("HTTPError:HTTPError")
            print("Host:",w)
    def picture_show(self):
        pygame.init()
        size=width,height=640,480
        screen=pygame.display.set_mode(size)
        color=(0,0,0)
        picture=pygame.image.load(input("Filename>"))
        picturerect=picture.get_rect()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                    break
                screen.fill(color)
                screen.blit(picture,picturerect)
                pygame.display.flip()
        pygame.quit()
    def create_dir(self):
        dir_name=input("Name>")
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        else:
            print("ERROR:dir'",dir_name,"is in this path")
        del dir_name
    def remove_dir(self):
        dir_name=input("Path>")
        try:
            shutil.rmtree(dir_name)
        except:
            print("ERROR:no this path")
    def walk_tree(self):
        top_=input("tree>")
        for walk_ in os.walk(top_):
            print(walk_)
            print(" ")
            print(" ")
            print(" ")
        print("=========================")
    def ftp_server(self):
        ip=input("Server_IP>")
        port=int(input("Server_port>"))
        authorizer = DummyAuthorizer()
        authorizer.add_user('user', '12345', 'FTP_user', perm='elradfmwMT')
        authorizer.add_anonymous('FTP_anonymous')
        handler = FTPHandler
        handler.authorizer = authorizer
        server = FTPServer((ip,port), handler)
        print("root user:user,pwd:12345")
        server.serve_forever()
    def ftp_client(self):
        s_ip=input("Server IP>")
        s_p=int(input("Server port>"))
        usr=input("FTP user-name>")
        usr_pwd=input("FTP_password>")
        s_path=input("Download server path>")
        cli_path=input("Download to>")
        ftp = FTP()
        ftp.connect(s_ip,s_p)
        ftp.login(usr, usr_pwd)
        Server_path = s_path
        Client_path=cli_path
        sum1 = 0
        sum2 = 0
        value = 0
        FTP_Dir_l = []
        Ftp_file_l = []
        if re.search(r".*/$",Server_path):
            pass
        else:
            Server_path = Server_path+"/"
        if os.path.exists(Client_path):
            print("OS notfound",Client_path,",created a new path.")
            os.makedirs(Client_path)
        def search_dir(start_dir):
            ftp.cwd(start_dir)
            FTP_Dir_l.append(ftp.pwd())
            dir_res = []
            ftp.dir('.', dir_res.append) 
            for i in dir_res:
                if i.startswith("d"):
                    global sum1 
                    sum1 += 1
                    search_dir(ftp.pwd()+"/"+i.split(" ")[-1])
                    ftp.cwd('..')
                else:
                    global sum2, value
                    sum2 += 1
                    val = i.split(" ")[-1]
                    value += ftp.size(val)
        def search_file(Dir_path):
            search_dir(Dir_path)
            for Server_f_l in FTP_Dir_l:
                file_list = ftp.nlst(Server_f_l)
                for Server_file in file_list:
                    if Server_file not in FTP_Dir_l:
                        Ftp_file_l.append(Server_file)
        search_file(Server_path)
        os.chdir(Client_path)
        for local_dir in FTP_Dir_l:
            if os.path.isdir(local_dir.split(Server_path,1)[-1]):
                pass
            else:
                print(local_dir.split(Server_path,1)[-1],"ERROR:OS notfound this path,created a new path.")
                os.makedirs(local_dir.split(Server_path,1)[-1])
        for Get_f in Ftp_file_l:
            print(Get_f,"download to this path:",Client_path+os.sep+Get_f.split(Server_path,1))[-1]
            fp = open(Client_path+os.sep+Get_f.split(Server_path,1)[-1],'wb')
            ftp.retrbinary('RETR ' +Get_f,fp.write,1024)
        ftp.close()
    def connect_wifi(self):
        profile = pywifi.Profile()
        profile.ssid = input("wifi ssid>")
        profile.auth = const.AUTH_ALG_OPEN     
        profile.akm.append(const.AKM_TYPE_WPA2PSK) 
        profile.cipher = const.CIPHER_TYPE_CCMP   
        profile.key = input("WiFi key>")
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0] 
        profile = iface.add_network_profile(profile)
        iface.connect(profile)
        time.sleep(3)
        if iface.status()==const.IFACE_CONNECTED:
            print("connect success.")
        else:
            print("connect fail.")
    def math(self):
        a=input("+,-,*,/>")
        n1=int(input("num1>"))
        n2=int(input("num2>"))
        n3=int(input("num3>"))
        n4=int(input("num4>"))
        num="ERROR"
        if a=="+":
            num=n1+n2+n3+n4
        elif a=="-":
            num=n1-n2-n3-n4
        elif a=="*":
            num=n1*n2*n3*n4
        elif a=="/":
            num=n1/n2/n3/n4
        else:
            print("ERROR:",a,"is not in[+,-,*,/]")
        print("num:",num)
    def send_mail(self):
        host=input("SMTP host>")
        port=int(input("SMTP host's port>"))
        your_email=input("your email>")
        pwd=input("your password>")
        send_email=input("send to>")
        subject=input("subject>")
        message=input("message>")
        msg = MIMEText("text",'html','utf-8')
        msg['From'] = u'<%s>' % your_email
        msg['To'] = u'<%s>' % send_email
        msg['Subject'] = subject

        smtp = smtplib.SMTP_SSL(host,port)
        smtp.set_debuglevel(1)
        smtp.ehlo(host)
        smtp.login(your_email, pwd)
        smtp.sendmail(your_email, [send_email], msg.as_string())
    def catch_mail(self):
        user=input("username>")
        password=input("password>")
        M = imaplib.IMAP4()
        M.login(user,password)
        M.select()
        typ, data = M.search(None, 'ALL')
        for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')
            print('Message %s\n%s\n' % (num, data[0][1]))
        M.close()
        M.logout()
    def make_qr(self):
        make__=input("make>")
        filename=input("filename>")
        myqr=qrcode.make(make__)
        myqr.save("D:\\"+filename)
    def info(self):
        i=input("path>")
       
        print(stat(i))
    def web_browser(self):
        chromePath = r'C:\Mozilla Firefox\firefox.exe'
        webbrowser.register('chrome', None, web.BackgroundBrowser(chromePath))
        website=input("website[temple:https://www.baidu.com/]>")
        webbrowser.get('chrome').open(website,new=1,autoraise=True)
    def run(self):
        run=input("EXE file>")
        webbrowser.register('EXE', None, web.BackgroundBrowser(run))
        webbrowser.get('EXE').open("",new=1,autoraise=True)
    def unzip(self):
        source_zip=input("source zip>") 
        target_dir=input("target dir>")
        myzip=ZipFile(source_zip) 
        myfilelist=myzip.namelist() 
        for name in myfilelist: 
            f_handle=open(target_dir+name,"wb") 
            f_handle.write(myzip.read(name))       
            f_handle.close() 
            myzip.close()
        fz.close()
    def new_zip(self):
        f=input("new file name>")
        d=input("zip dir>")
        shutil.make_archive(f,"zip",d)
        print("create zip success.")
    def add_zip(self):
        z=input("zip file>")
        f=input("file>")
        zip_=zipfile.Zipfile(z,"w",zipfile.ZIP_DEFLATED)
        zip_.write(f)
        print("add success.")
        f.close()
    def power_off(self):
        print("请按下你的关机键")
    def del_file(self):
        d=input("path>")
        os.remove(d)
    def rename(self):
        f=input("file/dir name>")
        n=input("new name>")
        os.rename(f,n)
    def help(self):
        print("cd                   -------change dir")
        print("open_file            -------open a file")
        print("create_file          -------create a new file")
        print("web_request          -------request a website")
        print("picture_show         -------show a picture")
        print("create_dir           -------create a dir")
        print("remove_dir           -------remove a dir")
        print("walk_tree            -------walk a dir")
        print("power_off            -------close your computer")
        print("FTP_server           -------open your FTP server")
        print("FTP_client           -------connect a FTP server")
        print("connect_wifi         -------connect a WLAN network")
        print("math                 -------math")
        print("send_mail            -------send a e-mail")
        print("catch_mail           -------catch e-mail")
        print("make_qr              -------make a qrcode")
        print("unzip                -------unzip a zip file")
        print("new_zip              -------create a zip file")
        print("add_file_to_zip      -------add a file to a zip file")
        print("info                 -------file(dir) info")
        print("remove_file          -------remove a file")
        print("rename               -------rename a file or dir")
        print("run                  -------run a EXE file")
        print("web_browser          -------browser a web site[temple:https://www.baidu.com]")
        print("python               -------open python")
        print("windows_cmd          -------Windows 命令提示符模拟器")
        print("如果你想通过命令行来给程序传参，你可以更改程序中的内容，然后再运行程序。")
    def python(self):
        run="C:\\Python35\\python.exe"
        webbrowser.register('EXE', None, web.BackgroundBrowser(run))
        webbrowser.get('EXE').open("",new=1,autoraise=True)
    def cmd(self):
        while True:
            command=input(str(os.getcwd())+">")
            if self.dict.keys().__contains__(command):
                self.dict[command]()            
MyOS=OS()
MyOS.cmd()

