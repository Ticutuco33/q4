print("❤️Welcome to Enzo's dating simulator❤️")

def choose_a_date():
    date = input("Choose a date: Kratos, Goku, Sonic, Dante, Master Chief, Gojo, Po, Gru, Senator Armstrong and Doom Guy? ")
    if date == "Kratos" or "kratos":
        kratos()
    elif date == "Goku" or "goku":
        goku()
    elif date == "Sonic" or "sonic":
        sonic()
    elif date == "Dante" or "dante":
        kratos()
    elif date == "Master Chief" or "master chief":
        master_chief()
    elif date == "Gojo" or "gojo":
        gojo()
    elif date == "Po" or "po":
        po()
    elif date == "Gru" or "gru":
        gru()
    elif date == "Senator Armstrong" or "senator armstrong":
        senator_armstrong()
    elif date == "Doom Guy" or "doom guy":
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
    try_again = input("Do you want to try again? ")
    if try_again == "yes":
        kratos()
    elif try_again == "no":
        choose_a_date()
    else:
        print("Invalid input, stupid!")
def deathk2():
    print("He punches you to test your strength, since your weak he kills you.")
def kratos2():
    print("I like your spirit human, I will train you and together we will have our REVENGE!!!\nKratos trains you for a year and now you have become much stronger. Kratos asks which god do you want to take down first?")
    kratos_choise3 = input("1. Hermes\n2. Aphrodite\nMake your choise: ")
    if kratos_choise3 == "1":
        kratos3()
    elif kratos_choise3 == "2":
        print("Kratos agreed but was not so sure. When you went to fight her you succumbed to her and your desires.\nYour now her slave.")
    else:
        print("Invalid choise, stupid!")
def kratos3():
    print("Good choice, he can run fast but that is everything he does. You and Kratos fought together and killed Hermes pretty easily.\nKratos then asks you, who is next?")
    
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
