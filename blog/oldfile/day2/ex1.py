import os
import commands
from os import system,popen
from os import *   #not suggested
import multiprocessing as multi

print multi.cpu_count()


cmd_res = system("dir")

print "--->",cmd_res
res2=popen("dir").read()
print res2

res3 =commands.getoutput("dir")