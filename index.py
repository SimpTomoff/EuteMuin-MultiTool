import base64
import os
os.system("title EuteMuin Multi Tool by SimpTom and scar17off")
current_path = os.path.dirname(os.path.realpath(__file__))
pats_path = current_path+"/pats/"
applications_path = current_path+"/applications/"
node_path = current_path+"/nodejs/"
from time import sleep
from colorama import Fore, Back, Style, init
#banners
eutemuin_multi_tool_banner = ''' _____      _       __  __       _          __  __       _ _   _
| ____|   _| |_ ___|  \\/  |_   _(_)_ __    |  \\/  |_   _| | |_(_)
|  _|| | | | __/ _ \\ |\\/| | | | | | '_ \\   | |\\/| | | | | | __| |
| |__| |_| | ||  __/ |  | | |_| | | | | |  | |  | | |_| | | |_| |
|_____\\__,_|\\__\\___|_|  |_|\\__,_|_|_| |_|  |_|  |_|\\__,_|_|\\__|_|

 _____           _
|_   _|__   ___ | |
  | |/ _ \\ / _ \\| |
  | | (_) | (_) | |
  |_|\\___/ \\___/|_|
'''
print(eutemuin_multi_tool_banner)
print(
'''
+=================================================================+
[1] Discord Token Fetcher
[2] EuteMuin Token Generator
[3] TerLeTzid Token Checker
[4] 8300 Discord Account Nuker
[5] Avery Discord Nuker
[6] Astaroth Discord Spammer cracked
[7] Lemon1337`s Discord Token Checker
[8] DiscordHaxx 2.1 ReMake by görenz#0001
[9] DiscordHaxx 1.9
+=================================================================+
''')

choice = input("Enter number: ")
if choice == "1":
	os.system("py "+pats_path+"discordtokenfetcher.py")
if choice == "2":
	os.system("py "+pats_path+"eutemuintokengenerator.py")
if choice == "3":
	os.system("py "+pats_path+"terletzidtokenchecker.py")
if choice == "4":
	os.system("py "+pats_path+"8300discordaccountnuker.py")
if choice == "5":
	os.system("start "+applications_path+"averynuker/avery.exe")
if choice == "6":
	os.system("start "+applications_path+"astarothdiscordspammer/AstarothSpammer Cracked By zFxbixn & Nichaen")
if choice == "7":
	os.system("start "+node_path+"/lemon1337sdiscordtokenchecker/install.bat")
	os.system("start "+node_path+"/lemon1337sdiscordtokenchecker/tokens.txt")
if choice == "8":
	os.system("start "+applications_path+"/discordhaxx19/OpenDiscordHaxx/bin/Debug/OpenDHBackend.exe")
	os.system("start "+applications_path+"/discordhaxx19/OpenDiscordHaxx/bin/Debug/tokens.txt")
	os.system("start "+applications_path+"/discordhaxx19/OpenDiscordHaxxUI/index.html")

else:
	print("Invalid choice. Try again.")
	os.system("py index.py")