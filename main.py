import os

os.system("pip install colorama")
from colorama import Fore, Back, Style
from time import sleep, strftime, localtime
from getpass import getpass
import requests

loop = True
userToken = ""

def teminToken(user):
    userApi_url = f"https://discord.com/api/v9/users/@me/guilds"
    userToken = user
    header = {"Authorization": f"{userToken}"}
    response = requests.get(userApi_url, headers=header)
    data = response.json()
    userObj = data
    n = 0
    for eny in userObj:
        n += 1
        guild_id = eny["id"]
        guild_name = eny["name"]
        print(f'{Fore.MAGENTA}[{n}] Name: {guild_name}{Style.RESET_ALL}')
        userChannel(guild_id, userToken, n)
    print(f"\n{Fore.GREEN}Server Get Count ({n})")
    showInput()

def userChannel(id, user, num):
    ch_url = f"https://discord.com/api/v9/guilds/{id}/emojis"
    emoji_url = f"https://cdn.discordapp.com"
    header = {"Authorization": f"{user}"}
    response = requests.get(ch_url, headers=header)
    data = response.json()
    userCh = data
    line = 0
    for eny in userCh:
        line += 1
        emoji_id = eny["id"]
        emoji_anim = eny["animated"]
        if emoji_anim:
           print(f"{Fore.CYAN}[{num}] {Fore.WHITE}Type: {Fore.RED}GIF")
        else:
           print(f"{Fore.CYAN}[{num}] {Fore.WHITE}Type: PNG")

        print(f"{Fore.CYAN}[{num}]{Fore.YELLOW} emoji id: {emoji_id}")
        if emoji_anim:
           print(f"{Fore.CYAN}[{num}]{Fore.YELLOW} emoji URL: {Fore.WHITE}{emoji_url}/emojis/{emoji_id}.gif?v=1{Fore.YELLOW}")
        else:
           print(f"{Fore.CYAN}[{num}]{Fore.YELLOW} emoji URL: {Fore.WHITE}{emoji_url}/emojis/{emoji_id}.png?v=1{Fore.YELLOW}")
        print(f"{Fore.CYAN}[{num}]{Fore.GREEN} Item: {line}")


def showInput():
    # Use getpass to hide the input
    choice = getpass(f"{Fore.MAGENTA}{strftime('%H:%M.%S', localtime())} | token: ")
    if not choice.lower().startswith("exit"):
       teminToken(choice)
    else:
       loop = False
       print(f"{Fore.RED}EXIT !")



if __name__ == "__main__":
   print("Success")
   showInput()
