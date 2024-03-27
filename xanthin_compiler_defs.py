#this compiler_def for android.
import os
import shutil
import importlib
class xanthin:
	def run(fname):
			empty = open(fname,"r")
			gaza = empty.read()
			em = gaza.replace("void main or mains(","\nfrom xanthin import *\n")
			t = em.replace("-","")
			y = t.replace(":","=")
			nkk = fname.replace(".xan",".py")
			fun = open(nkk,"a")
			nofun = fun.write(y)
			k = nkk.replace(".py","")
			__import__(k)