print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

name = input("What is your name? \n")
print(f"\nHello, {name}. Good luck on your quest!")
ship = input("What is the name of your ship? \n")

landing = print("\nA storm is coming in as you approach the island in your boat. \nYou can moor at the impressive headland where a narrow trail leads up the cliff. \nOr you could choose the bay, where there is a meandering track that winds inland.")

landing = input("Where do you land? 'Head' or 'bay'?\n")

if landing.lower() == "bay":
    print(f"\nYou safely moor {ship} in the bay. \nThere is a secluded spot where she will be sheltered from the storm. \nYou and your friend must set out up the track to see what the island holds.")
    friend = input("What is your friend's name?\n")
    print(
        f"\n'Look!' cries {friend}. 'There's a fork in the path. Do you think we should split up?'")
    fork = input(f"Do you and {friend} take the same path? 'Y' or 'N'?\n")
    if fork.lower() == "y":
        path = input("\nWill you go 'left' or 'right'? \n")
        if path.lower() == "right":
            print(
                f"\nYou spot the cave up ahead where you know the treasure is stored. You and {friend} race each other to the entrance, laughing as you go.\nIt's very dark in there, but you were well prepared and brought a torch.\nAlmost as soon as you step inside, the cave narrows to a passage you can only go down single file.")
            passage = input(
                f"Will you 'lead' the way, or 'follow' {friend}?\n")
            if passage.lower() == "follow":
                print(f"\nIt's hard to see what's ahead as {friend} shines the torch ahead. \n'I can see the treasure, {name}!' {friend} exclaims. You breathe a sigh of relief. Almost there.\nThe two of you work awkwardly in the cramped space to open the chest, but eventually you prise it open.\nGold and jewels fill it to the brim. It will be a challenge to carry it back to {ship}.\nStill, it's worth all the effort, you reflect later that evening as you and {friend} are celebrating your wonderful find. \nWhen you get back to the mainland, you'll be set for life!\nCongratulations, {name}! You win!")
            else:
                print(f"\nYou shine your torch ahead of you while {friend} shuffles closely behind you.\nThe passage is uncomfortably narrow, but soon you see a large gleaming chest ahead of you!\n'I see it, {friend}!' you exclaim, and rush forward.\n{friend} follows, not rushing.\nYou feel a sharp pain in your back as the knife penetrates. \nBetrayed! {friend} has literally stabbed you in the back!\nEt tu, {friend}?\nYou died, {name}. Game over.")
        else:
            print(
                f"\nYou are certain you can see the cave where the treasure is rumoured to be held up ahead.\n'Come on, {friend}!' you shout. 'Let's race!'\nIt's a close run thing, but you breathlessly reach the mouth of the cave a split second before {friend} and pause at the threshold.\nThere is a rumble overhead and rocks tumble down on you both.\nBad luck, {name}. Rocks fall, you die. Game over.")
    else:
        print(f"\nYou wave a friendly goodbye to {friend} and start along your way. \nIt is a beautiful island with delightful scenery.\nAs you walk, you watch a large eagle soaring overhead and fail to spot the large hole in the path. You fall in.\nSorry, {name}. You died. Game over.")
else:
    print(
        f"\nYou lose control of {ship} as the storm pushes her towards the rocks. \nYou are drowned in the shipwreck. \nGame over, {name}.")
