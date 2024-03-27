from xanthin_compiler_defs import *
from xanthin import *
import os
import time
from call_function_with_timeout import SetTimeoutDecorator

print("©2024 xanthin loader file.")
print("more info in http://xanthin.loxblog.com/page/loader")
print("type .xan file addres to run.")
b = input()
if(b!=""):
	xanthin.run(b)
	moo = b.replace(".xan",".py")
	__import__=(moo)
	__import__=(moo)
	oas = input()
	if(oas=="~delete cache"):
	   	os.remove(moo)
	   	print("DONE")
		
else:
		oas = input()
		if(oas=="~delete cache"):
		  	gi = input()
		  	moo = gi.replace(".xan",".py")
		  	os.remove(moo)
		print("DONE!")
		