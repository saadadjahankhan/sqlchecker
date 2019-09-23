import requests
import os
from colorama import Fore
import sys
import time
os.system("pip2 install colorama")
os.system("clear")

##Colors
fr = Fore.RED
fd = Fore.RESET
fg = Fore.GREEN
fc = Fore.CYAN


#printing
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./ 100)
        
def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4./ 100)
        
  
    
##codes
ban = """
|
|     _  _     _             _  
|    /_`/ //  / `/_ _  _  /_ _/_
|   ._//_\/_,/_,/ //_'/_ /\._// 
|                            
|
|  [*] SQL Injection vulnerability checker tool
|    [*] By T34M ROY4L B477L3R BD
|      [*]Author:  Mr.V3N0M
| 
|               Respect coders, 
|Coz single line of code can destroy your system.!
|
"""
payload = "%27"
slowprint(fr+ban+fd)
siteF = raw_input(fc+"[*]Sitelist to check: "+fd)
slowprint2(fr+"\n   Checking sites...\n     Please wait...\n\n")
siteF = open(siteF, "r").readlines()
for sites in siteF:
	try:  #COPYING CODE WILL NOT MAKE YOU A PROGRAMMER
		s1 = requests.get(sites)
		r1 = s1.content
		
		s2 = requests.get(sites+payload)
		r2 = s2.content
		
		if r1 != r2:
			slowprint(fc+"[*] "+sites+fg+"===> Vulnerable"+fd)
		else:
			slowprint(fc+"[*] "+sites+fr+"===> Not Vulnerable.."+fd)
	except:
		print(fr+"Something went wrong...")


#COD3D BY MR.V3N0M
