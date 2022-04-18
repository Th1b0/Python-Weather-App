import requests
from dotenv import load_dotenv
import os
from city import *
from cords import *
from clear import *
from tabulate import tabulate

load_dotenv()
URL = os.getenv("URL")
API_KEY = os.getenv("APIKEY")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
LOGO = """


░██╗░░░░░░░██╗███████╗░█████╗░████████╗██╗░░██╗███████╗██████╗░░░░██████╗░██╗░░░██╗
░██║░░██╗░░██║██╔════╝██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗░░░██╔══██╗╚██╗░██╔╝
░╚██╗████╗██╔╝█████╗░░███████║░░░██║░░░███████║█████╗░░██████╔╝░░░██████╔╝░╚████╔╝░
░░████╔═████║░██╔══╝░░██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗░░░██╔═══╝░░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░███████╗██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██╗██║░░░░░░░░██║░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░
  

            █▄▄ █▄█     ▀█▀ █░█ █ █▄▄ █▀█
            █▄█ ░█░     ░█░ █▀█ █ █▄█ █▄█                        
                                                                                 
"""

print(f"{bcolors.OKCYAN}{LOGO}{bcolors.ENDC}")

def main():
    text = f"""{bcolors.OKCYAN}What do you want to do?
        
        1. Search the weather for specific cordinates
    
        2. Search the weather for a specific city
        
    """
    
    table = [[text]]
    output = tabulate(table, tablefmt='grid')

    print(f"{bcolors.OKCYAN}{output}")
    api_choice = input("\nInput 1/2: ")
    if api_choice == "1":
        cords()
    elif api_choice == "2":
        city()
    else:
        clearConsole()
        print(f"{bcolors.OKCYAN}{LOGO}{bcolors.ENDC}")
        input("Not a valid option try again...(press key to continue)")
        main()


def test():
    lat = 1
    lon = 1
    response = requests.get(f'{URL}?lat={lat}&lon={lon}&appid={API_KEY}').status_code
    if response == 200:
        main()
    else:
        print(f"{bcolors.OKCYAN}{LOGO}{bcolors.ENDC}")
        input(f'connection error with status code {response} try again later or contact the author...(press any key to close')
test()