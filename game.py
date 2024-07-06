from rich.console import Console
from rich.table import Table
import pygame
import random
import time
import sys

console = Console()
pygame.init()
pygame.mixer.music.load('.\music.mp3')
pygame.mixer.music.play()

print("\n")
table = Table(title="Start Menu")
player_Table = Table(title="")
action_Table = Table(title="Plan")
hit_Table = Table(title="Powers")
heal_Table = Table(title="")

table.add_column("CANOPY CHAOS", style="green")
table.add_row(" | Start", style="bold")
table.add_row(" | Quit", style="bold")

action_Table.add_column("PLANS", style="green")
action_Table.add_row(" 1 -> Try to Start the Plane")
action_Table.add_row(" 2 -> Move Through the Jungle ")

hit_Table.add_column("INVENTORY", style="red")
hit_Table.add_row("1 -> Use your Rifle [-50]")
hit_Table.add_row("2 -> Use Dagger [-25]")

heal_Table.add_column("WILD HERBS", style="green bold")
heal_Table.add_row("1 -> NATIVE CRATOS")
heal_Table.add_row("2 -> WILD LUCAS")

console.print(table)

timer_Delay = 1
user_Name = ""
user_Choice = ""
user_Choice2 = ""
user_Choice3 = ""
health_User = 100
health_Monster = 100
health_Variable = [10, 30]
entry_Input = input("Enter your choice : ")
refined_entry_Input = entry_Input.lower()

def player_Killed():
    console.print("You have died....", style="italic red")

def engine_Exploded():
    console.print("Engine expolded and You Have Died....", style="italic red")

def see_Monster():
    console.print("\nYou See a Huge Jungle Monster",style="red italic")
    printable_Img = "───▄█▌─▄─▄─▐█▄\n───██▌▀▀▄▀▀▐██\n───██▌─▄▄▄─▐██\n───▀██▌▐█▌▐██▀\n▄██████─▀─██████▄"
    console.print(printable_Img, style="red")

def continuation():
    console.print("You Walk through the Jungle....", style="green italic")

def GameOver():
    console.print("GAME OVER", style="bold red")

def endOfGame():
    console.print("GAME FINISHED...", style="bold")
    console.print("Credits : Adithya P S", style="bold")



if refined_entry_Input == "start":
    console.print("Hi Lone Warrior, What's your Name? ", style="italic green")
    user_Name = input("Enter your Name : ")
    player_Table.add_column("Player One Ready", style="italic red")
    player_Table.add_row(user_Name)
    console.print(player_Table)
    time.sleep(timer_Delay)
    console.print("Ha! So You've Come my Dear,", user_Name, style="italic green")
    time.sleep(timer_Delay)
    console.print("We have been stranded in this godforsaken jungle of weird things", style="italic green")
    time.sleep(timer_Delay)
    console.print(" | Escape\n | Die\n", style="bold green")
    user_Choice = input("Enter your Choice : ")
    user_Choice.lower()
    refined_user_choice = user_Choice.lower()
    time.sleep(timer_Delay)
    if user_Choice == "escape":
        console.print("You are indeed a fighter!", style="italic green")
        time.sleep(timer_Delay)
        console.print("What's our Plan of Action?", style="italic green")
        time.sleep(timer_Delay)
        console.print(action_Table)
        time.sleep(timer_Delay)
        user_Choice2 = input("Enter your Plan : ")
        if user_Choice2 == "1":
            engine_Exploded()
        elif user_Choice2 == "2":
            console.print("Walking through the Dense Jungle", style="italic green")
            time.sleep(timer_Delay)
            console.print("Oh NO!!..", style="italic red")
            time.sleep(timer_Delay)
            see_Monster()
            console.print("You Check your Inventory....", style="italic green")
            time.sleep(timer_Delay)
            console.print(hit_Table)
            # monster has 2 powers fire ball [-50] and hit [-25]
            while health_User > 0 or health_Monster > 0:
                user_Choice3 = input("Enter Attack : ")
                if user_Choice3 == "1":
                    health_Monster = health_Monster - 51
                    console.print("Monster Health is",health_Monster,style="italic green" )
                    user_Health = random.choice(health_Variable)
                    health_User = health_User - user_Health
                    console.print("User Health is", health_User, style="italic green")
                    if health_Monster < 0:
                        console.print("HAHAHAH!!", style="bold green")
                        time.sleep(timer_Delay)
                        console.print("You have Defeated JONGLE!!..", style="italic green")
                        continuation()
                        break
                    elif health_User < 0:
                        console.print("NO..No...no..argghh", style="bold red")
                        time.sleep(timer_Delay)
                        console.print("GOODBYE", style="italic red")
                        GameOver()
                        sys.exit()
                else:
                    health_Monster = health_Monster - 26
                    console.print("Monster Health is",health_Monster,style="italic green" )
                    user_Health = random.choice(health_Variable)
                    health_User = health_User - user_Health
                    console.print("User Health is", health_User, style="italic green")
                    if health_Monster < 0:
                        console.print("HAHAHAH!!", style="bold green")
                        time.sleep(timer_Delay)
                        console.print("You have Defeated JONGLE!!..", style="italic green")
                        continuation()
                        break
                    elif health_User < 0:
                        console.print("NO..No...no..argghh", style="bold red")
                        time.sleep(timer_Delay)
                        console.print("GOODBYE", style="bold red")
                        GameOver()
                        sys.exit()
        else:
            console.print("Enter Valid Input", style="red bold")
        time.sleep(timer_Delay)
        console.print("Oh no!.. I've been Hurt!!", style="bold red")
        time.sleep(timer_Delay)
        console.print(heal_Table)
        time.sleep(timer_Delay)
        healInput = int(input("What do you Want? : "))
        console.print("Applying herbs...", style="italic green")
        if healInput == 1:
            console.print("NO..NO...no.no", style="bold red")
            time.sleep(2)
            console.print("This is Poisonousss!!!", style="bold red")
            GameOver()
            sys.exit()
        else:
            console.print("OH...Now I Feel Better..", style="bold green")
            console.print("Let me Sleep for a while Now...",  style="bold green")
            time.sleep(timer_Delay)
            console.print("ZZZzzz", style="green italic")
            time.sleep(2)
            console.print("Arhhhhh..Good Morning to ME!", style="green bold")
        console.print("YOU SEE HUGE STRUCTURES NEAR A CRATER...", style="bold cyan")
        console.print("You walk near to the crater..", style="italic green")
        time.sleep(timer_Delay)
        console.print("The ground beneath Alex’s feet feels uneven, the roots of ancient trees sprawling like gnarled fingers. Birds and insects hum in the background, a symphony of the jungle. As he approaches the crater, a sudden rustling in the foliage halts him in his tracks", style="italic green")
        console.print("A SNAKE!!!", style="bold red")
        time.sleep(timer_Delay)
        printable_Img2 = "⣀⡀⠀⣀\n⢠⣴⣾⡿⠿⠿⠿⠷⠦⠿⠿\n⠉⡉⠛⢠⣾⣷⡀⠰⣦\n⠸⠇⣈⣀⣀⣀⣀⠈⠂\n⠲⣶⡄⠘⠛⠛⠛⠛\n⠙⢷⡀⠻⣿⠿⠿\n⠉⢴⣶⣶⡄\n⠉⢁⣤⣤⡀\n⠛⠋⣉\n⠸⣿⣿⣷\n⣀⣠⣤⣶⠶⠶⠟⠛⠛⠛⠋⠁⣿⣿⣿⣧\n⠰⣿⣿⠷⠶⠶⠿⠿⠿⠿⠿⠿⠿⠿⠿⢁⣿⣿⣿⣿⠀⠿⢛⣻⡆\n⣠⣤⣤⣤⣶⣶⣶⣶⣶⡶⠶⠖⠒⢀⣤⣾⣿⣿⣿⡟⢀⣾⣿⡿⠃\n⠘⠿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⡿⠿⠋\n⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁"
        console.print(printable_Img2, style="red")
        health_Monster = 100
        health_User = 100
        console.print("You Check your Inventory....", style="italic green")
        time.sleep(timer_Delay)
        console.print(hit_Table)
        while health_User > 0 or health_Monster > 0:
                user_Choice3 = input("Enter Attack : ")
                if user_Choice3 == "1":
                    health_Monster = health_Monster - 51
                    console.print("Monster Health is",health_Monster,style="italic green" )
                    user_Health = random.choice(health_Variable)
                    health_User = health_User - user_Health
                    console.print("User Health is", health_User, style="italic green")
                    if health_Monster < 0:
                        console.print("HAHAHAH!!", style="bold green")
                        time.sleep(timer_Delay)
                        console.print("You have Defeated SERPENTINE!!..", style="italic green")
                        continuation()
                        break
                    elif health_User < 0:
                        console.print("NO..No...no..argghh", style="bold red")
                        time.sleep(timer_Delay)
                        console.print("GOODBYE", style="italic red")
                        GameOver()
                        sys.exit()
                else:
                    health_Monster = health_Monster - 26
                    console.print("Monster Health is",health_Monster,style="italic green" )
                    user_Health = random.choice(health_Variable)
                    health_User = health_User - user_Health
                    console.print("User Health is", health_User, style="italic green")
                    if health_Monster < 0:
                        console.print("HAHAHAH!!", style="bold green")
                        time.sleep(timer_Delay)
                        console.print("You have Defeated SERPENTINE!!..", style="italic green")
                        continuation()
                        break
                    elif health_User < 0:
                        console.print("NO..No...no..argghh", style="bold red")
                        time.sleep(timer_Delay)
                        console.print("GOODBYE", style="bold red")
                        GameOver()
                        sys.exit()


        
    


    else:
        player_Killed()

