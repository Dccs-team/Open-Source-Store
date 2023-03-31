# -*- coding:utf8 -*-

# Supports python & python3
# Name   : PyObfuscate - Simple Python Code Obfuscator
# Author : SaiMun-cyber-403
# Date   : Sun Jul 19 00:19:27 2022

# Import Modules
import os
import sys
import zlib
import time
import base64
import marshal
import requests
import py_compile
os.system('xdg-open https://facebook.com/saimonk189')
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")
    
    
logo =                                          ("""   
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
┃\033[1;91m    _____         _____ __  __  ____  _   _ ┃
┃  / ____|  /\   |_   _|  \/  |/ __ \| \ | | ┃
┃ | (___   /  \    | | | \  / | |  | |  \| | ┃
┃\033[1;97m  \___ \ / /\ \   | | | |\/| | |  | | . ` | ┃
┃  ____) / ____ \ _| |_| |  | | |__| | |\  | ┃
┃ |_____/_/    \_\_____|_|  |_|\____/|_| \_|©┃
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\033[1;32m┌━━━━━━━━━━━━━━━━━ \033[1;97mSAIMON\33[0;m \033[1;32m━━━━━━━━━━━━━━━━━━┑
\033[1;32m┃   \033[1;32mCREATED BY\33[0;m   :  \033[1;32mSAIMON.CYBER            ┃
┃   \033[1;32mFACEBOK      : \033[1;32m SAIMONk189              ┃
┃   \033[1;32mGITHUB       :  \033[1;32mSAIMUN.CYBER.403        ┃
┃   \033[1;32mTOOL VIRSION :  \033[1;32m2.0                     ┃
└━━━━━━━━━━━━━━━━━ \033[1;97mSAIMON\33[0;m \033[1;32m━━━━━━━━━━━━━━━━━━┘\n\033[1;33m""")



###don't replace this###


# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "\x23\x20\x4F\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x50\x79\x4F\x62\x66\x75\x73\x63\x61\x74\x65\x0A\x23\x20\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x53\x61\x69\x4D\x75\x6E\x2D\x63\x79\x62\x65\x72\x2D\x34\x30\x33\x0A\x23\x20\x54\x69\x6D\x65\x20\x3A\x20\x25\x73\x0A\x23\x20\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x0A" % time.ctime()
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)

#def banner(): # Program Banner
    #print(logo)

def menu(): # Program Menu
    jalan("\x20\x5b\x30\x31\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x0a\x20\x5b\x30\x32\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x0a\x20\x5b\x30\x33\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x31\x36\x0a\x20\x5b\x30\x34\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x33\x32\x0a\x20\x5b\x30\x35\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x36\x34\x0a\x20\x5b\x30\x36\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x42\x61\x73\x65\x31\x36\x0a\x20\x5b\x30\x37\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x42\x61\x73\x65\x33\x32\x0a\x20\x5b\x30\x38\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x42\x61\x73\x65\x36\x34\x0a\x20\x5b\x30\x39\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x5a\x6c\x69\x62\x0a\x20\x5b\x31\x30\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x42\x61\x73\x65\x31\x36\x0a\x20\x5b\x31\x31\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x42\x61\x73\x65\x33\x32\x0a\x20\x5b\x31\x32\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x42\x61\x73\x65\x36\x34\x0a\x20\x5b\x31\x33\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x5a\x6c\x69\x62\x2c\x42\x31\x36\x0a\x20\x5b\x31\x34\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x5a\x6c\x69\x62\x2c\x42\x33\x32\x0a\x20\x5b\x31\x35\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x5a\x6c\x69\x62\x2c\x42\x36\x34\x0a\x20\x5b\x31\x36\x5d\x20\x53\x69\x6d\x70\x6c\x65\x20\x45\x6e\x63\x6f\x64\x65\x0a\x20\x5b\x31\x37\x5d\x20\x45\x78\x69\x74\n")

class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Encoded File Size : %s\n" % self.datas(dts))
# FileSize('rec.py')

def Encode(option,data,output):
    loop = int(eval(_input % " [-] Encode Count : "))
    print (' [-] Please Wait Encoding Is Starting ')
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n Invalid Option!")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Main Menu
def MainMenu():
    try:
        os.system('clear') # os.system('cls')
        print(logo)
        menu()
        try:
            option = int(eval(_input % " [-] Option : "))
        except ValueError:
            sys.exit("\n Invalid Option !")
        
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n Thanks For Using this Tool")
            os.system('clear') # os.system('cls')
            print(logo)
            #banner()
        else:
            sys.exit('\n Invalid Option !')
        try:
            file = eval(_input % " [-] File Name : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n File Not Found!")
        
        output = file.lower().replace('.py', '') + '_enc.py'
        if option == 16:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        print("\n [-] Successfully Encrypted %s" % file)
        print(" [-] Saved as %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()
