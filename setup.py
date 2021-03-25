from setuptools import setup
import os, time
from utils import *

os.system("cls" if os.name == "nt" else "clear")

def installDepen():
    print("\tInstalling...")
    InstallationError = "\tThere was an error when installing dependencies.\n\tIf you can code then look at the code, if you can't code then contact a\n\tprogrammer.\n"
    #try:
        with open("requirements.txt") as f:
            required = f.read().splitlines()
        setup(install_requires=required)
    #except:
    #    print(InstallationError)

def jailbreak():
    print("Jailbreaking...")

def userUI():
    print("""

    \tWelcome To Roshan's Jailbreak.\n\tLet's start breaking stuff :)
    \tChoose one of the following options:\n\t[1]: Install the dependencies\n\t[2]: Start the jailbreak process.
""")

    userInput = int(input("\t"))

    if userInput == 1:
        installDepen()    
    elif userInput == 2:
        jailbreak()
    else:
        pass

userUI()