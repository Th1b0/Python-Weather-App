import requests
from dotenv import load_dotenv
import os
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
def city():
    clearConsole()
    print(f"{bcolors.OKCYAN}{LOGO}{bcolors.ENDC}")
    text = """Input a name of a city
    
    Example:
    
    London, New York, Genk"""
    table = [[text]]
    output = tabulate(table, tablefmt='grid')
    print(f"{bcolors.OKCYAN}{output}")
    city = input("\nInput city name: ")
    clearConsole()
    print(f"{bcolors.OKCYAN}{LOGO}{bcolors.ENDC}")
    text = """Choose which units of measurement you want to use.
    
    Metric
    
    Imperial
    \xa0
    """
    table = [[text]]
    output = tabulate(table, tablefmt='grid')
    print(f"{bcolors.OKCYAN}{output}")
    system = input(f"{bcolors.OKCYAN}\nInput Metric/Imeperial: ").lower()
    
    if system != "metric" and system != "imperial":
        input(f"{bcolors.OKCYAN}Not a valid option try again...(press any key to continue)")
        clearConsole()
        city()
    else:
        clearConsole()
        REQUEST_URL = f'{URL}?q={city}&units={system}&appid={API_KEY}'
        print(REQUEST_URL)
        response = requests.get(REQUEST_URL)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]['description']
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            deg = data["wind"]["deg"]
            clearConsole()
            print(f"{bcolors.OKCYAN}{LOGO}{bcolors.ENDC}")
            
            text = f"""The weather in {city} is:
            
    Weather
    
        {weather}
        
        The tempeture is {temp}
        
        Feels like {feels_like}
        
        Minimum Temperture is {temp_min}
        
        Maximim temperture{temp_max}
        
        The pressure is {pressure}
        
        The hummudity is {humidity}
        
        The wind speed is {wind}
        
        """
            table = [[text]]
            output = tabulate(table, tablefmt='grid')
            print(f"{bcolors.OKCYAN}{output}")
            input(f"{bcolors.OKCYAN}\nPress any key to close...")
        else:
            clearConsole()
            input(f'There has been an error. Status code {response.status_code}. Did you type the city name correct?')


