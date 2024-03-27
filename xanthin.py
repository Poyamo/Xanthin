import os
import os.path
import shutil
import importlib
import subprocess
import json
import sys
from varname.helpers import Wrapper
from varname import varname
#info of xanthin package.
version_of_xanthin = "0.0.1"
build = "DHJ-185-0823-mar"
class message:
	def show(a):
		print(a)
    
to = "to"
write = "write"
local = "local"
email = "email"
class var:
   def set(g , to ,numb):
   	globals()[g] = numb

class file:
   def create(name, write , s):
   	f = open(name,"a")
   	f.write(s)
   	f.close()
   
   def read(name, local , mkm):
   	k = open(mkm,"r")
   	k.read()
   	
   def copy(name , to ,sname):
      shutil.copy(name, sname)
      
   def delete(name):
   	os.remove(name)

   def be(fname):
   	os.path.exists(fname)


   def delete__folder__(fname):
   		os.rmdir(fname)
  	
   def move(fname , to ,sdf):
   	shutil.move(fname,sdf)



against = "against"
def Acceptation(fname , against ,lets):
    x = __import__(fname)
    
class archive:
	def create(file_type, local , to ,ziplocal):
		shutil.make_archive(local, file_type ,zipelocal)
		

run = "run"	
void = "void"

def type(hjk,xcv):
	    if(xcv==""):
	       hjk
	    else:
	    	hjk
	    	xcv
	    	class top:
	    		print("")
	    		

def call(fname,x):
	if(x=="true"):
		lo = subprocess.call(fname, shell=x)
		lo
	else:
		if(x=="false"):
			lo = subprocess.call(fname, shell=x)
			lo
		else:
			print("error from Xanthin")
			print("error: you can type only boolen's.")
	
def main(fname):
	if(fname==""):
		print("ERROR FROM XANTHIN")
		print("error: main is empty.")
	else:
		fname

import sys 


import time
def delete_cahac():
	file.delete(b+".py")

class inputs:
	def new():
		input()

packs = file.read("pack.txt", local , "pack.txt")
class get:
	def packages():
		packs = file.read("pack.txt", local , "pack.txt")
	
def mgl():
	return varname()

def show():
	return varname()
	