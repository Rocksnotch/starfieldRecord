import json
import os
import io
import time
import constants as c

# Classes and etc

# Variables and etc

def clear():
    os.system('cls')

path = "planets.json"

planetTemplate = {
    "actualName":"",
    "type":"",
    "gravity":"",
    "temperature":"",
    "atmosphere":"",
    "magnetosphere":"",
    "fauna":[],
    "flora":[],
    "water":"",
    "resources":[],
    "traits":[],
    "habitable":"",
    "moons":{}
}
moonTemplate = {
    "actualName":"",
    "type":"",
    "gravity":"",
    "temperature":"",
    "atmosphere":"",
    "magnetosphere":"",
    "fauna":[],
    "flora":[],
    "water":"",
    "resources":[],
    "traits":[],
    "habitable":""
}

# Methods and etc

def header():
    clear()
    print(c.COLOR_ORANGE + "===Planet Tracker V0.1===")
    print(c.RESET)

def checkJson():
    if os.path.isfile(path) and os.access(path, os.R_OK):
        print("File found. Loading file.")
        time.sleep(1)
        with open(path, 'r') as json_file:
            db_file = json.load(json_file)
        print("File loaded. Sending to main menu.")
        time.sleep(1)
    else:
        print("File either missing or not readable. Creating new 'planets.json'.")
        time.sleep(1)
        with io.open(path, 'w') as db_file:
            db_file.write(json.dumps({"Systems":{}}, indent=2))
        with open(path, 'r') as json_file:
            db_file = json.load(json_file)
        print("File created. Sending to main menu.")
        time.sleep(3)
    return db_file

def printSystems():
    header()
    print("==All Systems Currently on File==")
    if len(planetJson["Systems"]) == 0:
        print("!!!No systems on file!!!\n")
    else:
        for idx, x in enumerate(planetJson["Systems"]):
            print(str(idx + 1) + ":", x)
        print("")
    input("Press Enter to continue...")
        
def addSystem():
    header()
    userSystem = input("Enter System name: ")
    systemLvl = input("Enter System level: ")
    if userSystem in planetJson["Systems"]:
        print("System already exists. Returning to menu.")
        time.sleep(2)
        printMenu()
    else:
        planetJson['Systems'][userSystem] = {"Level":systemLvl}
        with open(path, "w") as jsonFile:
            json.dump(planetJson, jsonFile, indent=2)
        print("System added to record. Returning to menu.")
        time.sleep(2)
        printMenu()

def addPlanet():
    printSystems()
    newPlanet = planetTemplate
    
    systemChoice = input("Enter entire System name to add planet to from above list: ")
    if systemChoice not in planetJson["Systems"]:
        print(c.COLOR_RED + "System does not exist. Please add system before attempting to enter planet." + c.RESET)
        input("Press Enter to continue...")
        return
    
    planetName = input("\nEnter Solar Name for Planet (Ex: Sol-I, Sol-II): ")
    
    if planetName in planetJson["Systems"][systemChoice]:
        print("Planet already exists. Returning to menu.")
        time.sleep(2)
        printMenu()
    else:
        planetJson['Systems'][systemChoice][planetName] = {}
        with open(path, "w") as jsonFile:
            json.dump(planetJson, jsonFile, indent=2)
    
    actualName = input("Enter ACTUAL Planet name (Ex: Jamison, Earth): ")
    planetType = input("Enter Planet type (Ex: Barren): ")
    planetGravity = input("Enter Planet Gravity (Ex: 0.15): ")
    planetTemp = input("Enter Planet temperature: ")
    planetAtmos = input("Enter Planet Atmosphere (Ex: Light N2): ")
    planetMag = input("Enter Planet Magnetosphere: ")
    faunaCheck = input("Are there fauna (Y/N): ").upper()
    if faunaCheck == 'Y':
        while True:
            faunaInput = input("Enter fauna name (NA to exit): ")
            if faunaInput == 'NA':
                break
            faunaResource = input("Enter Fauna resource: ")
            tempFauna = [faunaInput, faunaResource]
            newPlanet['fauna'].append(tempFauna)
    floraCheck = input("Are there flora (Y/N): ").upper()
    if floraCheck == 'Y':
        while True:
            floraInput = input("Enter fauna name (NA to exit): ")
            if floraInput == 'NA':
                break
            floraResource = input("Enter Fauna resource: ")
            tempFlora = [floraInput, floraResource]
            newPlanet['flora'].append(tempFlora)
    
    planetWater = input("Enter Planet Water Status (Ex: Safe): ")

    while True:
        resource = input("Enter Resource name (NA to exit): ")
        if resource == 'NA':
            break
        newPlanet['resources'].append(resource)
        
    while True:
        trait = input("Enter Planet traits (NA to exit): ")
        if trait == 'NA':
            break
        newPlanet['traits'].append(trait)
        
    planetHabitable = input("Is this planet habitable (True or False): ")
    
    newPlanet['actualName'] = actualName
    newPlanet['type'] = planetType
    newPlanet['gravity'] = planetGravity
    newPlanet['temperature'] = planetTemp
    newPlanet['atmosphere'] = planetAtmos
    newPlanet['magnetosphere'] = planetMag
    newPlanet['water'] = planetWater
    newPlanet['habitable'] = planetHabitable
    planetJson['Systems'][systemChoice][planetName] = newPlanet
    with open(path, "w") as jsonFile:
            json.dump(planetJson, jsonFile, indent=2)
        
def printMenu():
    while True:
        header()
        print("==Starfield System Tracker Menu==\n")
        print("1: Print all recorded systems")
        print("2: Print all Planets by System")
        print("3: Add System to Record")
        print("4: Add Planet to Record")
        print("5: Add Moon to Planet")
        print("0: Exit Program")
        userChoice = input("Choice: ")
    
        match userChoice:
            case '1':
                printSystems()
            case '3':
                addSystem()
            case '4':
                addPlanet()
            case '0':
                header()
                print("Thanks for using this program!")
                print("Any bugs or suggested features, please add to the GitHub!\n")
                input("Press Enter to exit program...")
                quit()
        
# Main code body here
header()
planetJson = checkJson() # Either load existing file or create new file on first run
printMenu()

