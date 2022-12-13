import random
import time
import sys
import tkinter
import replit
from replit import db
legendary_banana=0
player_health=200
player_damage = 10
player_speed = 10
max_player_health = 200

golden_taco=0
legendary_herb=0
platinum_nut=0
noice_bacon=0
keys = 0

print("You find yourself washed up on an island and the group of people that live there nurses you back to health. If you want to join their tribe, you have to complete three tasks")

time.sleep(3)
print ("You wake up on saturday morning and head out to do your first task. It is to go into a maze and destroy the monster crytal that keeps on spawning monsters.")
time.sleep(3)
print("You go into the maze.")
health_potion = 1
attack_potion=1
speed_potion= 1
max_health_potion = 1
max_player_health = 200
player_health = 200
player_damage = 10
player_speed = 20
def fight_troll(player_health, player_damage,player_speed):
  troll_health = 250
  troll_attack= 10
  troll_speed = 0
  print("You encountered a troll.")
  if (player_speed >= pig_speed):
    turn = 1
  else:
    turn = 0
  while pig_health >0 and player_health > 0:
    if turn == "1":
      print("What do you do?")
      print("1.Attack")
      print("2. Run away")
      answer = input()
      if answer == "1":
        pig_health-= int(player_damage)
        print("The pig's health is:"+int(pig_health))
      if  pig_health >= 0:
        return True
      elif answer == "2":
        bob3=rand.randint(1,5)
        if bob3!=1:
          turn = 0
        if bob3==1:
          turn=0
          return False
          print("You died.")
          break
      elif turn == 0:
        player_health -= bear_damage
        print("Your health is:" + player_health)
def fight_pig(player_health, player_damage,player_speed):
  pig_health = 120
  pig_attack= 50
  pig_speed = -1
  print("You encountered a karate pig.")
  if (player_speed >= pig_speed):
    turn = 1
  else:
    turn = 0
  while pig_health >0 and player_health > 0:
    if turn == "1":
      print("What do you do?")
      print("1.Attack")
      print("2. Run away")
      answer = input()
      if answer == "1":
        pig_health-= int(player_damage)
        print("The pig's health is:"+int(pig_health))
      if  pig_health >= 0:
        return True
      elif answer == "2":
        bob3=rand.randint(1,5)
        if bob3!=1:
          turn = 0
        if bob3==1:
          turn=0
          return False
          print("You died.")
          break
      elif turn == 0:
        player_health -= bear_damage
        print("Your health is:" + player_health)

  
def fight_black_bear(player_health, player_damage,player_speed):
  bear_health = 240
  bear_attack= 10
  bear_speed = 20
  print("You encountered a black bear.")
  if (player_speed >= bear_speed):
    turn = 1
  else:
    turn = 0
  while bear_health >0 and player_health > 0:
    if turn == "1":
      print("What do you do?")
      print("1.Attack")
      print("2. Run away")
      answer = input()
      if answer == "1":
        bear_health -= int(player_damage)
        print("The Bear's health is:"+int(bear_health))
      if  bear_health >= 0:
        return True
      elif answer == "2":
        bob3=rand.randint(1,5)
        if bob3!=1:
          turn = 0
        if bob3==1:
          turn=0
          print("You died.")
          return False
      elif turn == 0:
        player_health -= bear_damage
        print("Your health is:" + player_health)



def fight_DEMON_MONKEY(player_health, player_damage,player_speed):
  print("A demon moke jumps out of a trash can! it snarles and charges!")
  
  demon_health = 150
  demon_attack= 35
  demon_speed = 5
  if ( player_speed >=  demon_speed):
    turn = 1
    
  else:
    turn = 0
  while demon_health > 0 and player_health > 0:
    if turn == 1:
      print("What do you do?")
      print("1. Attack")
      print("2. Run away")
      answer = input()
      if answer == "1":
        demon_health -= int(player_damage)
        print("The Monkey's health is:"+int(demon_health))
      if  demon_health >= 0:
        return True
      elif answer == "2":
        bob3=rand.randint(1,5)
        if bob3!= 1:
          turn = 0
        if bob3== 1:
          return False
      elif turn == 0:
        player_health -= demon_damage
        print("Your health is:" + player_health)
#--------------------------------------
def fight_Werewolf(player_health, player_damage,player_speed):
  print("A werewolf snarles and lumbers twoard you!")
  werewolf_health = 120
  werewolf_attack= 20
  werewolf_speed = 70
  if ( player_speed >=  werewolf_speed):
    turn = 1
  else:
    turn = 0
  while werewolf_health > 0 and player_health > 0:
    if turn == 1:
      
      print("What do you do?")
      print("1. Attack")
      print("2. Run away")
      answer = input()
      if answer == "1":
        werewolf_health -= int(player_damage)
        print("Werewolf health is:"+str(werewolf_health))
      if  werewolf_health <= 0:
        return True
      elif answer == "2":
        bob3=rand.randint(1,3)
        if bob3!= 1:
          turn = 0
        if bob3== 1:
          return False
    elif turn == 0:
      player_health -= werewolf_damage
      print("Your health is:" + str(player_health))
#-------------------------------------- NEED TO CHANGE
def fight_dragon(player_health, player_damage,player_speed):
  print("Charelene and roxy, 2 origami masters, folds a dragon and tell it to kill you.")
  werewolf_health = 120
  werewolf_attack= 20
  werewolf_speed = 70
  if ( player_speed >=  werewolf_speed):
    turn = 1
  else:
    turn = 0
  while werewolf_health > 0 and player_health > 0:
    if turn == 1:
      
      print("What do you do?")
      print("1. Attack")
      print("2. Run away")
      answer = input()
      if answer == "1":
        werewolf_health -= int(player_damage)
        print("Werewolf health is:"+str(werewolf_health))
      if  werewolf_health <= 0:
        return True
      elif answer == "2":
        bob3=rand.randint(1,3)
        if bob3!= 1:
          turn = 0
        if bob3== 1:
          return False
    elif turn == 0:
      player_health -= werewolf_damage
      print("Your health is:" + str(player_health))
#-----------------------------------------------------
def health_potion(player_health, max_player_health):
  if player_health > max_player_health-10: 
    print("You are not in contdition to use this potion.") 
  elif player_health <= max_player_health-10:
    print("You have used the potion")
    player_health = player_health + 10
    print("Your current health:"+str(player_health))
def attack_potion(player_damage):
  attack_potion = int(player_damage) + 3
  print("Your damage:"+str(player_damage))
def speed_potion(player_speed): 
  speed_potion = int(player_speed) + 5
  print("Your speed:"+str(player_speed))
def max_health_potion(max_player_health):
  player_health = max_player_health
  print("Your maximum amount of health:"+ str(max_player_health))
#------------------------------------------
def use_potions():
  print("would you like to use potions, (h for health,a for attack, s for speed,and m for max health potion.)")
  bob = input()
  if bob == "h" and health_potion != 0:
    health_potion()  
    health_potion-= 1    
  if bob == a and attack_potion != 0:
    attack_potion()
  
  if bob == s and speed_potion != 0:
    speed_potion()
  if bob == m and ma: 
    max_health_potion()
#-------------------------------------
#functions
def boss():
  replit.clear()
  print("           ")
  time.sleep(0.2)
  replit.clear()
  print("|         |")
  time.sleep(0.2)
  replit.clear()
  print("||       ||")
  time.sleep(0.2)
  replit.clear()
  print("|||     |||")
  time.sleep(0.2)
  replit.clear()
  print("||||   ||||")
  time.sleep(0.2)
  replit.clear()
  print("||||| |||||")
  time.sleep(0.2)
  replit.clear()
  print("|||||||||||")
  time.sleep(0.2)
  replit.clear()
  print("|||||f|||||")
  time.sleep(0.2)
  replit.clear()
  print("|||s fi||||")
  time.sleep(0.2)
  replit.clear()
  print("||ss figh||")
  time.sleep(0.2)
  replit.clear()
  print("|oss fight|")
  time.sleep(0.2)
  replit.clear()
  print("boss fight!")
  time.sleep(0.2)

def fight_Smaug(player_health, player_damage,player_speed,print1, print2):
  print(str(print1)) 
  demon_health = 100
  demon_attack= 20
  demon_speed = -1000
  if ( player_speed >=  demon_speed):
    turn = 1
    
  else:
    turn = 0
  while demon_health > 0 and player_health > 0:
    if turn == 1:
      print("What do you do?")
      print("1. Attack")
      print("2. Run away")
      answer = input()
      if answer == "1":
        demon_health -= int(player_damage)
        print(str(print2)+str(demon_health))
      if  demon_health >= 0:
        return True
      elif answer == "2":
        bob3=rand.randint(1,5)
        if bob3!= 1:
          turn = 0
        if bob3== 1:
          return False
      elif turn == 0:
        player_health -= demon_damage
        print("Your health is:" + player_health)  
def fight_Dark_Commander(player_health, player_damage,player_speed):
  print("A dark commander is waiting. he unsheathes his sword and brandishes it skillfully!")
  Dark_Commander_health = 20
  Dark_Commander_damage = 45
  Dark_Commander_speed = 30
  if (player_speed >= Dark_Commander_speed):
    turn = 1
  else:
    turn = 0
    print("The your health is:"+str(player_health))
  while Dark_Commander_health > 0and player_health > 0:
    if turn == 1:
      print("What do you do?")
      print("1.Attack")
      print("2.Run away")
      answer = input()
      if answer == "1":
        Dark_Commander_health -= int(player_damage)
        print("The Dark commander's health is:") + str(Dark_Commander_health)
        if Dark_Commander_health <=0:
          return True
      elif answer == "2":
        bob3=random.randint(1,5)
        if bob3!=1:
          turn = 0
        if bob3==1:
          return False
      elif turn == 0:
        player_health -= Dark_Commander_damage()
        print("Your health is:" + player_health)


#_________________________________________
#while true loop ||
#               _||_
#               \||/
#                \/ 


while True:
  kills = 0
  if kills == 8:
    break
  print("There are two doors.")
  input(int("type 1 for the first door and 2 for the second door."))
  door_one = [1,1,1,3,2,3]
  door_two = []
  choice = input()
  if bob == "1":
    kill = fight_troll(player_health, player_damage,player_speed)
    if kill:
      kills+= 1
  if bob == "3":
    kill = fight_Werewolf(player_health, player_damage,player_speed)
    if kill:
      kills += 1
  if choice == "2":
    print("You found a trader! He offers you a healing potion, a sharper sword, or a speed potion.")
    print("Type in h for the potion, w for a sharper sword, and s for a speed potion.")
    thing = input()
    if thing == "w":
      player_damage += 10
      print("your damage: " + str(player_damage))
      
    if thing == "h":
      player_health += 5
    if thing == "s":
      player_speed+=3
      print("your speed:"+ str(player_speed))
    

print("You find the dragon of legends, Smaug curled around the crystal, lying on a mountain of treasure! You try to sneak past, but he wakes up from his slumber, ready to fight!")
#boss()
win = fight_Smaug(player_health, player_damage,player_speed,"Smaug roars! he toys with you, testing your strength", "Smaug's health is:")

if win == True:
  print("You defeat Smaug, destroy the crystal with a few hits of your sword, and bring a scale back as proof You also find the holy golden taco. The natives are delighted and hold a great feast!")
  golden_taco += 1
  
  print("""\ \  / / /------\  __  __    __            __  _______   ___   __
 \ \/ /  |  __  | | |  | |   \ \    __    / / |_______| |   \  | |
  \  /   | |  | | | |  | |    \ \  /  \  / /     | |    | |\ \ | |
  |  |   | \--/ | | |__| |     \ \/ /\ \/ /   ___| |___ | | \ \| |
  |__|   \______/ \______/      \__/  \__/    |_______| | |  \  / """)
else:
  print("You fail to slay him and became Smaug's lunch.")
  print("""\ \  / / /------\  __  __     __      /------\   _______  _______
 \ \/ /  |  __  | | |  | |    | |     |  __  |  / _____| |__   __|
  \  /   | |  | | | |  | |    | |     | |  | |  |_____ \    | |
  |  |   | \--/ | | |__| |    | |___  | \--/ |   _____\ \   | |
  |__|   \______/ \______/    |_____| \______/  |_______/   |_|""")
print("You wake up at the tribe as they order you to get the other ingredients to kill a new plauge, the great mortality.")
werewolf=fight_Werewolf(player_health, player_damage,player_speed)
if werewolf == True:
  print("You find the legendary herb of life that treats the disease, the great mortality.")
  time_sleep(0.3)
  werewolf_choice=input("The werewolf drops a fang, a large speed potion, and a werewolf skin cape.( f for the fang, l for the potion, and w for the armor)")
  legendary_herb+=1
  if werewolf_choice == "f":
    player_damage += 5
  if werewolf_choice == "l":
    player_speed += 10
  if werewolf_choice == "w":
    max_player_health += 20
  if werewolf_choice == "boba":
    player_damage += 100
    player_speed += 100
    max_player_health += 100
    player_health = max_player_health
    EndText = ("Cheat code confirmed\n-------------")
    for char in EndText:
      time.sleep(0.05)
      sys.stdout.write(char)
      sys.stdout.flush()
  legendary_herb+=1
  
else:
  print("You lost")


monkey=fight_DEMON_MONKEY(player_health,player_damage,player_speed)
if monkey == True:
  print("You have defeated the monkey and stole the legendary banana.")
  legendary_banana+=1
else:
  print("You lost")
blackbear=fight_black_bear(player_health,player_damage,player_speed)
if blackbear==True:
  print("You got the platinum nut.")
  platinum_nut+=1
  OP=input("You found a claw of money. You touch it and if you type the secret you will get the Minigun")
  OP_Choice= ["ALMOND MILK","MILK","ULTIMATE CHERRY"]
  NOICE=random.randchoice(OP_Choice)
  if NOICE==OP:
    print("Congrats! You basically win the entire game.")
    player_damage+=1000
    print("ur damage is:" + player_damage)
  else:
    claw=input("You got a claw and it increased your attack, but lowered you maximum amount of health. (1 to equip 2 to not).")
    if claw == "1":
      attack+=8
      max_player_health-=5
    if claw == "2":
      print("You left the claw behind and got cursed!")
      player_health-=5
if blackbear==False:
  print("You lost.")
pig=fight_pig(player_health, player_damage,player_speed)
if pig==True:
  print("You got the noice bacon")
  noice_bacon+=1
if pig==False:
  print("You lost")
if noice_bacon==1 and platinum_nut==1 and golden_taco==1 and legendary_herb==1 and legendary_banana==1:
  print("You healed the tribe of ligma. You got a cloak that allows you to move first on almost any ocassion.")
  player_speed+=80
#Third Task__________________________________
print("You are appointed to commander of the army")
print(" ")
