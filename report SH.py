
# --[ DECODED BY > https://t.me/termux_tools1 ]--
# --[ JOIN > https://t.me/termux_tools1 ]--
# --[ DECODE NOT FOR ENEMY - ITS ONLY EDUCATION ]--


import os
import sys
import itertools
import threading
import time
import signal
from colorama import Fore, Style
os.system('clear')
sys.stdout.write('\x1b]2;🍁TIKTOK REPORT</>SAKIBUL HASAN🔥\x07')
os.system('pip install ms4')
os.system('pip install dictionary')
os.system('pip install pystyle')
from pystyle import Colors, Colorate
from pystyle import Colors, Colorate
from pystyle import Write, Colors
from datetime import datetime
import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text
from ms4 import InfoTik  # Ensure InfoTik is correctly implemented in ms4
def animated (text) :
	for x in text :
		sys.stdout.write(x)
		sys.stdout.flush ( )
		time.sleep(0.005)
###----------[ COLOUR 1]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

###----------[ COLOUR 2 ]---------- ###
Z2 = "[#000000]" # HITAM #Black
M2 = "[#FF0000]" # MERAH  #Rad
H2 = "[#00FF00]" # HIJAU #Tiya Coular
K2 = "[#FFFF00]" # KUNING #Holod
B2 = "[#00C8FF]" # BIRU #Nill
U2 = "[#AF00FF]" # UNGU #Halka Begoni
N2 = "[#FF00FF]" # PINK #Begoni
O2 = "[#00FFFF]" # BIRU MUDA #Frash
P2 = "[#FFFFFF]" # PUTIH #White
J2 = "[#FF8F00]" # JINGGA #Koyri
A2 = "[#AAAAAA]" # ABU-ABU #Halka sada

os.system('clear')


logo = ("""
\t\033[38;5;46m         / __|  /\   | |/ /_   _|  _ \                             ____         _  _______ ____             
\t\033[38;5;46m      /     (___   /  \  | ' /  | | | |_) |    
\t\033[38;5;46m.    \___ \ / /\ \ |  <   | | |  _ <
\t\033[38;5;46m.  |_____/_/____\_\_|\_\_____|____/
\t\033[38;5;36m.  |______|______|______|______|______|______|
\t\033[38;5;46m                                      
                                                                                                                                                       

\033[1;91m\033[1;41m\033[1;97m              WELCOME TO TIK TOK AUTO REPORT  TOOLS               \033[;0m\033[1;91m\033[1;92m


\033[1;32m[-] TOOLS TYPE:\033[1;32m FREE
\033[1;32m[-] AUTHOR    :\033[1;32m SAKIB Hasan 
\033[1;32m[-] GITHUB    : SAKIB-SYVER 
\033[1;32m[-] FACEBOOK : Sakibul hasan 👿

""")
animated (logo)
                            
COLOR_DEFAULT = Style.RESET_ALL
COLOR_BLUE = Fore.BLUE
COLOR_MAGENTA = Fore.MAGENTA
COLOR_CYAN = Fore.CYAN
COLOR_GREEN = Fore.GREEN
COLOR_RED = Fore.RED
COLOR_YELLOW = Fore.YELLOW
ICON = "➤ "
ARRAY_ANIMATION = [    f"{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}    ",
    f" {COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}   ",
    f"  {COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_YELLOW}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}  ",
    f"   {COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON} ",
    f"    {COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_RED}{ICON}{COLOR_YELLOW}{ICON}{COLOR_MAGENTA}{ICON}"
]
class Spinner:
    def __init__(self, message):
        self.message = message
        self.stop_running = False
        self.thread = None
        self.animation_cycle = itertools.cycle(ARRAY_ANIMATION)
        self.columns = shutil.get_terminal_size().columns
    def start(self):
        self.stop_running = False
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()
    def _animate(self):
        while not self.stop_running:
            sys.stdout.write(f"\r{self.message} {next(self.animation_cycle)}")
            sys.stdout.flush()
            time.sleep(0.1)
    def stop(self, exit_status):
        self.stop_running = True
        if self.thread is not None:
            self.thread.join()      
        sys.stdout.write("\r" + " " * self.columns + "\r")
        sys.stdout.flush()
if __name__ == "__main__":
    import shutil
    Spinner = Spinner("\tLoading")
    Spinner.start()
    time.sleep(5) 
    Spinner.stop(0)
# Initialize variables
gg = 0
bb = 0
console = Console()

# Join Telegram group (Ensure this URL is correct)
os.system('xdg-open https://t.me/termux_tools1')

# Input target username
os.system('clear')
animated (logo)
print(" Example = @haker....")
user = input(f"ENTER TIK TOK TARGET ID : ")
info = InfoTik.TikTok_Info(user)
ip = requests.get("https://api.ipify.org").text
# Retrieve user info with error handling
try:
    nm = info.get('name', "")
    folo = str(info.get('followers', ""))
    following = str(info.get('following', ""))
    country = f"{info.get('country', '')} {info.get('flag', '')}"
    bio = info.get('bio', "")
    user_id = str(info.get('id', ""))
    private = str(info.get('private', ""))
    date = str(info.get('Date', ""))
    likes = str(info.get('like', ""))
    Ip = str(info.get('{Ip}', ""))
    
except KeyError as e:
    console.print(f"Missing expected field: {e}", style="bold red")

def killman():
    # Example implementation; adjust as needed
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

def base_params():
    # Example implementation; adjust as needed
    return {
        "param1": "value1",
        "param2": "value2"
    }

def Report():
    global gg, bb
    url = "https://api16-normal-c-alisg.ttapis.com/aweme/v2/aweme/feedback/"
    headers = killman()
    params = base_params()
    try:
        res = requests.get(url, params=params, headers=headers)
        if '"status_code":0,"status_message":""' in res.text:
            os.system('clear')
            gg += 1
        else:
            os.system('clear')
            bb += 1
    except requests.RequestException as e:
        console.print(f"Request error: {e}", style="bold red")
os.system('clear')        
animated (logo)  
                                                                                              
def display_report():
    total = gg + bb
    table = Table(title="TIKTOK REPORT")
    table.add_column("Type", justify="center", style="cyan", no_wrap=True)
    table.add_column("Count", justify="center", style="magenta")
    table.add_row("Good Report", Text(str(gg), style="green"))
    table.add_row("Bad Report", Text(str(bb), style="red"))
    table.add_row("Total", Text(str(total), style="yellow"))
    table.add_row("Dev", "https://t.me/termux_tools1")
    table.add_row("User", Text(user, style="cyan"))
    table.add_row("Name", Text(nm, style="cyan"))
    table.add_row("Followers", Text(folo, style="green"))
    table.add_row("Following", Text(following, style="yellow"))
    table.add_row("Country", Text(country, style="blue"))
    table.add_row("Bio", Text(bio, style="magenta"))
    table.add_row("ID", Text(user_id, style="cyan"))
    table.add_row("Private", Text(private, style="red" if private == "True" else "green"))
    table.add_row("Date", Text(date, style="magenta"))
    table.add_row("Likes", Text(likes, style="green"))
    table.add_row("Ip", Text(Ip, style="green"))
    console.print(table)

# Main loop
while True:
    try:
        Report()
        display_report()
    except Exception as e:
        console.print(f"Error reporting: {e}", style="bold red")
        


# --[ DECODED BY > https://t.me/termux_tools1]--
# --[ JOIN > https://t.me/termux_tools1 ]--
# --[ DECODE NOT FOR ENEMY - ITS ONLY EDUCATION ]--

