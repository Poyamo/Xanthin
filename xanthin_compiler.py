
import urllib.request
import sys
import os
from xanthin import *
print("©2024 Xanthin Programming Languge Compiler")
print("information go to 'http://xanthin.lxb.com/page/compiler.html")
print("type your law in next line...")
c = input()

v = "print('©2024 IMK Xanthin Package Manager')\nprint('for install your like package type')\nprint('~IMK install package_name')\nmgk = input()\nif(mgk=='~IMK upgrade'):\n   print('[find from server-A...]')\n   print('[000%]')\n   print('uknow error')\ninput()\nversion_of_imk = '1.0'"

gh = "input()"
if(c=="~install rad from server-def"):
    print("do")
else:
		if(c=="~info of compiler"):
			print("version 0.0.1")
			print("build *67")
			print("mode *unload")
			print("name of package Xanthin I")
			
		else:
				if(c=="~install IMK from server-def"):
					if(os.path.exists("imk.py")):
						print("Error: IMK is before installed at system.")
						print("do you want upgrade IMK ?")
						print("for upgrade type '~install IMK upgrade'")
						print("for programm finsed type someting.")
					else:
						file.create("imk.py", write , v+"\nbuild_of_imk = 'fverofIMK-01'")
						file.create("imk_info.py" , write ,"build_of_imk = 'fverofIMK-01'\nversion_of_imk = '1.0'")
						print("done")
						import imk
				else:
						if(c=="~info of rad"):
							print("name of package rad-Xanthin-1")
							print("version 1.0")
							print("do you want load info.txt?")
							bjk = input()
							if(bjk=="y"):
								print("empty.")
								
						else:
							if(c=="~info of xanthin"):
								print("version"+" "+version_of_xanthin)
								print("build "+build)
								print("for finshed programm enter something.")
							else:
									if(c=="~IMK"):
										from imk import *
									else:
											if(c=="~info of IMK"):
												if(os.path.exists("imk.py")):
													from imk_info import *
													print("build"+build_of_imk)
													print("version"+version_of_imk)
												else:
														print("IMK pack not install at system.")
											else:
												if(c=="~install Ruby2xanthin"):
													print("done")
												else:
													print("unkonw")
															
c = input()
if(c=="y"):
      os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 