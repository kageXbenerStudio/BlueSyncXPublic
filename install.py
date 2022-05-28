import os

os.system("clear")
os.system("termux-setup-storage")
print "Check BlueSyncXApi..."
os.system("python2 /sdcard/BlueSyncX/InstallBlueSyncXApi/InstallBlueSX.py")
os.system("clear")
print "Not Found BlueSyncXApi!"
os.system("sh InstBlueSyncXApi")
