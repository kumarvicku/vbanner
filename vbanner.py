# -*- coding: UTF-8 -*-
# Banner-Generator
# Description: 🚩 A simple and clean colourful python banner generator
# Author: kumarvicku
# Github:  https://github.com/kumarvicku
# Contact: https://www.instagram.com/v_for_vicku/

import os, sys, time, requests
from time import sleep
# Normal
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

# Bold
bblack="\033[1;30m"
bred="\033[1;31m"
bgreen="\033[1;32m"
byellow="\033[1;33m"
bblue="\033[1;34m"
bpurple="\033[1;35m"
bcyan="\033[1;36m"
bwhite="\033[1;37m"

ask = green + '[' + white + '?' + green + '] '+ yellow
success = green + '[' + white + '√' + green + '] '
error = red + '[' + white + '!' + red + '] '
pw= yellow + '\n[' + white + '+' +yellow + ']'+' Please Wait!'

os.system("clear")

logo =blue+'''
       _
'''+red+'''_    _| |__  __ __ __  _ _    __ _ __
'''+green+'''\ \ / / '_ \/  '| '_ \| '_ \ / _ \ '_|
'''+purple+''' \ V /| |) | (| | | | | | | |  __/ |
'''+cyan+'''  \_/ |_.__/\_,_|_| |_|_| |_|\__||_|

'''

def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.001)

def writer(logotext, filename):
    logotext = str(logotext)
    with open(filename, 'w') as file2:
            file2.write('''# -*- coding: UTF-8 -*-
# Generated by banner-generator. Github: https://github.com/kumarvicku/vbanner
import os, sys, time
# Normal
black="\\033[0;30m"
red="\\033[0;31m"
green="\\033[0;32m"
yellow="\\033[0;33m"  
blue="\\033[0;34m"
purple="\\033[0;35m"
cyan="\\033[0;36m"
white="\\033[0;37m"
# Bold
bblack="\\033[1;30m"
bred="\\033[1;31m"
bgreen="\\033[1;32m"
byellow="\\033[1;33m"
bblue="\\033[1;34m"
bpurple="\\033[1;35m"
bcyan="\\033[1;36m"
bwhite="\\033[1;37m"

# Use colors according to your wish       

# Use https://fsymbols.com/generators/carty/ for your own font in banner

# If you use a custom banner from any site, you may use colourbanner.py to add colors easily

logo='\'\'\n'''+logotext+'''\n'\'\'
def slowprint(n):
    for word in n + '\\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)
slowprint(logo)''')


    with open(filename, 'r') as f3:
        lines = f3.readlines()
    with open(filename, 'w') as f:
            lines [29] = "'\'\'+green+'\'\'"+ lines[29]
            lines [30] = "'\'\'+red+'\'\'"+ lines[30]
            lines [31] = "'\'\'+cyan+'\'\'"+ lines[31]
            lines [32] = "'\'\'+yellow+'\'\'"+ lines[32]
            lines [33] = "'\'\'+blue+'\'\'"+ lines[33]
            lines [34] = "'\'\'+purple+'\'\'"+ lines[34]
            lines [35] = "'\'\'+green+'\'\'"+ lines[35]
            f.writelines(lines)
    print("\n"+success+"File saved as "+filename)
    os.system("python2 "+filename)
options='''
'''+red+'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
||                       ||    '''+blue+'''       _                                              ||
||                       ||    '''+purple+'''_    _| |__  __ __ __  _ _    __ _ __                 ||
||1. Figlet              ||    '''+cyan+'''\ \ / / '_ \/  '| '_ \| '_ \ / _ \ '_|                ||
||                       ||    '''+green+''' \ V /| |) | (| | | | | | | |  __/ |                  ||
||                       ||    '''+red+'''  \_/ |_.__/\_,_|_| |_|_| |_|\__||_|                  ||
||                       ||    '''+yellow+'''                                                      ||
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
||                       ||    '''+blue+'''        #                                             ||
||                       ||    '''+purple+''' m   m  #mmm    mmm   m mm   m mm    mmm    m mm      ||
||                       ||    '''+cyan+''' "m m"  #" "#  "   #  #"  #  #"  #  #"  #   #"  "     ||
||2. Toilet              ||    '''+green+'''  #m#   #   #  m"""#  #   #  #   #  #""""   #         ||
||                       ||    '''+red+'''   #    ##m#"  "mm"#  #   #  #   #  "#mm"   #         ||
||                       ||    '''+yellow+'''                                                      ||
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
||                       ||    '''+blue+'''       _                                              ||
||                       ||    '''+purple+'''_    _| |__  __ __ __  _ _    __ _ __                 ||
||3. website             ||    '''+cyan+'''\ \ / / '_ \/  '| '_ \| '_ \ / _ \ '_|                ||
||                       ||    '''+green+''' \ V /| |) | (| | | | | | | |  __/ |                  ||
||                       ||    '''+red+'''  \_/ |_.__/\_,_|_| |_|_| |_|\__||_|                  ||
||                       ||    '''+yellow+'''                                                      ||
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                    
||                       ||    '''+blue+'''___                                                   ||
||                       ||    '''+purple+'''< vbanner >                                           ||
||4.cowsay               ||    '''+cyan+''' ---------                                            ||
||                       ||    '''+green+'''        \   ^__^                                       ||
||                       ||    '''+red+'''         \  (oo)\___                                    ||
||                       ||    '''+yellow+'''            (__)\       )\/\                          ||
||                       ||    '''+green+'''                ||----w |                             ||
||                       ||    '''+red+'''               ||     ||                                 ||
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                                  
'''
def main():
    print(green+"[+]"+yellow+" Choose one of the three options:"+options)
    num = raw_input(ask+"Select "+purple+"> ")
    while True:
        if (num=="1"):
            logoword= raw_input("\n"+ask+"Enter word(s) "+purple+"> ")
            if (logoword==""):
                print("\n"+error+"No Input")
                sleep(2)
                main()
            os.system("figlet "+logoword+" >> temp.txt")
            with open("temp.txt", 'r') as file1:
                logotext = file1.read()
                if (logotext==""):
                    print("\n"+error+"Error! Figlet not Installed.\n\n"+yellow+"[+] Install it by \"apt install figlet\"")
                    exit(1)
                os.system("rm -rf temp.txt")
                filename = raw_input("\n"+ask+"Output File Name "+purple+"> ")
                if (filename==""):
                    print("\n"+error+"No Input")
                    sleep(2)
                    main()
                os.system("rm -rf "+filename)
            writer(logotext,filename)
            exit()
        elif (num == "2"):
            logoword= raw_input("\n"+ask+"Enter word(s) "+purple+"> ")
            if (logoword==""):
                print("\n"+error+"No Input")
                sleep(2)
                main()
            os.system("toilet "+logoword+" >> temp.txt")
            with open("temp.txt", 'r') as file1:
                logotext = file1.read()
                if (logotext==""):
                    print("\n"+error+"Error! Toilet not Installed.\n\n"+yellow+"[+] Install it by \"apt install toilet\"")
                    exit(1)
                os.system("rm -rf temp.txt")
            filename = raw_input("\n"+ask+"Output File Name "+purple+"> " )
            if (filename==""):
                print("\n"+error+"No Input")
                sleep(2)
                main()
            os.system("rm -rf "+filename)
            writer(logotext,filename)
            break
        elif (num == "4"):
            logoword= raw_input("\n"+ask+"Enter word(s) "+purple+"> ")
            if (logoword==""):
                print("\n"+error+"No Input")
                sleep(2)
                main()
            os.system("cowsay "+logoword+" >> temp.txt")
            with open("temp.txt", 'r') as file1:
                logotext = file1.read()
                if (logotext==""):
                    print("\n"+error+"Error! cowsay not Installed.\n\n"+yellow+"[+] Install it by \"apt install toilet\"")
                    exit(1)
                os.system("rm -rf temp.txt")
            filename = raw_input("\n"+ask+"Output File Name "+purple+"> " )
            if (filename==""):
                print("\n"+error+"No Input")
                sleep(2)
                main()
            os.system("rm -rf "+filename)
            writer(logotext,filename)
            break       
        elif (num == "3"):
            logoword= raw_input("\n"+ask+"Enter word(s) "+purple+"> ")
            if (logoword==""):
                print("\n"+error+"No Input")
                sleep(2)
                main()
            slowprint(pw)
            try:
                 logotext = requests.get('https://artii.herokuapp.com/make?text='+logoword).text
                 filename = raw_input("\n"+ask+"Output File Name "+purple+"> ")
                 os.system("rm -rf "+filename)
                 writer(logotext, filename)
            except:
                print(error+"No Internet or empty input!")
                exit(1)
            break
        elif (num =="0"):
            exit()
        elif (num =="5"):
        	os.system("xdg-open --view https://github.com/kumarvicku?tab=repositories")
        else:
            print("\n"+error+"Error! Please choose right number!")
            time.sleep(2)
            main()
slowprint(logo)
main()
