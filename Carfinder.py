# Register Dependencies
import time

# Program Start

def displayVehicles():
 print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
 file = open("availablevehicles.txt", "r")
 fileContents = file.read()
 print(fileContents)
 print("Returning to the Main Menu in 5 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu in 4 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu in 3 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu in 2 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu in 1 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu now...")
 time.sleep(1)
 menu()

def addVehicle():
 file = open("availablevehicles.txt", "a")
 carAdd = input("Enter your Vehicle Name: ")
 file.write("\n" + carAdd) 
 file.flush()
 print(carAdd + " is now an Authorized Vehicle. Returning to the Main Menu in 5 Seconds...")
 time.sleep(1)
 print("Returning to the Main Menu in 4 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu in 3 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu in 2 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu in 1 seconds...")
 time.sleep(1)
 print("Returning to the Main Menu now...")
 time.sleep(1)
 menu()

def searchForVehicles():
 Search = input("Search: ")
 file = open("availablevehicles.txt", "r")
 filecontent = file.readlines()
 SearchSuccessful = False
 for line in filecontent:
  if Search in line.lower():
     SearchSuccessful = True
     print(line)
     time.sleep(3)
     menu()
  if line.find(Search) != -1:
     SearchSuccessful = True
     print(line)
     time.sleep(3)
     menu()

 if SearchSuccessful == False:
  print(Search, "is not an authorized vehicle. Please try again...") 
  time.sleep(3)
  menu()

def menu():
 print("************************************")
 print("  AutoCountry Vehicle Finder v0.3")
 print("************************************")
 print("Please select one of the following numbers from the menu below:")

 print("1: PRINT all Authorized Vehicles")
 print("2: SEARCH all Authorized Vehicles")
 print("3: ADD Authorized Vehicle")
 print("4: Exit")
 menuSelection = int(input("Your Selection: "))
 
 if menuSelection == int("1"):
  displayVehicles()

 if menuSelection == int("2"):
  searchForVehicles()

 if menuSelection == int("3"):
  addVehicle()

 if menuSelection == int("4"):
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    exit()
menu()

# Program Complete. 
