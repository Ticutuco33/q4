print("❤️Welcome to Enzo's dating simulator❤️")

def choose_a_date():
    date = input("Choose a date: Kratos, Goku, Sonic, Dante, Master Chief, Gojo, Po, Gru, Senator Armstrong and Doom Guy? ")
    if date == "Kratos" or date == "kratos":
        kratos()
    elif date == "Goku" or date == "goku":
        goku()
    elif date == "Sonic" or date == "sonic":
        sonic()
    elif date == "Dante" or date == "dante":
        kratos()
    elif date == "Master Chief" or date == "master chief":
        master_chief()
    elif date == "Gojo" or date == "gojo":
        gojo()
    elif date == "Po" or date == "po":
        po()
    elif date == "Gru" or date == "gru":
        gru()
    elif date == "Senator Armstrong" or date == "senator armstrong":
        senator_armstrong()
    elif date == "Doom Guy" or date == "doom guy":
        doom_guy()
    else:
        print("Please choose a available date")
    
    
def kratos():
    print("I am the God of War!!! What do you want with me human?")
    kratos_choise1 = input("1. I want to go kill gods with you.\n2. I came here to kill you!!\nMake your choise: ")
    if kratos_choise1 == "1":
        kratos1()
    elif kratos_choise1 == "2":
        deathk()
    else:
        print("Invalid Choise, stupid!")
def kratos1():
    print("I see human, but do you have the strength to fight alongside the God of War?")
    kratos_choise2 = input("1. Tell him that you are stronger then him.\n2. Tell him that you are not that strong but you have the power of revenge.\nMake your Choise: ")
    if kratos_choise2 == "1":
        deathk2()
    elif kratos_choise2 == "2":
        kratos2()
    else:
        print("Invalid choise, stupid!")
def deathk():
    print("You dare to challenge the God of War? Prepare for battle!\nHe completely oblitarated you, womp womp.")
    try_againk = input("Do you want to try again? ")
    if try_againk == "yes":
        kratos()
    elif try_againk == "no":
        choose_a_date()
    else:
        print("Invalid input, stupid!")
def deathk2():
    print("He punches you to test your strength, since your weak he kills you.")
    try_againk = input("Do you want to try again? ")
    if try_againk == "yes":
        kratos()
    elif try_againk == "no":
        choose_a_date()
    else:
        print("Invalid input, stupid!")
def kratos2():
    print("I like your spirit human, I will train you and together we will have our REVENGE!!!\nKratos trains you for a year and now you have become much stronger. Kratos asks which god do you want to take down first?")
    kratos_choise3 = input("1. Hermes\n2. Aphrodite\nMake your choise: ")
    if kratos_choise3 == "1":
        kratos3()
    elif kratos_choise3 == "2":
        death_aphrodite()
    else:
        print("Invalid choise, stupid!")
def death_aphrodite():
    print("Kratos agreed but was not so sure. When you went to fight her you succumbed to her and your desires.\nYour now her slave.")
    try_againk = input("Do you want to try again? ")
    if try_againk == "yes":
        kratos()
    elif try_againk == "no":
        choose_a_date()
    else:
        print("Invalid input, stupid!")
def kratos3():
    print("Good choice, he can run fast but that is everything he does. You and Kratos fought together and killed Hermes pretty easily.\nKratos then asks you, who is next?")
    kratos_choise4 = input("1. We should fight Poseidon. \n2. We should fight Hades.\nMake your choise: ")
    if kratos_choise4 == "1":
        kratos4()
    elif kratos_choise4 == "2":
        kratos4_1()
    else:
        print("Invalid choise, stupid!")
def kratos4():
    print("Great choise Poseidon is strong but together he will be a piece of cake. You and Kratos defeat Poseidon pretty easily. You guys keep defeating more and more gods, until the only god left is Zeus, the god of the gods. Zeus knows that you guys together are too strong so he calls his father Cronos to help him. Kratos wants to fullfill his revenge by killing his father.")
    kratos_choise5 = input("Do you fight Zeus or Cronos?\n1. Zeus\n2. Cronos\nMake your choise: ")
    if kratos_choise5 == "1":
        deathk3()
    elif kratos_choise5 == "2":
        kratos_win()
    else:
        print("Invalid input, stupid!")
def deathk3():
    print("Kratos wants his revenge, he wants to kill his father with his own hands, so he stabs you in the back and you die.")
    try_againk = input("Do you want to try again? ")
    if try_againk == "yes":
        kratos()
    elif try_againk == "no":
        choose_a_date()
    else:
        print("Invalid input, stupid!")
def kratos_win():
    print("You go and take on Cronos, he is strong but you will being filled by anger and revenge you manege to kill Cronos with averege difficulty. Kratos defeats Zeus, both of you and Kratos got their revenge.\nThe End!!!")
    the_endk = input("Do you want to go back to the menu? ")
    if the_endk == "yes":
        choose_a_date()
    elif the_endk == "no":
        print("Bye Bye 🤫🧏‍!!!")
def kratos4_1():
    print("Hades will be hard but we can do it. You and Kratos fight Hades it was a hard battle, you guys won but you came of injured. You two keep defeating all the other gods with averege difficulty, until the only god left is Zeus, the god of the gods. Zeus knows that you guys together are too strong so he calls his father Cronos to help him. Kratos wants to full fill his revenge by killing his father.")
    kratos_choise51 = input("Do you fight Zeus or Cronos?\n1. Zeus\n2. Cronos\nMake your choise: ")
    if kratos_choise51 == "1":
        deathk3()
    elif kratos_choise51 == "2":
        kratos_win_death()
    else:
        print("invalid input, stupid!")
def kratos_win_death():
    print("You go and take on Cronos, but you are still injured from the fight with Hades. The battle is hard and both you and Cronos are in the verge of the death, but with you wanting to fullfill your revenge, you use your last bit of strengh to kill Cronos. Kratos comes to you and say: You fought well my brother, now you may rest. After you he finishes talking you close your eyes and die.\nThe End!!!")
    the_endk2 = input("Do you want to go back to the menu or try again? ")
    if the_endk2 == "menu":
        choose_a_date()
    elif the_endk2 == "try again":
        kratos()
    else:
        print("Invalid input, stupid!")
def goku():
    print("Hey, I am Goku, are you strong?")
    
def sonic():
    print("Sup, I am Sonic, nice to meet, you do you want to race?")
    
def dante():
    print("Hey Devil May Cry, I am Dante, would you like to kill some demons?")
    
def master_chief():
    print("")
    
def gojo():
    print("Your weak. I am Gojo the strongest sorcerer alive, would you like my help in killing curses?")
    
def po():
    print("Hello I am Po, the Dragon Warrior, do you want to help me in saving China?")
    
def gru():
    print("I am Gru, do you want to rob the moon with me?")
    
def senator_armstrong():
    print("I am Senator Armstrong, do you like nano machines son?")
    
def doom_guy():
    print("Kill Demons?")
    
choose_a_date()
