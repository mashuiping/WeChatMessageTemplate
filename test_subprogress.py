import subprocess
import sys
from send_template_message import *
import threading

if __name__ == '__main__':
	print "in"
	subprocess.Popen("python update_access_token.py", shell = True)
	print "out"
	sys.exit()