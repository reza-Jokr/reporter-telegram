import time,os,platform
try:from prettytable import PrettyTable
except:os.system("pip install prettytable")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'
def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)  
if 'Windows' in platform.uname():
    from colorama import init
    init()
else:
    pass
banner = f"""
                                                                 
{k}                                                                
 ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
 ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
 ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
 ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
 ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
 ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁
      𝗿𝗲𝗽𝗼𝗲𝘁𝗲𝗿-𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 <> 𝗝𝗢𝗞𝗘𝗥           
"""

re(banner)
re("Warning ! This is a test reporter, any offense is the responsibility of the user !")
print (f"{lrd}")
t = PrettyTable([f'{cn}Number{lrd}',f'{cn}info{lrd}'])
t.add_row([f'{lgn}1{lrd}',f'{gn}Reporter Channel{lrd}'])
t.add_row([f'{lgn}2{lrd}',f'{gn}Reporter Account{lrd}'])
t.add_row([f'{lgn}3{lrd}',f'{gn}Reporter Group [Updating]{lrd}'])
print (t)

number = input(f"{gn}Enter Number : {cn}")
if number == "1":
    os.system("python report/reporter.py")
if number == "2":
	os.system("python report/report.py")
elif number == "3":
    print ("This section is being updated and will be added soon \n\n𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 : IMPOSR")
