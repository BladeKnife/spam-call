import os,sys,time
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)
kata('''\033[91m[!]\033[00mScript Sudah Koid
Silahkan Update Ketikan: git pull jika sudah
Ketikan: python call-1.py''')
