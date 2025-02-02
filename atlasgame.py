import json
import random
import os
import create_pattern as cp
cp.word("atlas", "*")
print("______________________________________________________________________________________")
print("______________________________________________________________________________________ \n")
def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_data(filename):
    if not os.path.exists(filename):
        return {"p1": [], "p2": []}
    with open(filename, "r") as file:
        data = json.load(file)
        return data

def del_data(filename):
    with open(filename,"w") as f:
        json.dump({"p1":[], "p2":[]},f, indent=4)

def start_game():
    countries = [
        "Argentina", "Brazil", "Canada", "Denmark", "Egypt", "France", 
        "Germany", "Hungary", "India", "Japan", "Kenya", "Mexico", 
        "Nigeria", "Oman", "Peru", "Qatar", "Russia", "Spain", 
        "Turkey", "Uganda", "Vietnam", "Zimbabwe"
    ]
    
    p1name = input("Player 1, enter your name here: ")
    p2name = input("Player 2, enter your name here: ")
    print("__________________________________________________________")
    word = random.choice(countries)
    print(f"Your starting word is: {word}")
    print("__________________________________________________________")
    data = load_data("player.json")
    
    while True:
        lastword = word[-1].lower()
        player1 = input(f"({p1name}) Enter a country/city name that starts with ({lastword}): ")
        print("__________________________________________________________")
        p1word = player1[0].lower()
        
        if p1word == lastword:
            if player1.lower() in data["p1"] or player1.lower() in data["p2"]:
                print(f"The word ({player1}) has already been used.")
                print("__________________________________________________________")
            else:
                data["p1"].append(player1.lower())
                save_data(data, "player.json")
                word = player1  # Update the word for the next round
        else:
            print("You entered the wrong word. \n----- GAME OVER -----")
            print("__________________________________________________________")
            del_data("player.json")
            break
        
        lastword = word[-1].lower()
        player2 = input(f"({p2name}) Enter a country/city name that starts with ({lastword}): ")
        print("__________________________________________________________")
        p2word = player2[0].lower()
        
        if p2word == lastword:
            if player2.lower() in data["p1"] or player2.lower() in data["p2"]:
                print(f"The word ({player2}) has already been used.")
                print("__________________________________________________________")
                
            else:
                data["p2"].append(player2.lower())
                save_data(data, "player.json")
                word = player2  # Update the word for the next round
        else:
            print("You entered the wrong word. \n----- GAME OVER -----")
            print("__________________________________________________________")
            del_data("player.json")
            break

def restart():
    start_game()
    list=["yes","y","YES", "Yes"]
    while True:
            choice=input("do you want to restart ? (y/n):- ")
            if choice.lower() in list:
                start_game()
            else:
                print("---------- GAME OVER ---------")
                break
restart()